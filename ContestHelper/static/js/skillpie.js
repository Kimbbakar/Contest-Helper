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

        success: function (response) { 
            $("#uvacount").html(response['uva']);

            if(update==false){
                $("#LoadingImage").hide();
                $("#profile").show();

                var abc = new RGraph.Radar({ 
                    id: ID,
                    data: [ [ response['NONE'],response['DP'], response['GRAPH'],response['STRING'],response['NT'],response['GEO'] ] ],
                    options: {
                        textAccessible: true,
                        tooltips: [
                             response['NONE'].toString() ,response['DP'].toString(), response['GRAPH'].toString(),response['STRING'].toString(),response['NT'].toString(),response['GEO'].toString()
                        ],
                        backgroundCirclesPoly: true,
                        backgroundCirclesSpacing: 30,
                        colors: ['#463D72'],
                        axesColor: 'transparent',
                        highlights: true,
                        strokestyle: ['#463D72'],
                        linewidth: 2,
                        labels: [ 'Untaged','DP', 'GRAPH','STRING','NT','GEO'],
                        labelsAxes: '0',
                        textSize: 16,
                        clearto: 'white',
                        labelsAxesBoxed: false,
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