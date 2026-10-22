from ckeditor.fields import RichTextField
from django.db import models


class List(models.Model):
    email_list = models.CharField(max_length=25)

    def __str__(self):
        return self.email_list


class Subscriber(models.Model):
    email_list=models.ForeignKey(List,null=True, related_name='list_email' , on_delete=models.SET_NULL)
    email_address=models.EmailField( max_length=75)

    def __str__(self):
        return self.email_address



class Email(models.Model):
    email_list=models.ForeignKey(List, related_name='email_list_send', null=True, on_delete=models.SET_NULL)
    subject=models.CharField( max_length=100)
    body=RichTextField()
    attachment=models.FileField( upload_to='email/attachments/', max_length=100,blank=True,null=True)
    sent_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.subject