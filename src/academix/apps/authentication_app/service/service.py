from django.contrib.auth.models import User

def check_user_exists(attribute: str, value: str) -> User:
    """
    Проверяет существование пользователя по указанному атрибуту.

    :param attribute: Атрибут для поиска пользователя ('username', 'email' или 'id').
    :param value: Значение атрибута.
    :return: Объект User, если пользователь существует, иначе None.
    """

    try: 
        if attribute == 'username':
            user = User.objects.get(username=value)
        elif attribute == 'email':
            user = User.objects.get(email=value)
        elif attribute == 'id':
            user = User.objects.get(id=value)
        else:
            user = None

        return user
    except User.DoesNotExist: 
        return None
    
def check_user_password(user: User, password: str) -> bool: 
    """
    Проверяет корректность пароля от учетной записи пользователя

    :param user: Объект типа User
    :param password: Строка с паролем от учетной записи.
    :return: Тип boolean=True, если пароль корректный, иначе boolean=False
    """
    return user.check_password(password)