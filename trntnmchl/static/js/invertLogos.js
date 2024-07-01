function invertLogos(invert) {
    var bandcampLogo = document.getElementById("bandcamp");
    var soundcloudLogo = document.getElementById("soundcloud");
    if(invert)  {
        bandcampLogo.style.filter = "invert(1)";
        soundcloudLogo.style.filter = "invert(1)";
    }
    else {
        bandcampLogo.style.filter = "";
        soundcloudLogo.style.filter = "";
    }
}