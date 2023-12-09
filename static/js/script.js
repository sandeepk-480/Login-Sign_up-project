function togglePassword_login() {
    var show_pass = document.querySelector(".show_pass");
    var password1 = document.getElementById('id_password');

    if (show_pass.checked) {
        password1.type = "text";
    } else {
        password1.type = "password";
    }
}


function togglePassword_signup() {
    var show_pass = document.querySelector(".show_pass");
    var password1 = document.getElementById('id_password1');
    var password2 = document.getElementById('id_password2');

    if (show_pass.checked) {
        password1.type = "text";
        password2.type = "text";
    } else {
        password1.type = "password";
        password2.type = "password";
    }
}



setTimeout(() => {
    let dashboard = document.querySelector('.message-js');
    if (dashboard) {
        dashboard.style.display = 'none';
    }
}, 3000);



