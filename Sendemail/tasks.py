from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
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

@periodic_task(run_every=crontab(), name="send_remainder")
def send_remainder_celery():
    send_mail(
        "Email remainder",
        "Pagame prro",
        "kevintovar@esimez.mx",
        ["kevotovar14@gmail.com"]
    )