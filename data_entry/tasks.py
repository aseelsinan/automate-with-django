

from django.conf import settings
from django.core.management import call_command

from automate_main.celery import app
from emails.models import Email

from .utils import send_email_notification


@app.task
def send_email_task(email_id, to_emails):
    try:
        email_record = Email.objects.get(id=email_id)
        
        # نتحقق إذا كان هناك مرفق ونأخذ مساره
        attachment_path = None
        if email_record.attachment:
            attachment_path = email_record.attachment.path

        send_email_notification(
            mail_subject=email_record.subject,
            message=email_record.body,
            to_email=to_emails,
            attachment_path=attachment_path
        )
        return 'Email sent successfully via Celery'
    except Email.DoesNotExist:
        return 'Email record not found'



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
