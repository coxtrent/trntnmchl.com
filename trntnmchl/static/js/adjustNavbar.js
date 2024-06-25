function makeNavbarVisible() {
    var navbar = document.querySelector('.navbar');
    navbar.style.transition = 'none';
    navbar.style.opacity = '1';  
}

function makeNavbarTextBlack() {
    var navbar = document.querySelector('.navbar');
    navbar.style.textShadow = '1px 1px 4px white';
    var navbar_a = document.querySelectorAll('.navbar a');
    navbar_a.forEach(function(a) {
        a.style.color = '#00000f';
    });
}