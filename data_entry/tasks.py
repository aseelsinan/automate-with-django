

from django.conf import settings
from django.core.management import call_command

from automate_main.celery import app

from .utils import send_email_notification


@app.task
def sending_email_task():
    mail_subject='this subject'
    message='this is email'
    
    to_email=settings.DEFAULT_TO_EMAIL 
    send_email_notification(mail_subject,message,to_email)

    
   
    return 'email sent successfully'





@app.task
def import_data_task(path, model_name):

    try:
        call_command("insert_data_specific", path, model_name)
    except Exception as e:  # noqa: TRY203
        raise (e)  # noqa: TRY201

    mail_subject='import data completed'
    message='Your data import has been successfully'
        
    to_email=settings.DEFAULT_TO_EMAIL 
    send_email_notification(mail_subject,message,to_email)
    
        
    return "data imported successfully"
