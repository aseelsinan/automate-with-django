from django.shortcuts import render ,redirect
from .utils import get_all_custom_models
from uploades.models import Upload
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages
def data_entry(request):
    if request.method=='POST':
        file_path=request.FILES.get('file_path')
        model_name=request.POST.get('model-name')

        #store this file inside upload model
        upload = Upload.objects.create(file=file_path,model_name=model_name)
        
        #construct full path
        relative_path=upload.file.url
        base_url=settings.BASE_DIR
        path=f'{base_url}{relative_path}'
        print(path)
        
        try:
            call_command('insert_data_specific',path,model_name)
            messages.success(request,'Data imported successfully')
        except Exception as e:
            messages.error(request,str(e))
            
        return redirect('import-data')
    else:
        all_models=get_all_custom_models()
        context ={'all_models':all_models}
        
    return render(request,'data-entry.html',context)