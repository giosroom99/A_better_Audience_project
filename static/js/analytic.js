

google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      
      const rev1 =  parseInt($('#review1_avg').text())
      const rev2 =  parseInt($('#review2_avg').text())
      const rev3 =  parseInt($('#review3_avg').text())


      const data = google.visualization.arrayToDataTable([
        ["Element", "Audience Review", { role: "style" } ],
        ["Demonstrates all final project requirements (Give score 0-100)\n" +
        "\n 1", rev1, "#34ebe1"],
        ["Originality of project's demonstration of class concepts (Give a score 0-100))\n" +
        "\n", rev2, "#3458eb"],
        ["Overall demonstration of mastery of course material ? (Give a score 0-100)", rev3, "#cf1df2"],
     
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
        chartArea: {width: '80%'},
        // width: 'auto',
        // height: 400,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
        backgroundColor: '#012e45',
        colors:['red','#004411'],
      };
      const chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
      chart.draw(view, options);
  }