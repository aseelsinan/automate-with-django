from django.core.management.base import BaseCommand ,CommandError
from django.apps import apps
import datetime
import csv
class Command(BaseCommand):
    help='Export Data From Specific Table'
    
    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str,help='Enter Table Name')
        
    def handle(self, *args, **kwargs):
        model_name=kwargs['model_name'].capitalize()
        model=None
        
        for app_config in apps.get_app_configs():
            try:
                model=apps.get_model(app_config.label,model_name)
                break
            except LookupError:
                continue
        
        if not model:
           raise CommandError(f'model {model_name} not found in app')
         
        
        data= model.objects.all()
        
        file_path=f'exported_{model_name}_data_{datetime.datetime.now().strftime('%d%m%Y%H%M%S')}.csv'
        with open(file_path,'w',newline='')as file:
            
            writer =csv.writer(file)
            writer.writerow([field.name  for field in model._meta.fields ])
            for dt in data:
                writer.writerow([field.name for field in model._meta.fields])
            self.stdout.write(self.style.SUCCESS(f'File {file_path} exported successfully'))
            