/*Source: https://www.w3schools.com/w3css/w3css_tabulators.asp*/

function openSource(sourceName) {
    var i;
    var x = document.getElementsByClassName("source");
    for (i = 0; i < x.length; i++) {
      x[i].style.display = "none";
    }
    document.getElementById(sourceName).style.display = "block";
  }