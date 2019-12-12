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