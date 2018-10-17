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
				$('#table2 > tbody:last').append('<tr><td><a href= /section/'+data.pk +' > ' +data.sectionName + ' </td> <td>Teacher</td></tr>'); 

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


$("#checkproblem").on('submit',function(e){ 
	e.preventDefault();  

	if ($("input[name='problemid']").val().length ){
		$("#solver").show();
		$.ajax({
			url:   $("#checkproblem").attr("href") ,
			type: "POST",

			data:{ 
	            "csrfmiddlewaretoken": $('#info').attr("token-id") ,
				"id" : $("input[name='problemid']").val() ,
				"section_pk": $("#info").attr("section")
			}  ,
			dataType: 'json',
			success: function (data) {

				if(data.solver.length){
					$("#solver td").remove();
					for(var i =0;i < data.solver.length  ;i++)
					{
		  
						$('#solver > tbody').append('<tr><td>' + data.solver[i].username + ' </td></tr>'); 
					}  
				}
				else
					alert("No one solve this problem");
			}
		});		
	}
	else{
		alert("Problem ID invalid");
	} 


});


function delFunction(e) { 

/*	$(e).preventDefault(); */
	
	var r = confirm("Wants to remove a student?");
	
	if (r==true){
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
	}



	return false; 
}

$("#chelper").on('submit',function(e){ 
	e.preventDefault();     
	$.ajax({
		url:   $("#chelper").attr("form-url")  ,
        type: "POST",
		data: {
            "csrfmiddlewaretoken": $('#info').attr("token-id") ,
			"type": $("#contest").val(),
			"section": $("#info").attr("section"),
			"coach": $("#coach").val()

		} ,
		dataType: 'json',
		success: function (data) {
 
			$("#table5 td").remove();
			for(var i =0;i < data.problem.length  ;i++)
			{
  
				$('#table5 > tbody').append('<tr><td><a href= /'+data['problem'][i] .number + ' > ' +data['problem'][i] .number + ' </td> <td>' +   data['problem'][i] .title  +'</td></tr>'); 
			}  
		}
	});
}); 