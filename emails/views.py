


from django.contrib import messages
from django.shortcuts import redirect, render

from data_entry.tasks import send_email_task

from .forms import EmailForm


def send_email(request):
    if request.method=='POST':
        email_form =EmailForm(request.POST,request.FILES)
        if email_form.is_valid():
            # Export all emails in list
            email=email_form.save()  
            subscribers = email.email_list.list_email.all()
            
            # grouping emails in list
            to_emails = [sub.email_address for sub in subscribers]
            
           
            send_email_task.delay(email.id, to_emails)
            # display success message
            messages.success(request,'Email send successfully')
            return redirect('send-email')
        else:
            messages.error(request,'something worng with this email')
    else:
        email_form=EmailForm()
    return render(request,'send-email.html',{'email_form':email_form})

# 59 03:51