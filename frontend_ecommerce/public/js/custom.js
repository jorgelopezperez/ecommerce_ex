$(document).ready(function() {


    $('input').change(function() {
        if ($(this).val()) {
            $(this).addClass("modified-input")
        }
    });


    $("#contact").submit(function(e) {

        e.preventDefault(); // preent the execution of submit form

        var form = $(this);
        var url = form.attr('action');

        $.ajax({
            type: "GET",
            url: url,
            crossDomain: true,
            "headers": {
                "accept": "application/json",
                "Access-Control-Allow-Origin": "*"
            },
            dataType: 'jsonp',
            data: form.serialize(),
            success: function(data) {
                var btn = $("myBtn");
                $('#text_in_modal').html(data["date"]) // put date into DOM element inside pop-up window
                $("#myModal").show('blind', {}, 600) // display pop-up window with effect
                $("#contact").trigger("reset"); // reset the form 
                setTimeout(function() { // hide the pop-up window after 2 seconds
                    $("#myModal").hide('blind', {}, 100)
                }, 2000)
                $('input').removeClass("modified-input")
            }
        });


    });

});