// Ayudantes de gráficos (Chart.js 4). Paleta categórica validada en orden fijo.
const PAL = ["#2a78d6","#eb6834","#1baf7a","#eda100","#e87ba4","#008300"];
const INK = "#111827", INK2 = "#4b5563", GRID = "#eef0f3";
Chart.defaults.font.family = '"Segoe UI",Calibri,system-ui,sans-serif';
Chart.defaults.color = INK2;
Chart.defaults.plugins.legend.labels.boxWidth = 10;
Chart.defaults.plugins.legend.labels.boxHeight = 10;
Chart.defaults.plugins.legend.labels.usePointStyle = true;
Chart.defaults.plugins.tooltip.backgroundColor = "#0f1f3d";
Chart.defaults.plugins.tooltip.padding = 10;
Chart.defaults.animation = false;

function tableFor(el, labels, series){
  const d=document.createElement('details');
  const s=document.createElement('summary'); s.textContent='Ver datos en tabla'; d.appendChild(s);
  const t=document.createElement('table'); const thead=t.createTHead(); const hr=thead.insertRow();
  hr.insertCell().textContent=''; labels.forEach(l=>{ const c=document.createElement('th'); c.textContent=l; hr.appendChild(c); });
  const tb=t.createTBody();
  series.forEach(sr=>{ const r=tb.insertRow(); const th=document.createElement('th'); th.textContent=sr.name; r.appendChild(th); sr.data.forEach(v=>{ r.insertCell().textContent=(v===null||v===undefined)?'—':v; }); });
  d.appendChild(t); el.parentElement.appendChild(d);
}
function base(opts){ return Object.assign({responsive:true,maintainAspectRatio:false,interaction:{mode:'index',intersect:false},
  scales:{x:{grid:{display:false},ticks:{color:INK2}},y:{grid:{color:GRID},border:{display:false},ticks:{color:INK2},beginAtZero:true}}}, opts||{}); }

function mkLine(id, labels, series, o){ o=o||{}; const el=document.getElementById(id);
  new Chart(el,{type:'line',data:{labels,datasets:series.map((s,i)=>({label:s.name,data:s.data,borderColor:PAL[i],backgroundColor:PAL[i],borderWidth:2,pointRadius:4,pointHoverRadius:6,tension:.25,spanGaps:true,fill:false}))},
   options:base({plugins:{legend:{display:series.length>1}},scales:{x:{grid:{display:false}},y:{grid:{color:GRID},border:{display:false},beginAtZero:o.zero!==false,suggestedMax:o.max,ticks:{callback:v=>o.unit?v+o.unit:v}}}})});
  tableFor(el,labels,series); }
function mkBar(id, labels, series, o){ o=o||{}; const el=document.getElementById(id);
  new Chart(el,{type:'bar',data:{labels,datasets:series.map((s,i)=>({label:s.name,data:s.data,backgroundColor:PAL[i],borderRadius:4,borderSkipped:'start',maxBarThickness:34,borderWidth:o.stacked?2:0,borderColor:'#fff'}))},
   options:base({indexAxis:o.horizontal?'y':'x',plugins:{legend:{display:series.length>1}},
     scales:o.horizontal?{x:{grid:{color:GRID},border:{display:false},beginAtZero:true,stacked:!!o.stacked,ticks:{callback:v=>o.unit?v+o.unit:v}},y:{grid:{display:false},stacked:!!o.stacked}}
                        :{x:{grid:{display:false},stacked:!!o.stacked},y:{grid:{color:GRID},border:{display:false},beginAtZero:true,stacked:!!o.stacked,suggestedMax:o.max,ticks:{callback:v=>o.unit?v+o.unit:v}}}})});
  tableFor(el,labels,series); }
function mkDonut(id, labels, data, o){ o=o||{}; const el=document.getElementById(id);
  new Chart(el,{type:'doughnut',data:{labels,datasets:[{data,backgroundColor:PAL.slice(0,labels.length),borderColor:'#fff',borderWidth:2,hoverOffset:4}]},
   options:{responsive:true,maintainAspectRatio:false,cutout:'62%',plugins:{legend:{position:'right'},tooltip:{callbacks:{label:c=>' '+c.label+': '+c.parsed+(o.unit||'')}}}}});
  tableFor(el,labels,[{name:o.name||'Valor',data}]); }
