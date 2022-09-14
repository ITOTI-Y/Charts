

var dom = document.getElementById("chart-container");
var myChart = echarts.init(dom, null, {
  renderer: "canvas",
  useDirtyRect: false,
});
var app = {};
var chart = 1;
var option;

option = {
  toolbox: {
    feature: {
      dataView: {
        show: true,
        readOnly: false,
        optionToContent: function(opt){
          var data = opt.dataset[0].source
          var t_head = '<table class="biaoti"><tr><th>'+ 'Time' + '</th>'
          for (var i=0, len = data.length; i<len; i++){
            if(i!= 0){
              if (data[i][0]!=data[i-1][0]){
                t_head += '<th>'+data[i][0]+'</th>'
              }
            }
            else{
              t_head += '<th>'+data[i][0]+'</th>'
            }
          }
          t_head += '</tr></table>'
          console.log(data)
          console.log(opt)
          return t_head
      },
      },
    },
  },
  tooltip: {
    position: "top",
    triggerOn:"click",
  },
  dataset: {
    dimensions: ["columns", "row", "value"],
    source: [
      ["columns1", "row1", 1],
      ["columns1", "row2", 3],
      ["columns2", "row1", 2],
      ["columns2", "row2", 4],
    ],
  },
  xAxis: {
    type: "category",
    axisLabel: { interval: 0, rotate: 0 },
  },
  yAxis: {
    type: "category",
  },
  series: {
    name: "Concentration",
    type: "heatmap",
    label: {
      show: true,
    },
    encode: { x: "columns", y: "row" },
    datasetIndex: 0,
  },
};

if (option && typeof option === "object") {
  myChart.setOption(option);
}

window.addEventListener("resize", myChart.resize);
