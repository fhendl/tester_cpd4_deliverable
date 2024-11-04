document.querySelectorAll('img').forEach(img => {
    console.log("runs")
    img.onerror = function(){
    this.onerror = null;
    this.src = '../js/placeholder-image.jpg';
    this.alt = ""
    };
});