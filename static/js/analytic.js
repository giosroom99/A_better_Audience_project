

google.charts.load("current", {packages:["corechart"]});
google.charts.setOnLoadCallback(drawChart);
function drawChart() {

  const rev1 =  parseInt($('#review1_avg').text())
  const rev2 =  parseInt($('#review2_avg').text())
  const rev3 =  parseInt($('#review3_avg').text())


  const data = google.visualization.arrayToDataTable([
    // ["Element", "Peer Review", { role: "style" } ],
    // ["Demonstrates all final project requirements (Give score 0-100)", rev1, "#34ebe1"],
    // ["Originality of project's demonstration of class concepts (Give a score 0-100))", rev2, "#3458eb"],
    // ["Overall demonstration of mastery of course material ? (Give a score 0-100)", rev3, "#cf1df2"],

    ["Element", "Peer Review", { role: "style" } ],
    ["Rubric 1", rev1, "#34ebe1"],
    ["Rubric 2", rev2, "#3458eb"],
    ["Rubric 3", rev3, "#cf1df2"],

  ]);

  const view = new google.visualization.DataView(data);
  view.setColumns([0, 1,
    { calc: "stringify",
      sourceColumn: 1,
      type: "string",
      role: "annotation" },
    2]);

  const options = {
    title: "AVG Reviews Based on Audience Rating",
    titleTextStyle:{ color: 'White',

      fontSize: 14,
      bold: true,
    },

    chartArea: { width: 410, },


    legend: { position: "",
      textStyle: {color: 'White',
        fontSize:10,},
      alignment:'end'


    },
    // #012e45
    backgroundColor: '#012e45',
    colors:['#34ebe1','#3458eb','#cf1df2'],
  };
  const chart = new google.visualization.PieChart(document.getElementById("piechart"));
  chart.draw(view, options);
}
