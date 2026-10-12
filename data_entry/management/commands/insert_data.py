from django.core.management.base import BaseCommand
from data_entry import models
# I want to add some data to database using custom command

class Command(BaseCommand):
    help='it will insert data to database '
    
    def handle(self, *args, **options):
        dateset=[
            {'roll_number':1006,'name':'Rodrigo','age':25},
            {'roll_number':1007,'name':'Abadol','age':24},
            {'roll_number':1008,'name':'Sami','age':32},
        ]
        for data in dateset:
            roll_number=data['roll_number']
            existing_data=models.Student.objects.filter(roll_number=roll_number).exists()
            if not existing_data:    
                models.Student.objects.create(roll_number=data['roll_number'] , name=data['name'],age=data['age'])
                self.stdout.write(self.style.SUCCESS('Data inserted Successfully'))
            else:
                self.stdout.write(self.style.WARNING(f'student in {roll_number} exist'))
        