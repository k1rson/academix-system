// CONSTS
const username_input = document.getElementById('username-input');
const password_input = document.getElementById('password-input');
const login_button = document.getElementById('login-button');

const icon_login_error = document.getElementById('icon-login-error');
const icon_password_error = document.getElementById('icon-password-error');

const auth_block_element = document.getElementById('auth-block');
const otp_block_element = document.getElementById('otp-block');

let first_flag_for_button = false;
let second_flag_for_button = false;

// DEFAULT
login_button.disabled = true;

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

function send_opt_code(){
    let button = $('#login-button')
    let spinner = button.find(".spinner-border");
    let button_text = button.find("#button-text");

    button.prop("disabled", true);
    spinner.show();
    button_text.text("Отправка кода на почту");

    let crsf_token = getCookie('csrftoken');
    $.ajax({
        url: 'auth_user/send_opt_code',
        type: 'POST',
        data: { username: username_input.value },
        beforeSend: function(xhr, settings){
            if (!csrfSafeMethod(settings.type) && !this.crossDomain){
                xhr.setRequestHeader("X-CSRFToken", crsf_token); 
            }
        },
        success: function(response) {
            if (response.status === 'success') {
                animate_and_replace_element(auth_block_element, otp_block_element)
            }else{
               callToast('Ошибка', 3, response.message)
            }
        },
        error: function(status) {
            callToast('Ошибка', 3, 'Ошибка работы сервера, попробуйте позже');
        }
    });
}

function check_login(username, callback) {
    let crsf_token = getCookie('csrftoken');
    $.ajax({
        url: 'auth_user/check_otp_code',
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

// other functions
function handle_input_otp(input) {
    var value = input.value.replace(/\D/g, '');
  
    if (value.length > 1) {
      value = value.charAt(0);
    }
  
    input.value = value;
  
    var next_input = input.nextElementSibling;
    if (next_input !== null && value !== '') {
      next_input.focus();
    }
  }

function show_password(){
    const toggle_password = document.querySelector('#toggle-password')

    const type = password_input.getAttribute('type') === 'password' ? 'text' : 'password';
    password_input.setAttribute('type', type);
}