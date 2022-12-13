

// $("#search-presentations").on("change paste keyup", function() {
//   console.log("hello")
//   $('#button-search').click()
// });



$(window).on('load', function() {
    $('#myModal').modal('show');
});

function getActivity(){
// Display the div that is initially hidden
    $('#activity-text').show();

    // Make a AJAX request
    $.ajax({
        url: 'https://www.boredapi.com/api/activity/',
        dataType: 'json',
        success: function(data) {
            console.log(data);
            const activity = data['activity'];
            const type = data['type'];

            console.log(activity, type);

            // Update the page with the information received from the API
            $('#activity-text').text(activity);
            $('#activity-type').text(type);
        }
    });

}


getActivity()
