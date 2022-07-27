/*Source: https://www.w3schools.com/w3css/w3css_tabulators.asp*/

function openSource(evt, sourceName) {
    var i, x , tablinks;
    var x = document.getElementsByClassName("source");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < x.length; i++) {
    tablinks[i].className = tablinks[i].className.replace(" buttonRed", "");
  }
  document.getElementById(sourceName).style.display = "block";
  evt.currentTarget.className += " buttonRed";
}


