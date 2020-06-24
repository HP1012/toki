// $(document).ready(function(){
//     $("#btn-on").click(async function(){
//         console.log("Button on click");
//         await eel.click_button("on");
//     });
//     $("#btn-off").click(async function(){
//         console.log("Button off click");
//         await eel.click_button("off");
//     });
//   });
$(document).ready(function(){
// a1: workspace home
var a1;
var Test = {
    settings: {
        btnOn: $("#btn-on"),
        btnOff: $("#btn-off")
    },

    init: function() {
        a1 = this.settings;
        this.bindUIActions();
    },
    bindUIActions: function(){
        a1.btnOn.on("click", async function(){
            $("ol").append("<li> Button on click </li>");
            console.log("Button on click");
            await eel.click_button("on");
        });
        a1.btnOff.on("click", async function(){
            console.log("Button on click");
            $("ol").append("<li> Button on click </li>");
            await eel.click_button("off");
        });
    }
}

// Initial
Test.init();
// console.log("Button on click");
})