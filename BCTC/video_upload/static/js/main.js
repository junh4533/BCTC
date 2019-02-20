function dropdown_change(){
    console.log("JS running");
    player = document.getElementById('player');
    dropdown =  document.getElementById('selected_tv');
    tv = document.getElementById('tv_video');
    // selected_tv = dropdown.options[selected_tv.selectedIndex].value;
    selected_tv = dropdown.value;
    player.src = 'media/videos/' + selected_tv + '.mp4';
    tv.load();

}


