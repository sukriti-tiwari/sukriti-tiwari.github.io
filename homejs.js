$(document).ready(function() {
    $('.owl-carousel').owlCarousel({
        pagination: false,
        loop: true,
        autoplay: true,
        autoplayTimeout: 2000,
        autoplayHoverPause: true,
        responsive: {
            0: {
                items: 1,
                nav: false
            }
        }
    })
});