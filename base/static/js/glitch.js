document.addEventListener("DOMContentLoaded", function () {
  var carousel = document.getElementById("carouselExampleCaptions");

  carousel.addEventListener("slid.bs.carousel", function (event) {
    var activeItem = event.relatedTarget;
    activeItem.classList.add("glitch");

    // remove a classe depois da animação
    setTimeout(function () {
      activeItem.classList.remove("glitch");
    }, 400);
  });
});


