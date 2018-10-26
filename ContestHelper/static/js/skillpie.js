var a = document.getElementById("profile"); 
  
if (a)
    draw("profile"); 


function draw (ID,update = false)
{  
    if (update==false){
        $("#uvacount").html("?");  
        $("#LoadingImage").show(); 
    }
    else{
        alert("Information will be updated with int 5 minutes!");        
    } 

    $.ajax({

        url: $('#info' ).attr("user-info-url"),
        type: "POST",

        data:{
            "csrfmiddlewaretoken": $('#info').attr("token-id") ,
            "update": update
        },

        dataType: 'json',

        success: function (server_response) { 
            $("#uvacount").html(server_response['uva']);

            if(update==false){
                $("#LoadingImage").hide();
                $("#profile").show();

                var abc = new RGraph.Radar({ 
                    id: ID,
                    data: [ [0, server_response['DP'], server_response['GRAPH'],server_response['STRING'],server_response['NT'],server_response['GEO'] ] ],
                    options: {
                        textAccessible: true,
                        tooltips: [
                            '', 'Dynamic Programming', 'Graph Theory','String','Number Theory','Geometry'
                        ],
                        backgroundCirclesPoly: true,
                        backgroundCirclesSpacing: 30,
                        colors: ['transparent'],
                        axesColor: 'transparent',
                        highlights: true,
                        strokestyle: ['green'],
                        linewidth: 2,
                        labels: ['', 'DP', 'GRAPH','STRING','NT','GEO'],
                        labelsAxes: 'n',
                        textSize: 16,
                        clearto: 'white',
                        labelsAxesBoxed: true,
                        labelsAxesBoxedZero: false,
                        textAccessible: true
                    }
                }).grow();
            } 


        }



    } );
        
}


$("#update").on('click',function(){ 
    draw("profile",true);


});