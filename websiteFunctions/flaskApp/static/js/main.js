function allowDrop(ev) {
  ev.preventDefault();
}

window.onload = function() {
  var matrixDiv = document.getElementById("flaskVector").value;
  if(matrixDiv != "0"){
    matrix = matrixDiv.split(',').map(function(item) {
      return parseInt(item, 10);
    });
    size = Math.sqrt(matrix.length)
    console.log(matrix)
    console.log(matrix.length)
  } else{
    size = 4
  }
  tableCreate(size);
};

/*document.ready(function(){
  var sizeDropdown = document.getElementById(mosaicSize);
  sizeDropdown.on('change', function(){
    console.log(sizeDropdown.value)
    if sizeDropdown.value == '6'{
      document.getElementById(6x6layouts).show():
    }
    else{
      document.getElementById(6x6layouts).hide():
    }
  }
}*/

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
    //ev.dataTransfer.clearData();
    delete s
    delete name
    delete data

  var size = window.value;
  if (size == null) {
     size = 3
  }
  //console.log(size)
  var lim = size*size;
  //console.log(lim)
  var j;
  var tilearray = Array(0);
  for (j = 1; j < lim+1; j++) {
    parent = "B" + j;
    var kid;
    kid = document.getElementById(parent).children;
    var haskids
    haskids = kid.length;
    //console.log(kid)
    if (haskids == 2) {
      var tilesource = document.getElementById(parent).children[1].src.toString();
      //var tilesource = "horse_123456";
      var tile = tilesource.split("_").pop();
      tile = tile.substring(0, tile.length - 4);
      tilearray.push(tile)
    } else {
      tile = "0"
      tilearray.push(tile)
    }
  }
  //console.log(tilearray);
  finalarray = tilearray.toString();
  document.getElementById("flaskVector").value = finalarray;
  //console.log("the value of the flask vector is:")
  console.log(document.getElementById("flaskVector").value)
  //console.log(finalarray)
  //document.getElementById("results").innerHTML = "The array for this knot is " + finalarray + "." ;
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
    ev.target.appendChild(s);
    //ev.dataTransfer.clearData();
    delete s
    delete name
    delete data
  var size = window.value;
  if (size == null) {
     size = 3
  }
  var lim = size*size;
  var j;
  var tilearray = Array(0);
  for (j = 1; j < lim+1; j++) {
    parent = "B" + j;
    var kid;
    kid = document.getElementById(parent).children;
    var haskids
    haskids = kid.length;
    if (haskids == 2) {
      var tilesource = document.getElementById(parent).children[1].src.toString();
      //var tilesource = "horse_123456";
      var tile = tilesource.split("_").pop();
      tile = tile.substring(0, tile.length - 4);
      tilearray.push(tile)
    } else {
      tile = "0"
      tilearray.push(tile)
    }
  }
  //console.log(tilearray);
  finalarray = tilearray.toString();
  document.getElementById("flaskVector").value = finalarray;
  //console.log("the value of the flask vector is:")
  console.log(document.getElementById("flaskVector").value)
  //console.log(finalarray)
  //document.getElementById("results").innerHTML = "The array for this knot is " + finalarray + "." ;
    }




function setOptions() {
  var val = document.getElementById("sel1").value;
  var selbox = document.getElementById("sel2");
  selbox.options.length = 0;
  if (val == "Crossings") {
  option1 = document.createElement("option");
  option1.text = "Minimize mosaic size";
  option1.value = "Mosaic";
  option2 = document.createElement("option");
  option2.text = "Minimize number of tiles";
  option2.value = "TileNum";
  selbox.add(option1);
  selbox.add(option2);
  }
  else if (val == "Mosaic") {
  option1 = document.createElement("option");
  option1.text = "Minimize number of crossings";
  option1.value = "Crossings";
  option2 = document.createElement("option");
  option2.text = "Minimize number of tiles";
  option2.value = "TileNum";
  selbox.add(option1);
  selbox.add(option2);
  }
  else if (val == "TileNum") {
  option1 = document.createElement("option");
  option1.text = "Minimize number of crossings";
  option1.value = "Crossings";
  option2 = document.createElement("option");
  option2.text = "Minimize mosiac size";
  option2.value = "Mosaic";
  selbox.add(option1);
  selbox.add(option2);
  }
}



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






function tableCreate(size, mat){
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
                td.setAttribute('draggable', false);
		td.addEventListener("drop", function(event){drop(event)});
                td.addEventListener("dragover", function(event){allowDrop(event)});
                td.addEventListener("dragstart", function(event){dragBox(event)});
                //matrix = matrix || document.getElementById("flaskVector").value;
                //console.log(matrix)
                //console.log(document.getElementById("flaskVector").value)
                //var imgID = "drag" + matrix[position - 1];
                var matrixDiv = mat || document.getElementById("flaskVector").value;
                //console.log(matrixDiv)
                if(typeof(matrixDiv) != 'Undefined' && matrixDiv != null && matrixDiv != "0"){
                   document.getElementById("flaskVector").value = matrixDiv;
                   //matrix = JSON.parse(matrixDiv.dataset.matrix);
                   matrix = matrixDiv.split(',').map(function(item) {
                     return parseInt(item, 10);
                   });
                   //console.log(matrix)
                   var imgID = "drag" + matrix[position - 1];
                   if ( imgID != "drag0"){
                     //console.log(matrix[position])
                     var img = document.getElementById(imgID).cloneNode(true);
                     img.id = "dragged" + position + 1000;// This is so it doesn't conflict with other ids
                     td.appendChild(img);
                   }
                }
        }
    }
    document.getElementById("tableau").children[0].remove();
    document.getElementById("tableau").appendChild(tbl) ;
    //document.getElementById("flaskVector").value = "0,0,0";
}



function tableClear(){
  var matrix = document.getElementById("flaskVector").value.replace(/ /g,'');
// count the number of commas in the matrix, add one and take square root to get size of mosaic
  var mosaicSize = ((matrix.match(/,/g) || []).length + 1) ** .5;
  console.log(matrix)
  if (mosaicSize != 1){
    tableCreate(mosaicSize, '0');
    document.getElementById("flaskVector").value = '0';
  }
}
/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}
function dropdownFunc2() {
  document.getElementById("chooseKnot").classList.toggle("show");
}
/* When clicking the dropdown select for mosaic size, this calls the createTable function with appropriate size*/
function changeFunc() {
  var selectBox = document.getElementById("selectBox");
  var selectedValue = selectBox.options[selectBox.selectedIndex].value;
  tableCreate(selectedValue, '0');
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
