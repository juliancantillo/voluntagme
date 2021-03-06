/* Project specific Javascript goes here. */

global.jQuery = require('../vendor/jquery/dist/jquery');
var $ = global.jQuery;
var bootstrap = require('../vendor/bootstrap/dist/js/npm');
var bootstrap = require('./lib/cbpAnimatedHeader');

$(document).ready(function () {

    // Highlight the top nav as scrolling
    $('body').scrollspy({
        target: '.navbar-fixed-top',
        offset: 80
    });

    $('#inSlider').carousel();

    // Page scrolling feature
    $('a.page-scroll').bind('click', function(event) {
        var link = $(this);
        $('html, body').stop().animate({
            scrollTop: $(link.attr('href')).offset().top - 70
        }, 500);
        event.preventDefault();
    });

});