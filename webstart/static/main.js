function goBack() {
    window.history.back();
  }
  
function setUpEvents() { 
    let content = document.querySelector(".dropdown");
    let button = document.querySelector(".button-wrapper");
    let svg = document.querySelector(".svg")

    button.addEventListener("click", function() { 
        content.classList.toggle("active");
        svg.classList.toggle("active")
    })
}

window.onload = function(){ 
    setUpEvents();
}