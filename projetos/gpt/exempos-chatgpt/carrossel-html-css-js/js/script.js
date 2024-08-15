var carousel = document.querySelector('.carousel-items');
var items = carousel.querySelectorAll('.carousel-item');
var currentIndex = 0;
var interval = setInterval(changeSlide, 5000);

function changeSlide() {
  carousel.style.transform = 'translateX(' + (-100 * currentIndex) + '%)';
  currentIndex++;

  if (currentIndex >= items.length) {
    currentIndex = 0;
  }
}
