// CONSTS
const username_input = document.getElementById('username-input');
const password_input = document.getElementById('password-input');
const login_button = document.getElementById('login-button');

const icon_login_error = document.getElementById('icon-login-error');
const icon_password_error = document.getElementById('icon-password-error');

let first_flag_for_button = false;
let second_flag_for_button = false;

// EVENT INPUT
username_input.addEventListener('input', () => {
    check_login(username_input.value, function() {
        update_button_state();
    });
});

password_input.addEventListener('input', () => {
    check_password(username_input.value, password_input.value, function() {
        update_button_state();
    });
});

// FUNCTIONS
function update_button_state() {
    if(first_flag_for_button && second_flag_for_button){
        login_button.disabled = !login_button.disabled;
        return
    }
    login_button.disabled = true;
}

function check_login(username, callback) {
    let crsf_token = getCookie('csrftoken');
    $.ajax({
        url: 'check_login/',
        type: 'POST',
        data: { username: username },
        beforeSend: function(xhr, settings){
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
                xhr.setRequestHeader("X-CSRFToken", crsf_token); 
            }
        },
        success: function(response) {
            if (response.status === 'success') {
                first_flag_for_button = true;
                callback();

                icon_login_error.classList.add('d-none');
            }else{
                first_flag_for_button = false;
                callback();

                icon_login_error.classList.remove('d-none');
            }
        },
        error: function(status) {
            callToast('Ошибка в работе сервера. Подробная информация: ' + status);
        }
    });
}

function check_password(username, password, callback) {
    let crsf_token = getCookie('csrftoken');
    $.ajax({
        url: 'check_password/',
        type: 'POST',
        data: { username: username,
                password: password },
        beforeSend: function(xhr, settings){
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
                xhr.setRequestHeader("X-CSRFToken", crsf_token); 
            }
        },
        success: function(response) {
            if (response.status === 'success') {
                second_flag_for_button = true
                callback();

                icon_password_error.classList.add('d-none');
            }else{
                second_flag_for_button = false
                callback();

                icon_password_error.classList.remove('d-none');
            }
        },
        error: function(status) {
            callToast('Ошибка в работе сервера. Подробная информация: ' + status);
        }
    });
}

function authenticate_user(){
    let crsf_token = getCookie('csrftoken');
    $.ajax({
        url: 'auth_user/',
        type: 'POST',
        data: { username: username_input.value, 
                password: password_input.value },
        beforeSend: function(xhr, settings){
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
                xhr.setRequestHeader("X-CSRFToken", crsf_token); 
            }
        },
        success: function(response) {
            window.location.href = response.href;
        },
        error: function(status) {
            callToast('Ошибка', 3, 'Ошибка работы сервера, попробуйте позже');
        }
    });
}

function show_password(){
    const toggle_password = document.querySelector('#toggle-password')

    const type = password_input.getAttribute('type') === 'password' ? 'text' : 'password';
    password_input.setAttribute('type', type);
}