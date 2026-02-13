function showGif() {
    document.getElementById("kingGif").style.display = "block";
}


let typed = "";
let secret = "clash";

document.addEventListener("keydown", function (event) {
  typed += event.key.toLowerCase();

  if (typed.includes(secret)) {
    window.location.href = "/secret";
  }
});