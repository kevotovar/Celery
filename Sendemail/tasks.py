from celery.decorators import task
from celery.utils.log import get_task_logger
from django.core.mail import send_mail

logger = get_task_logger(__name__)

@task(name='send_email')
def send_email_celery(email,mensaje):
    send_mail(
        "Email de prueba",#Asunto
        mensaje,#Mensaje
        'kevotovar14@gmail.com',#quien envia
        [email]#para
    )
    logger.info('sent email')