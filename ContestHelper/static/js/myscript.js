$( "#create" ).click(function() { 

	if($('#form2').is(':visible'))
		$("#form2").toggle(); 

	$("#form1").toggle();
 
});


$( "#join" ).click(function() { 

	if($('#form1').is(':visible'))
		$("#form1").toggle(); 

	$("#form2").toggle();
 
});

$("#form1").on('submit',function(e){ 
	e.preventDefault();

	$.ajax({
		url: $("#form1").attr("form-url") ,
		type: "GET",
		data:{ 
			section : $("input[name='section']",this).val()
		}  ,
		dataType: 'json',
		success: function (data) {
			alert(	data.sectionName  );
		}
	});



});


$("#form2").on('submit',function(e){ 
	e.preventDefault();
	$('[name=group]').val("")

});
 