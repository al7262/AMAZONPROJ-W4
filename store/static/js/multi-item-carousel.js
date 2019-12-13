// for product 1
$('#carouselExample').on('slide.bs.carousel', function (e) {

    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 6;
    var totalItems = $('.product .carousel-item').length;
    
    if (idx >= totalItems-(itemsPerSlide-1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i=0; i<it; i++) {
            // append slides to end
            if (e.direction=="left") {
                $('.product .carousel-item').eq(i).appendTo('.product .carousel-inner');
            }
            else {
                $('.product .carousel-item').eq(0).appendTo('.product .carousel-inner');
            }
        }
    }
});

// for product 2
$('#carouselExample2').on('slide.bs.carousel', function (e) {

    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 6;
    var totalItems = $('.product2 .carousel-item').length;
    
    if (idx >= totalItems-(itemsPerSlide-1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i=0; i<it; i++) {
            // append slides to end
            if (e.direction=="left") {
                $('.product2 .carousel-item').eq(i).appendTo('.product2 .carousel-inner');
            }
            else {
                $('.product2 .carousel-item').eq(0).appendTo('.product2 .carousel-inner');
            }
        }
    }
});

// for product 3
$('#carouselExample3').on('slide.bs.carousel', function (e) {

    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 6;
    var totalItems = $('.product3 .carousel-item').length;
    
    if (idx >= totalItems-(itemsPerSlide-1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i=0; i<it; i++) {
            // append slides to end
            if (e.direction=="left") {
                $('.product3 .carousel-item').eq(i).appendTo('.product3 .carousel-inner');
            }
            else {
                $('.product3 .carousel-item').eq(0).appendTo('.product3 .carousel-inner');
            }
        }
    }
});

// for product 4
$('#carouselExample4').on('slide.bs.carousel', function (e) {

    var $e = $(e.relatedTarget);
    var idx = $e.index();
    var itemsPerSlide = 6;
    var totalItems = $('.product4 .carousel-item').length;
    
    if (idx >= totalItems-(itemsPerSlide-1)) {
        var it = itemsPerSlide - (totalItems - idx);
        for (var i=0; i<it; i++) {
            // append slides to end
            if (e.direction=="left") {
                $('.product4 .carousel-item').eq(i).appendTo('.product4 .carousel-inner');
            }
            else {
                $('.product4 .carousel-item').eq(0).appendTo('.product4 .carousel-inner');
            }
        }
    }
});