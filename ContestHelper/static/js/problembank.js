var problemset = [];

$("#LoadingImage").show(); 


function Problem() {
	var topic = $("#topic option:selected").val();
	var diff =parseInt( $("#diff option:selected").val() )  ;
	$("#problemset td").remove();

	for (var key in problemset){
		if (problemset[key][topic] ==1 &&  problemset[key]['difficulty']<=diff ){
			var row  = "<tr>";
			row+='<td><a href= # >'+ key.toString() +' </td>';
			row+='<td>'+ problemset[key]['title'] + '</td>';
			row+='<td>'+ problemset[key]['difficulty'] .toString() + '</td>';

			if(problemset[key]['solved'] == 1)
				row+='<td>YES</td>';
			else
				row+='<td>NO</td>';
			row+="/<tr>";

			$('#problemset > tbody:last').append(row); 			
		}

	}
 

}

$.ajax({
	url: $("#info").attr("href"),
	type: "POST",
	data:{
        "csrfmiddlewaretoken": $('#info').attr("token-id") ,
		"pk": $('#info').attr("user_pk") ,
		"topic": $("#topic option:selected").val(),
		"diff": $("#diff option:selected").val()
	},	

	datType: 'Json',

	success: function(response){ 
		$("#LoadingImage").hide(); 
		problemset = response;
		Problem();

	}
});
 



$("#topic").on('change',function() {Problem();});
$("#diff").on('change',function() {Problem();});