$(document).ready(function(){
    $("#kotteri").click(function(){
        $("#kotteri_popup").removeClass("invisible");
        $("#kotteri_popup").dialog({
            modal: true,
            // buttons: {
            //     Add: function() {
            //         $( this ).dialog( "close" );
            //     }
            // }
        });
    });
    $("#mala_kotteri").click(function(){
        $("#mala_kotteri_popup").removeClass("invisible");
        $( "#mala_kotteri_popup" ).dialog({
            modal: true,
        });
    });
    $("#shio").click(function(){
        $("#shio_popup").removeClass("invisible");
        $( "#shio_popup" ).dialog({
            modal: true,
        });
    });
    $("#shoyu").click(function(){
        $("#shoyu_popup").removeClass("invisible");
        $( "#shoyu_popup" ).dialog({
            modal: true,
        });
    });
    $("#spicy_vegetarian").click(function(){
        $("#spicy_vegetarian_popup").removeClass("invisible");
        $( "#spicy_vegetarian_popup" ).dialog({
            modal: true,
        });
    });
    $("#vegetarian_miso").click(function(){
        $("#vegetarian_miso_popup").removeClass("invisible");
        $( "#vegetarian_miso_popup" ).dialog({
            modal: true,
        });
    });
    $("#shanghai").click(function(){
        $("#shanghai_popup").removeClass("invisible");
        $( "#shanghai_popup" ).dialog({
            modal: true,
        });
    });
    $("#ayamgoreng").click(function(){
        $("#ayamgoreng_popup").removeClass("invisible");
        $( "#ayamgoreng_popup" ).dialog({
            modal: true,
        });
    });
    $("#chicken_sandwich").click(function(){
        $("#chicken_sandwich_popup").removeClass("invisible");
        $( "#chicken_sandwich_popup" ).dialog({
            modal: true,
        });
    });
});
