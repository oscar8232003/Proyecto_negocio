	$(function () {
        $.scrollUp({
            animation: 'fade',
            activeOverlay: false,
            scrollImg: {
            active: true,
            type: 'background',
            src: 'img/top.png'}
            });
    });
    $('#scrollUpTheme').attr('href', 'css/estilos.css');
    $('.image-switch').addClass('active');

    AOS.init();


    $(window).on('load', function () {
      $(".loader").fadeOut("slow");});