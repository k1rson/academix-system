import secrets
import string

from django.contrib.auth.hashers import make_password

from ...main_app.models import CustomUser

from ...mail_client_app.smtp_utils.smtp_client import SMTPServer
from ...mail_client_app.service.template_generator import TemplateGenerator

def check_user_exists(attribute: str, value: str) -> CustomUser:
    """
    Проверяет существование пользователя по указанному атрибуту.

    :param attribute: Атрибут для поиска пользователя ('username', 'email' или 'id').
    :param value: Значение атрибута.
    :return: Объект CustomUser, если пользователь существует, иначе None.
    """

    try: 
        if attribute == 'username':
            user = CustomUser.objects.get(username=value)
        elif attribute == 'email':
            user = CustomUser.objects.get(email=value)
        elif attribute == 'id':
            user = CustomUser.objects.get(id=value)
        else:
            user = None

        return user
    except CustomUser.DoesNotExist: 
        return None
    except CustomUser.MultipleObjectsReturned:
        return None
    
def check_user_password(user: CustomUser, password: str) -> bool: 
    """
    Проверяет корректность пароля от учетной записи пользователя

    :param user: Объект типа CustomUser
    :param password: Строка с паролем от учетной записи.
    :return: Тип boolean=True, если пароль корректный, иначе boolean=False
    """
    return user.check_password(password)

def login_user_in_system(user: CustomUser) -> str: 
    """
    Авторизовывает пользователя в системе

    :param user: Объект типа CustomUser
    :return: Тип string, возвращает строку с URL, указывающий на рабочее пространство пользователя (student_workspace or teacher_workspace)
    """
    if user.groups.filter(name='Student').exists():
        return '/std_workspace/'
    elif user.groups.filter(name='Teacher').exists(): 
        return '/tch_workspace/'
    
    return '/adm_workspace/'

def reset_password(user: CustomUser) -> bool:
    """
    Сбрасывает пароль от учетной записи пользователя

    :param user: Объект типа CustomUser
    :param email: Строка с электронной почтой пользователя
    :return: Тип bool, возвращает bool, характеризующее статус c6poca пароля
    """
    try:
        new_password = generate_random_password(12)
        user.password = make_password(new_password)
        user.save()

        user_data = {
            'username': user.username,
            'new_password': new_password, 
            'email': user.email
        }

        send_email_status = send_reset_password_email(user_data)
        if not send_email_status:
            return False

        return True        

    except Exception:
        return False

def send_reset_password_email(user_data: dict) -> bool:
    """
    Отправляет новый пароль от учетной записи на электронную почту

    :param user_data: Словарь, содержащий всю информацию по пользователю и его новый пароль
    :return: Тип bool, возвращает bool, характеризующее статус отправки письма
    """
    smtp_server = SMTPServer()
    template_generator = TemplateGenerator('reset_password_email.html')

    context = {
        'username': user_data['username'], 
        'new_password': user_data['new_password']
    }

    html_content = template_generator.generate_html_content(context)
    send_status = smtp_server.send_message(f'Доброго времени суток, {user_data["username"]}!. Восстановление доступа к учетной записи', '', user_data['email'], html_content)

    if not send_status: 
        return False
    
    return True 

def send_otp_code_mail(email: str) -> bool:
    """
    Отправляет OTP (One-Time-Password) код на почту, привязанную к электронной почте

    :param email: Строка, включающая в себя электронную почту пользователя
    :return: Тип bool, возвращает bool, характеризующее статус отправки OPT кода
    """
    opt_code = generate_otp(4, 1)

    smtp_server = SMTPServer()
    templater_generator = TemplateGenerator('otp_code_email.html')

    context = {
        'otp_code': opt_code 
    }

    html_content = templater_generator.generate_html_content(context)
    send_status = smtp_server.send_message(f'Одноразовый код для входа в систему (OTP Auth - Academix)', '', email, html_content)

    if not send_status: 
        return False
    
    return True, opt_code

def generate_random_password(length: int):
    """
    Генерирует случайный пароль указанной длины

    :param length: Длина пароля
    :return: Тип str, возвращает строку co сгенерированным паролем
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return f''.join(secrets.choice(alphabet) for _ in range(length))

def generate_otp(length: int, otp_type: int) -> str:
    """
    Генерирует одноразовый пароль (One-Time-Password)

    :param length: Количество символов
    :param otp_type: Тип генерации (1 -> числа, 2 -> символы)

    :return: Тип str, возвращает строку, включающая в себя сгенерированный OTP
    """
    if otp_type == 1:
        alphabet = string.digits  
    elif otp_type == 2:
        alphabet = string.ascii_letters + string.punctuation  
    else:
        raise ValueError("Неподдерживаемый тип генерации")

    otp = ''.join(secrets.choice(alphabet) for _ in range(length))
    return otp