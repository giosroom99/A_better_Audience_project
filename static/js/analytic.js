



google.charts.load("current", {packages:["corechart"]});
    google.charts.setOnLoadCallback(drawChart);
    function drawChart() {
      
      const rev1 =  parseInt($('#review1_avg').text())
      const rev2 =  parseInt($('#review2_avg').text())
      const rev3 =  parseInt($('#review3_avg').text())


      console.log(rev2)
      var data = google.visualization.arrayToDataTable([
        ["Element", "Audience Review", { role: "style" } ],
        ["Review 1", rev1, "#34ebe1"],
        ["Review 2", rev2, "#3458eb"],
        ["Review 3", rev3, "#cf1df2"],
     
      ]);

      var view = new google.visualization.DataView(data);
      view.setColumns([0, 1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation" },
                       2]);

      var options = {
        title: "AVG Reviews Based on Audience Rating",
        chartArea: {width: '80%'},
        // width: 'auto',
        // height: 400,
        bar: {groupWidth: "95%"},
        legend: { position: "none" },
        backgroundColor: '#012e45',
        colors:['red','#004411'],
      };
      var chart = new google.visualization.BarChart(document.getElementById("barchart_values"));
      chart.draw(view, options);
  }