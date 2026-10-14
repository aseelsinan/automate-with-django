from django.core.management.base import BaseCommand,CommandError
from django.apps import apps
import csv

from django.db import DataError

# Proposed Command = Python manage.py import_data file_path model_name

class Command(BaseCommand):
    help='insert specific CSV to Specific Model'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str,help='Enter CSV File Path')
        parser.add_argument('model_name',type=str,help='Enter Model Name')

    def handle(self, *args, **kwargs):
        file_path=kwargs['file_path']
        model_name=kwargs['model_name'].capitalize()
        model =None
        for app_config in apps.get_app_configs():
            
            try:
                model=apps.get_model(app_config.label,model_name)
                break
            except LookupError:
                continue
        if not model:
            raise CommandError(f'model {model_name} not found in any app')
        
        # Compare CSV header with 
        # get all the field names of the model   
        model_fields=[field.name for field in model._meta.fields]
        
                
        
        with open(file_path,'r',encoding='utf-8-sig') as file:
            reader =csv.DictReader(file)
            csv_reader=reader.fieldnames
            
            if csv_reader != model_fields:
                raise DataError(f"CSV file dosen't match with the {model_name} table fields")
            for row in reader:
                model.objects.create(**row)
                print(row)
        self.stdout.write(self.style.SUCCESS('File added Successfully'))
            