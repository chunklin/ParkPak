var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;
var req = new XMLHttpRequest();
var x = req;
var i=0;
while(i<19){
x.open('GET', 'https://newsapi.org/v2/top-headlines?country=us&apiKey=c5eb346b60fd47e9a84f53b29e3dc280',false);
x.send();

x.onload = function() {
  if (x.status != 200) {
  } else {
 //console.log(JSON.parse(x.responseText));
 console.log(JSON.parse(x.responseText)["articles"][i]["title"]);
// document.getElementById('news').innerHTML = JSON.parse(x.responseText)["articles"][i]["title"];
 //console.log(x.responseText[0])
  }
};
console.log(i) ;
i++
}
