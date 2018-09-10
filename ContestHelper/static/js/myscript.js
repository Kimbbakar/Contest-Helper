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


$("#form4").on('submit',function(e){ 
	e.preventDefault(); 
	token =  $("#form4").attr("token") ;
	type: "GET",

	$.ajax({
		url:  $("#form4").attr("form-url") ,


		data:{ 
			student : $("input[name='student']").val() 
		}  ,
		dataType: 'json',
		success: function (data) {

 			if( data.messege === "Student has been added!!" ){
				$("input[name='student']").val("");
				$('#table3 > tbody:last').append('<tr><td><a href= /'+data.pk + ' > ' +data.student + ' </td> <td> <button onclick=delFunction(this) class="btn btn-info"  pk = ' + data.pk +  ' > Remove </button></td></tr>'); 

			} 
			alert(data.messege);

		}
	});
});


function delFunction(e) { 

/*	$(e).preventDefault(); */
	type: "GET", 

	$.ajax({
		url: $("#abc").attr("form-url") ,

		data:{ 
			student : $(e).attr("pk") 
		}  ,
		dataType: 'json',
		success: function (data) {
			alert(data.messege);

		}
	});
	$(e).closest('tr').remove();


	return false; 
}


 