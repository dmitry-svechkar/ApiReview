import hashlib

from api_yamdb.settings import SECRET_KEY
from django.core.mail import send_mail


def generate_activation_code(username: str) -> str:
    code_bytes = (SECRET_KEY + username).encode('utf-8')
    hash_code = hashlib.sha256(code_bytes)
    return hash_code.hexdigest()


def send_confirmation_code(username, recipient):
    confirmation_code = generate_activation_code(username)
    send_mail(
        subject='Register',
        message='Успешная регистрация.'
                f'Ваш код подтверждения {confirmation_code=}',
        from_email='yamdb@yamdb.ru',
        recipient_list=[recipient],
        fail_silently=True
    )
