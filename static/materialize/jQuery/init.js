(function($){
    $(function(){
        $(".button-collapse").sideNav();
        $('.collapsible').collapsible();
        $('select').material_select();
        $('.scrollspy').scrollspy();
        $('ul.tabs').tabs({
            swipeable: true,
            responsiveTreshold: 1996
        });
        $('.datepicker').pickadate();
    }); // end of document ready
})(jQuery); // end of jQuery name space