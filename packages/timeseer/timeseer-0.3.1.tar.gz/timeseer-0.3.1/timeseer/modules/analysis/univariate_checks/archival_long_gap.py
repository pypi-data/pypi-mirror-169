"""There is a much longer period between data being recorded than expected based on history.

<p>This check identifies periods of time where no data
has been archived. These could be indications of issues with
connectivity or offline sensors.</p>
<p class="scoring-explanation">The score for this check is based on the total amount of time
where there seems to be gaps relative to the total time range of the analysis.</p>
<div class="ts-check-impact">
<p>
A series that does not put out any data might be faulty or could indicate a network failure.
Failing to detect this could lead to wrong process operation when attempting to obtain a particular
interval of operation.
</p>
</div>
"""

from datetime import datetime, timedelta

import jsonpickle
import numpy as np
import pandas as pd

from timeseer import AnalysisInput, AnalysisResult, EventFrame

from timeseer.analysis.utils import (
    event_frames_from_dataframe,
    process_open_intervals,
    handle_open_intervals,
)

_CHECK_NAME = "Increased archival step size"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "event_frames": ["Increased archival step size"],
        }
    ],
    "conditions": [
        {
            "min_series": 1,
            "min_data_points": 3,
        }
    ],
    "signature": "univariate",
}


def _get_cutoff_for_gap(sketch):
    if sketch.max == sketch.min:
        return 5 * sketch.max

    if sketch.count <= 30:
        return sketch.max

    q25, q75 = [sketch.get_quantile_value(q) for q in [0.25, 0.75]]
    iqr = q75 - q25

    if iqr == 0:
        return 5 * q25

    return q75 + 3 * iqr


def _is_frame_long_enough(frame, df, delta):
    end_date = frame.end_date
    if frame.end_date is None:
        end_date = df.index[-1]

    return (
        end_date.replace(tzinfo=None) - frame.start_date.replace(tzinfo=None)
    ) >= timedelta(seconds=delta)


def _filter_stale_event_frames(all_frames, df, delta):
    filter_iterator = filter(lambda x: _is_frame_long_enough(x, df, delta), all_frames)
    return filter_iterator


def _get_intervals(active_points, df, event_type):
    interval_grp = (active_points != active_points.shift().bfill()).cumsum()
    active_points[active_points.isna()] = 0
    active_points = np.array(active_points, dtype=bool)
    intervals = (
        df.assign(interval_grp=interval_grp)[active_points]
        .reset_index()
        .groupby(["interval_grp"])
        .agg(start_date=("ts", "first"), end_date=("ts", "last"))
    )
    intervals["type"] = event_type
    return intervals


def _clean_dataframe(df: pd.DataFrame):
    return df[~df.index.duplicated(keep="first")].sort_index()


def _run_gap_check(
    analysis_input: AnalysisInput, stale_sketch
) -> tuple[list[EventFrame], datetime]:
    df = _clean_dataframe(analysis_input.data)

    delta = _get_cutoff_for_gap(stale_sketch)
    active_points = pd.DataFrame(
        {"value": ((df.index.to_series().diff()).dt.total_seconds() > delta)}
    )
    active_points = active_points | active_points.shift(-1).bfill()

    intervals = _get_intervals(active_points, df, _CHECK_NAME)
    intervals = handle_open_intervals(df, intervals)

    frames = _filter_stale_event_frames(
        event_frames_from_dataframe(process_open_intervals(intervals)), df, delta
    )

    last_analyzed_point = df.index[-1]

    return frames, last_analyzed_point


def _get_relevant_statistic(analysis_input, stat_name):
    statistics = [
        statistic.result
        for statistic in analysis_input.statistics
        if statistic.name == stat_name
    ]
    if statistics is None or len(statistics) == 0:
        return None
    return statistics[0]


# pylint: disable=missing-function-docstring
def run(
    analysis_input: AnalysisInput,
) -> AnalysisResult:
    median_archival_step = _get_relevant_statistic(
        analysis_input, "Archival time median"
    )
    json_stale_sketch = _get_relevant_statistic(analysis_input, "Archival Sketch")
    if median_archival_step is None:
        return AnalysisResult(condition_message="No median archival step")
    if json_stale_sketch is None:
        return AnalysisResult(condition_message="No archival sketch")
    stale_sketch = jsonpickle.decode(json_stale_sketch)

    frames, last_analyzed_point = _run_gap_check(analysis_input, stale_sketch)

    return AnalysisResult(
        event_frames=list(frames),
        last_analyzed_point=last_analyzed_point,
    )
