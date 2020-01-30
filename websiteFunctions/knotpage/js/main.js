function allowDrop(ev) {
  ev.preventDefault();
}

function drag(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
    //console.log(ev.target.parentElement.id)
    ev.dataTransfer.setData("parentid", ev.target.parentElement.id)
    //console.log("from the list")
}

function dragBox(ev) {
    ev.dataTransfer.setData("text", ev.target.id);
    ev.dataTransfer.setData("parentid", ev.target.parentElement.id)
    //console.log(ev.target.parentElement.id)
    //console.log("from a box")
}


function drop2(ev){
    ev.preventDefault();
    var data=ev.dataTransfer.getData("text");
    var s=document.getElementById(data);
    ev.target.appendChild(s);
    ev.target.src=s.src;
    ev.dataTransfer.clearData();
}


var i = 1
function drop(ev){
    ev.preventDefault();
    var data=ev.dataTransfer.getData("text");
    var name=ev.dataTransfer.getData("parentid");
    //var parnt=document.getElementById(data).parentElement.id;
    /* What I want is to have this function "read" where the image came from:
    if it came from a "B"ox, then don't copy it, but do copy it otherwise. */
    if (name.includes("B")) {
      var s=document.getElementById(data);
    } else {
      var s=document.getElementById(data).cloneNode(true);
      s.id = 'dragged' + i;
      i++
    }
    //console.log(name);
    //console.log(s)
    //console.log(data);
    //var s=document.getElementById(data).cloneNode(true);
    ev.target.appendChild(s);
    ev.target.src=s.src;
    ev.dataTransfer.clearData();
    delete s
    delete name
    delete data

  var size = window.value;
  console.log(size)
  var lim = size*size;
  console.log(lim)
  var j;
  var tilearray = Array(0);
  for (j = 1; j < lim; j++) {
    parent = "B" + j;
    var kid;
    kid = document.getElementById(parent).children;
    var haskids
    haskids = kid.length;
    if (haskids != 0) {
      var tilesource = document.getElementById(parent).children[0].src.toString();
      var tile = tilesource.substring(67, tilesource.length - 4);
      tilearray.push(tile)
    } else {
      tile = "0"
      tilearray.push(tile)
    }
  }
  //console.log(tilearray);
  finalarray = "[" + tilearray.toString() + "]";
  document.getElementById("results").innerHTML = "The array for this knot is " + finalarray + "." ;
    }


function trashdrop(ev){
    ev.preventDefault();
    var data=ev.dataTransfer.getData("text");
    var name=ev.dataTransfer.getData("parentid");
    //var parnt=document.getElementById(data).parentElement.id;
    /* What I want is to have this function "read" where the image came from:
    if it came from a "B"ox, then don't copy it, but do copy it otherwise. */
    if (name.includes("B")) {
      var s=document.getElementById(data);
    } else {
      var s=document.getElementById(data).cloneNode(true);
      s.id = 'dragged' + i;
      i++
    }
    //console.log(name);
    //console.log(s)
    //console.log(data);
    //var s=document.getElementById(data).cloneNode(true);
    ev.target.appendChild(s);
    ev.dataTransfer.clearData();
    delete s
    delete name
    delete data
    }


/* old drop event handler
function drop(ev) {
  ev.preventDefault();
  var data=ev.dataTransfer.getData("text/html");
  var nodeCopy = document.getElementById(data).cloneNode(true);
  nodeCopy.id = "newId";
  ev.target.appendChild(nodeCopy);
}

*/



function Submitbuttonclick(ev) {
  //console.log("clicked")
  
}


/* old attempt at getting the tile array
console.log("clicked2")
var k;
for (k = 1; k < 9; k++) {
dj = "dragged" + k;
var kid2;
parent = "B" + k;
var kid3;
kid3 = document.getElementById(parent).children;
/*var boolkids
boolkids = dj.hasChildNodes()
console.log(boolkids)
if (kid3 != []) {
console.log(parent + " has a tile in it");
kid2 = document.getElementById(dj).src;

} else {
console.log(parent + " has no tile in it");
kid2 = "0";
}

image = kid2.toString().substring(60);
console.log(kid2);
} */



function tableCreate(size){
    window.value = size;
    var body = document.body,
    tbl  = document.createElement('table');
    tbl.setAttribute('align', 'center');
    for(var i = 0; i < size; i++){
        var tr = tbl.insertRow();
        for(var j = 0; j < size; j++){
                var td = tr.insertCell();
                td.appendChild(document.createElement("div"));
                td.className = "div1";
                var position = i*size + j + 1;
                td.id = "B" + position;
                td.setAttribute('draggable', true);
		td.addEventListener("drop", function(event){drop(event)});
                td.addEventListener("dragover", function(event){allowDrop(event)});
                td.addEventListener("dragstart", function(event){dragBox(event)});
        }
    }
    document.getElementById("tableau").children[0].remove();
    document.getElementById("tableau").appendChild(tbl) ;
}


/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown menu if the user clicks outside of it
window.onclick = function(event) {
  if (!event.target.matches('.dropbtn')) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains('show')) {
        openDropdown.classList.remove('show');
      }
    }
  }
}
