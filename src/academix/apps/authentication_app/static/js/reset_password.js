// CONSTS
const email_input = document.getElementById('email-input');
const reset_button = document.getElementById('reset-button');

const icon_mail_error = document.getElementById('icon-email-error');
const block_email = document.getElementById('block-email');
const block_send_main_spinner = document.getElementById('block-send-main-spinner');

const block_send_email_success = document.getElementById('block-send-email-success');
const block_send_email_error = document.getElementById('block-send-email-error');

// functions
function check_email(email, callback) {
    let csrfToken = getCookie('csrftoken');
    $.ajax({
        url: 'check_email/',
        type: 'POST',
        data: { email: email },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        },
        success: function (response) {
            callback(response.status === 'success');
        },
        error: function (status) {
            callToast('Ошибка', 3, 'Ошибка в работе сервера. Попробуйте позже');
        }
    });
}

function send_email(email) {
    let csrfToken = getCookie('csrftoken');
    $.ajax({
        url: 'send_mail/',
        type: 'POST',
        data: { email: email },
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrfToken);
            }
        },
        success: function (response) {
            if (response.status === 'success') {
                animate_and_replace_element(block_send_main_spinner, block_send_email_success);
            } else {
                animate_and_replace_element(block_send_main_spinner, block_send_email_error);
                callToast('Ошибка', 3, response.message);
            }
        },
        error: function (status) {
            callToast('Ошибка', 3, 'Ошибка в работе сервера. Попробуйте позже');
        }
    });
}

function reset_password() {
    check_email(email_input.value, function (isExist) {
        if (isExist) {
            animate_and_replace_element(block_email, block_send_main_spinner);
            animate_and_replace_element(reset_button, undefined);
            send_email(email_input.value);
        } else {
            icon_mail_error.classList.remove('d-none');
        }
    });
}