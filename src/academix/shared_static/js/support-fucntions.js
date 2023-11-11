// initalization tooltips
var tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
var tooltipList = tooltipTriggerList.map(function (tooltipTriggerEl) {
    return new bootstrap.Tooltip(tooltipTriggerEl);
});

// functions for cookie-crsf
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

// fucntion for toast
function callToast(type_toast_text, type_icon_number, message){
    let toast_live_object = document.getElementById('live-toast')

    let toast_type = document.getElementById('toast-type')
    let toast_content = document.getElementById('toast-content')
    let toast_icon = document.getElementById('toast-icon')

    let icon_path;
    switch (type_icon_number) {
        case 1:
            icon_path = success_icon
            break;
        case 2:
            icon_path = warning_icon
            break;
        case 3:
            icon_path = error_icon
            break;
    }

    toast_type.innerText = type_toast_text
    toast_content.innerText = message
    toast_icon.src = icon_path

    let toast = new bootstrap.Toast(toast_live_object)
    toast.show()
}


// functions for replacing elements
function animate_and_replace_element(element, targetElement) {
    element.classList.add('animated-remove');
    element.addEventListener('animationend', function () {
        remove_element(element);

        if (targetElement) {
            targetElement.classList.remove('d-none');
            targetElement.classList.add('animated-create');
        }
    });
}

function remove_element(element) {
    if (element) {
        element.remove();
    }
}