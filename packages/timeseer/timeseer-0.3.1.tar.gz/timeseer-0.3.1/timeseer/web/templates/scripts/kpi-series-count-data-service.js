(function () {
  var kpiCounts = {{ graph_kpi_counts|tojson }};
  var comparisonKPICounts = {{ graph_comparison_counts|tojson }}
  var kpis = {{ kpi_set_entries|map(attribute='kpi')|sort(attribute='name')|map(attribute='name')|list|tojson }};
  var totalSeries = {{report.series_count|tojson }}

  var counts = kpis.map(function (kpi) {return kpiCounts[kpi]||0;});
  var comparisonCounts = kpis.map(function (kpi) {return comparisonKPICounts[kpi];});

  var data = [];
  {% if (compare_evaluation is defined and compare_evaluation is not none) or compare_to is not none %}
  if (Object.keys(comparisonKPICounts).length > 0) {
    data.push({
      type: 'scatterpolar',
      r: comparisonCounts,
      theta: kpis,
      fill: 'toself',
      {% if compare_evaluation is defined and compare_evaluation is not none %}
      name: new Date('{{ compare_evaluation.evaluation_date.isoformat() }}').toLocaleString()
      {% else %}
      name: '{{ compare_to }}'
      {% endif %}
    });
  }
  {% endif %}
  data.push({
    type: 'scatterpolar',
    r: counts,
    theta: kpis,
    fill: 'toself',
    name: 'Current evaluation'
  });

  var layout = {
    polar: {
      radialaxis: {
        visible: true,
        range: [totalSeries, 0]
      }
    },
    showlegend: true,
    legend: {
      xanchor: 'right',
      x: 1.2,
      y: 1.2
    },
    margin: {
      t: 0,
      l: 15,
      r: 0,
      b: 30,
    }
  }
  if (totalSeries < 6) {
    layout.polar.radialaxis.tickvals = [];
    for (var i=totalSeries; i>=0; i--) {
      layout.polar.radialaxis.tickvals.push(i);
    }
  }

  Plotly.newPlot("timeseries_source_score", data, layout);
})();
