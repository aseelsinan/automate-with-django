from django.core.management.base import BaseCommand
from data_entry.models import Student
import csv
# Proposed Command = Python manage.py import_data file_path
class Command(BaseCommand):
    help='import data from csv file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path',type=str,help='File to CSV Path')
    def handle(self,*args, **kwargs):
        file_path=kwargs['file_path']
        with open(file_path,'r',encoding='utf-8') as file:
            reader=csv.DictReader(file)
            for row in reader:
                Student.objects.create(**row)
                print(row)
            self.stdout.write(self.style.SUCCESS("Data imported successfully")) 
                
