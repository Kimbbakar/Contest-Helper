draw('cvs'); 


function draw (ID)
{
    var abc = new RGraph.Radar({ 
    id: ID,
    data: [ [0, 8,7,6,7,8,6,1] ],
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
}



 