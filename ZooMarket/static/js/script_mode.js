btn_theme = document.getElementById('btn_theme');

function changeTheme() {
    mode = LocalStorage.getItem('theme');

    if (mode == 'dark') {
        console.log(localStorage.getItem('theme'));
        document.body.classList.remove('dark-mode')
        document.body.classList.add('light-mode')
        localStorage.setItem('theme', 'light');
    } else {
        console.log(localStorage.getItem('theme'));
        document.body.classList.remove('light-mode')
        document.body.classList.add('dark-mode')
        localStorage.setItem('theme', 'dark');
    }
}

document.addEventListener("DOMContentLoaded ", changeTheme);
btn_theme.addEventListener('click', changeTheme);

localStorage.setItem('theme', 'dark');





//document.getElementById('btn_theme').addEventListener('click', function() {
//    const currentTheme = document.body.className;
//
//    if (currentTheme === 'light-mode') {
//        document.body.className = 'dark-mode';
//    } else {
//        document.body.className = 'light-mode';
//    }
//});


