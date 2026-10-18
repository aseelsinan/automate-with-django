from django.contrib import messages
from django.shortcuts import redirect, render

from uploades.models import Upload

from .tasks import import_data_task
from .utils import check_csv_errors, get_all_custom_models


def data_entry(request):
    if request.method=='POST':
        file_path=request.FILES.get('file_path')
        model_name=request.POST.get('model-name')

        #store this file inside upload model
        upload = Upload.objects.create(file=file_path,model_name=model_name)
        
        #construct full path
        path=upload.file.path
       
        # Check CSV Erorrs 
        try:
            check_csv_errors(path,model_name)
        except Exception as e:  # noqa: BLE001
            messages.error (request,str(e))   
            upload.delete()
            return redirect('import-data')
         
        # Handle import data task 
        import_data_task.delay(path,model_name)
        messages.success(request,'your data is being imported , you will notified once it is done')
        return redirect('import-data')
        
    else:
        all_models=get_all_custom_models()
        context ={'all_models':all_models}
        
    return render(request,'data-entry.html',context)


def data_export(request):
    return render(request,'data-export.html')