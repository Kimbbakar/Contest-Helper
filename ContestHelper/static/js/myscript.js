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
			section : $("input[name='section']").val()
		}  ,
		dataType: 'json',
		success: function (data) {
			$("input[name='section']").val("");
			alert(	data.messege  );

			if( data.messege === 'Section open successfully!!' ){
				$('#table1 > tbody:last').append('<tr><td><a href= /section/'+data.pk +' > ' +data.sectionName + ' </td> <td>Teacher</td></tr>'); 

			}

		}
	});



});


$("#form2").on('submit',function(e){ 
	e.preventDefault();
	$('[name=group]').val("")

});
 