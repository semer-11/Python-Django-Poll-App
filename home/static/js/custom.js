/* HTML document is loaded. DOM is ready.
-------------------------------------------*/
$(function() {


    $('.chart').easyPieChart({
        size: 100,
        barColor: "#36e617",
        scaleLength: 0,
        lineWidth: 15,
        trackColor: "#525151",
        lineCap: "rectangle",
        animate: 4000,
    });
    $('.laravel').easyPieChart({
        size: 100,
        barColor: "orange",
        scaleLength: 0,
        lineWidth: 15,
        trackColor: "#525151",
        lineCap: "rectangle",
        animate: 4000,
    });
    $('.django').easyPieChart({
        size: 100,
        barColor: "red",
        scaleLength: 0,
        lineWidth: 15,
        trackColor: "#525151",
        lineCap: "rectangle",
        animate: 4000,
    });
    /* start typed element */
    //http://stackoverflow.com/questions/24874797/select-div-title-text-and-make-array-with-jquery
    var subElementArray = $.map($('.sub-element'), function(el) { return $(el).text(); });
    $(".element").typed({
        strings: subElementArray,
        typeSpeed: 30,
        contentType: 'html',
        showCursor: false,
        loop: true,
        loopCount: true,
    });
    /* end typed element */

    /* Smooth scroll and Scroll spy (https://github.com/ChrisWojcik/single-page-nav)    
    ---------------------------------------------------------------------------------*/
    $('.templatemo-nav').singlePageNav({
        offset: $(".templatemo-nav").height(),
        filter: ':not(.external)',
        updateHash: false
    });

    /* start navigation top js */
    $(window).scroll(function() {
        if ($(this).scrollTop() > 58) {
            $(".templatemo-nav").addClass("sticky");
        } else {
            $(".templatemo-nav").removeClass("sticky");
        }
    });

    /* Hide mobile menu after clicking on a link
    -----------------------------------------------*/
    $('.navbar-collapse a').click(function() {
        $(".navbar-collapse").collapse('hide');
    });
    /* end navigation top js */

    $('body').bind('touchstart', function() {});

    /* wow
    -----------------*/
    new WOW().init();
});

/* start preloader */
$(window).load(function() {
    $('.preloader').fadeOut(3000); // set duration in brackets   



});
/* end preloader */