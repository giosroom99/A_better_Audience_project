// google.charts.load("current", {packages:['corechart']});
// google.charts.setOnLoadCallback(drawChart);
// function drawChart() {
//   var data = google.visualization.arrayToDataTable([
//     ["Element", "Density", { role: "style" } ],
//     ["Copper", 8.94, "#b87333"],
//     ["Silver", 10.49, "silver"],
//     ["Gold", 19.30, "gold"],
//     ["Platinum", 21.45, "color: #e5e4e2"]
//   ]);
//
//   var view = new google.visualization.DataView(data);
//   view.setColumns([0, 1,
//                    { calc: "stringify",
//                      sourceColumn: 1,
//                      type: "string",
//                      role: "annotation" },
//                    2]);
//
//   var options = {
//     title: "AVG Reviews Based on Audience Rating",
//         chartArea: {width: '80%'},
//         // width: 'auto',
//         // height: 400,
//         bar: {groupWidth: "95%"},
//         legend: { position: "none" },
//         backgroundColor: '#012e45',
//         colors:['red','#004411'],
//   };
//   var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
//   chart.draw(view, options);
// }