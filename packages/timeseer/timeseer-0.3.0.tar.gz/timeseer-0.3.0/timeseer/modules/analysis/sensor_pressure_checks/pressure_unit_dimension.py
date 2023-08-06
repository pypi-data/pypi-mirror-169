""" Check if the unit has a dimension that matches pressure"""


from timeseer import AnalysisInput, AnalysisResult, DataType
from timeseer.analysis.utils.unit_dimension_match import unit_not_matching_dimension


_CHECK_NAME = "pressure unit dimension"
_EVENT_FRAME_NAME = "Unit not matching pressure"

META = {
    "checks": [
        {
            "name": _CHECK_NAME,
            "event_frames": [_EVENT_FRAME_NAME],
        }
    ],
    "conditions": [
        {
            "min_series": 1,
            "min_data_points": 1,
            "data_type": [DataType.STRING],
        }
    ],
    "signature": "univariate",
}


# pylint: disable=missing-function-docstring
def run(
    analysis_input: AnalysisInput,
) -> AnalysisResult:

    parameters = {}
    parameters["value"] = "[pressure]"
    analysis_input.parameters = parameters
    return unit_not_matching_dimension.run(analysis_input)
