// // $.getJSON('http://localhost:8000/getData/' + x +'/', function (serverdata) { 
// //     console.log('function ran')})

// // $.getJSON('http://localhost:8000/getData/' + x +'/');

// function load_video(selected_tv){
//     tv = document.getElementById('tv_video');
//     player = document.getElementById('player');
//     player.src = '../../media/videos/' + selected_tv + '.mp4';
//     tv.load();
//     console.log('load video ran');
// }

// function previous(){
//     window.location.href = "../accounts/login/";
// }

$(document).ready(function() {
    console.log("running jssss");
    // $.ajax({
    //     // url: '10.30.126.35',
    //     url: '/localhost:8000',
    //     type: 'get', // This is the default though, you don't actually need to always mention it
    //     success: function(data) {
    //         console.log(data);
    //     },
    //     failure: function(data) { 
    //         console.log('Got an error dude');
    //     }
    // });

    var i = document.getElementById("player");
    console.log(i);

    // go full-screen
    if (i.requestFullscreen) {
        i.requestFullscreen();
    } else if (i.webkitRequestFullscreen) {
        i.webkitRequestFullscreen();
    } else if (i.mozRequestFullScreen) {
        i.mozRequestFullScreen();
    } else if (i.msRequestFullscreen) {
        i.msRequestFullscreen();
    }


});
// $(document).ready(function() {
//     $.ajax({
//         method: 'GET',
//         url: 'http://10.30.122.76:8000',
//         data: {'yourJavaScriptArrayKey': yourJavaScriptArray},
//         success: function (data) {
//              //this gets called when server returns an OK response
//              alert("it worked!");
//         },
//         error: function (data) {
//              alert("it didnt work");
//         }
//     });
// });
