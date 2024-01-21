  // Obtiene el carousel
  const myCarousel = document.getElementById('carouselExampleIndicators');
  
  // Inicia el carousel
  const carousel = new bootstrap.Carousel(myCarousel);

  // Cambia al siguiente slide cada 5 segundos
  setInterval(function() {
    carousel.next();
  }, 3000);