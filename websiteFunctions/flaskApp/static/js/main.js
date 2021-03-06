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
    s.setAttribute('oncontextmenu', "rightClickRotate(event);return false;");
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


/* changes a tile in the mosaic to the tile that corresponds to a 90 degree clockwise rotation */
function rightClickRotate(ev){
  var currentTile = ev.target.src.slice(-6,-4);
  if (currentTile == "_1"){
    var newTile = "drag4";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "_2"){
    var newTile = "drag1";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "_3"){
    var newTile = "drag2";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "_4"){
    var newTile = "drag3";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "_5"){
    var newTile = "drag6";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "_6"){
    var newTile = "drag5";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "_7"){
    var newTile = "drag8";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "_8"){
    var newTile = "drag7";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "_9"){
    var newTile = "drag10";
    ev.target.src = document.getElementById(newTile).src;
  } else if (currentTile == "10"){
    var newTile = "drag9";
    ev.target.src = document.getElementById(newTile).src;
  }
  /* the next section redefines the flaskVector */
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
    //console.log(kid)
    if (haskids == 2) {
      var tilesource = document.getElementById(parent).children[1].src.toString();
      var tile = tilesource.split("_").pop();
      tile = tile.substring(0, tile.length - 4);
      tilearray.push(tile)
    } else {
      tile = "0"
      tilearray.push(tile)
    }
  }
  finalarray = tilearray.toString();
  document.getElementById("flaskVector").value = finalarray;

  return false;
}


function setOptions(selected1, selected2) {
  var val1 = selected1 || document.getElementById("sel1").value;
  var val2 = selected2 || document.getElementById("sel2").value || 'nullVal';
  var selbox = document.getElementById("sel2");
  selbox.options.length = 0;
  if (val1 == "Crossings") {
  option1 = document.createElement("option");
  option1.text = "Minimize mosaic";
  option1.value = "Mosaic";
  if (val2 != val1 && val2 == option1.value){
    option1.setAttribute('selected', 'selected');
  }
  option2 = document.createElement("option");
  option2.text = "Minimize tiles";
  option2.value = "TileNum";
  if (val2 != val1 && val2 == option2.value){
    option2.setAttribute('selected', 'selected');
  }
  selbox.add(option1);
  selbox.add(option2);
  }
  else if (val1 == "Mosaic") {
  option1 = document.createElement("option");
  option1.text = "Minimize crossings";
  option1.value = "Crossings";
  if (val2 != val1 && val2 == option1.value){
    option1.setAttribute('selected', 'selected');
  }
  option2 = document.createElement("option");
  option2.text = "Minimize tiles";
  option2.value = "TileNum";
  if (val2 != val1 && val2 == option2.value){
    option2.setAttribute('selected', 'selected');
  }
  selbox.add(option1);
  selbox.add(option2);
  }
  else if (val1 == "TileNum") {
  option1 = document.createElement("option");
  option1.text = "Minimize crossings";
  option1.value = "Crossings";
  if (val2 != val1 && val2 == option1.value){
    option1.setAttribute('selected', 'selected');
  }
  option2 = document.createElement("option");
  option2.text = "Minimize mosaic";
  option2.value = "Mosaic";
  if (val2 != val1 && val2 == option2.value){
    option2.setAttribute('selected', 'selected');
  }
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
                     /* rotate the tile when right-clicked */
                     img.setAttribute('oncontextmenu', "rightClickRotate(event);return false;");
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
/* clears the current mosaic */
  var matrix = document.getElementById("flaskVector").value.replace(/ /g,'');
/* count the number of commas in the matrix, add one and take square root to get size of mosaic*/
  var mosaicSize = ((matrix.match(/,/g) || []).length + 1) ** .5;
  if (mosaicSize != 1){
    tableCreate(mosaicSize, '0');
    document.getElementById("flaskVector").value = '0';

    /* remove the results table and name of knot */
    var table = document.getElementById("resultsTable");
    var ans = document.getElementById("ans");
    if (table != null){
      table.style.display = "none";
    }
    if (ans != null){
      ans.style.display = "none";
    }
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

// The following is from w3schools.com and sets up the autocomplete functionality of the knot search, with minor edits

function autocomplete(inp, arr) {
  /*the autocomplete function takes two arguments,
  the text field element and an array of possible autocompleted values:*/
  var currentFocus;
  /*execute a function when someone writes in the text field:*/
  inp.addEventListener("input", function(e) {
      var a, b, i, val = this.value;
      /*close any already open lists of autocompleted values*/
      closeAllLists();
      if (!val) { return false;}
      currentFocus = -1;
      /*create a DIV element that will contain the items (values):*/
      a = document.createElement("DIV");
      a.setAttribute("id", this.id + "autocomplete-list");
      a.setAttribute("class", "autocomplete-items");
      /*append the DIV element as a child of the autocomplete container:*/
      this.parentNode.appendChild(a);
      /*set up the max number of autocomplete suggestions*/
      var count = 0;
      var stopAt = 5;
      /*for each item in the array...*/
      for (i = 0; i < arr.length; i++) {
        /*check if the item starts with the same letters as the text field value:*/
        if (arr[i].substr(0, val.length).toUpperCase() == val.toUpperCase()) {
          count = count + 1;
          if (count > stopAt){break}
          /*create a DIV element for each matching element:*/
          b = document.createElement("DIV");
          /*make the matching letters bold:*/
          b.innerHTML = "<strong>" + arr[i].substr(0, val.length) + "</strong>";
          b.innerHTML += arr[i].substr(val.length);
          /*insert a input field that will hold the current array item's value:*/
          b.innerHTML += "<input type='hidden' value='" + arr[i] + "'>";
          /*execute a function when someone clicks on the item value (DIV element):*/
              b.addEventListener("click", function(e) {
              /*insert the value for the autocomplete text field:*/
              inp.value = this.getElementsByTagName("input")[0].value;
              /*close the list of autocompleted values,
              (or any other open lists of autocompleted values:*/
              closeAllLists();
              /*un-select the item*/
              currentFocus = -1;
          });
          a.appendChild(b);
        }
      }
  });
  /*execute a function presses a key on the keyboard:*/
  inp.addEventListener("keydown", function(e) {
      var x = document.getElementById(this.id + "autocomplete-list");
      if (x) x = x.getElementsByTagName("div");
      if (e.keyCode == 40) {
        /*If the arrow DOWN key is pressed,
        increase the currentFocus variable:*/
        currentFocus++;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 38) { //up
        /*If the arrow UP key is pressed,
        decrease the currentFocus variable:*/
        currentFocus--;
        /*and and make the current item more visible:*/
        addActive(x);
      } else if (e.keyCode == 13) {
        /*If the ENTER key is pressed and an item is highlighted, prevent the form from being submitted,*/
        if (currentFocus > -1) {
          e.preventDefault();
          /*and simulate a click on the "active" item:*/
          if (x) x[currentFocus].click();
        }
      }
  });
  function addActive(x) {
    /*a function to classify an item as "active":*/
    if (!x) return false;
    /*start by removing the "active" class on all items:*/
    removeActive(x);
    if (currentFocus >= x.length) currentFocus = 0;
    if (currentFocus < 0) currentFocus = (x.length - 1);
    /*add class "autocomplete-active":*/
    x[currentFocus].classList.add("autocomplete-active");
  }
  function removeActive(x) {
    /*a function to remove the "active" class from all autocomplete items:*/
    for (var i = 0; i < x.length; i++) {
      x[i].classList.remove("autocomplete-active");
    }
  }
  function closeAllLists(elmnt) {
    /*close all autocomplete lists in the document,
    except the one passed as an argument:*/
    var x = document.getElementsByClassName("autocomplete-items");
    for (var i = 0; i < x.length; i++) {
      if (elmnt != x[i] && elmnt != inp) {
      x[i].parentNode.removeChild(x[i]);
    }
  }
}
/*execute a function when someone clicks in the document:*/
document.addEventListener("click", function (e) {
    closeAllLists(e.target);
});
}


