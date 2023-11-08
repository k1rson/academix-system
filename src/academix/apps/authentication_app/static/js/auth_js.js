// CONSTS
const username_input = document.getElementById('username-input');
const password_input = document.getElementById('password-input');
const login_button = document.getElementById('login-button');

const icon_login_error = document.getElementById('icon-login-error');
const icon_password_error = document.getElementById('icon-password-error');

// EVENT INPUT
username_input.addEventListener('input', () => {
    check_login(username_input.value, function(is_login_valid) {
        update_button_state(is_login_valid);
    });
});

password_input.addEventListener('input', () => {
    check_password(username_input.value, password_input.value, function(is_password_valid) {
        update_button_state(is_password_valid);
    });
});

// FUNCTIONS
function update_button_state(isButtonEnabled) {
    login_button.disabled = !isButtonEnabled;
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
                callback(true);

                icon_login_error.classList.add('d-none');
            }else{
                callback(false);

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
                callback(true);

                icon_password_error.classList.add('d-none');
            }else{
                callback(false);
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
            console.log('good')
        },
        error: function(status) {
            callToast('Ошибка в работе сервера. Подробная информация: ' + status);
        }
    });
}