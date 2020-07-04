$(document).ready(function(){

	  
	  $("#contact").submit(function(e) {

			e.preventDefault(); // preent the execution of submit form

			var form = $(this);
			var url = form.attr('action');

			$.ajax({
				   type: "GET",
				   url: url,
				   data: form.serialize(), 
				   success: function(data)
				   {
					    var btn = $("myBtn");
					    $('#text_in_modal').html(data["date"]) // put date into DOM element inside pop-up window
					    $("#myModal").show('blind', {}, 600)   // display pop-up window with effect
						$("#contact").trigger("reset");	// reset the form 
						setTimeout(function() { // hide the pop-up window after 2 seconds
							$("#myModal").hide('blind', {}, 100)
						}, 2000)
				   }
				 });


		});
	  	  
	});