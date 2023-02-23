function goBack() {
    window.history.back();
  }
  
function setUpEvents() { 
    let content = document.querySelector(".dropdown");
    let button = document.getElementById("button");

    button.addEventListener("click", function() { 
        content.classList.toggle("active");
    })
}

window.onload = function(){ 
    setUpEvents();
}