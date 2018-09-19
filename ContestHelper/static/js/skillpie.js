var a = document.getElementById("profile"); 
  
if (a)
    draw("profile"); 


function draw (ID)
{
    $("#LoadingImage").show();
    $.ajax({
        url: $('#' + ID).attr("canvas-url"),
        type: "GET",

        data:{

        },

        dataType: 'json',

        success: function (server_response) { 
            $("#LoadingImage").hide();
            $("#profile").show();
            var abc = new RGraph.Radar({ 
                id: ID,
                data: [ [0, server_response['DP'], server_response['Graph'],server_response['Flow'],server_response['Number Theory'],server_response['String'],server_response['Geometry'] ] ],
                options: {
                    textAccessible: true,
                    tooltips: [
                        '', 'DP', 'Graph','Flow','Number Theory','String','Geometry'
                    ],
                    backgroundCirclesPoly: true,
                    backgroundCirclesSpacing: 30,
                    colors: ['transparent'],
                    axesColor: 'transparent',
                    highlights: true,
                    strokestyle: ['red'],
                    linewidth: 2,
                    labels: ['', 'DP', 'Graph','Flow','Number Theory','String','Geometry'],
                    labelsAxes: 'n',
                    textSize: 16,
                    clearto: 'white',
                    labelsAxesBoxed: true,
                    labelsAxesBoxedZero: false,
                    textAccessible: true
                }
            }).grow();
            $("#uvacount").html(server_response['uva']);

        }



    } );
        
}



 