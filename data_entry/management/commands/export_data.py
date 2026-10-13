from django.core.management.base import BaseCommand
from data_entry.models import Student
import datetime
import csv
# Proposed Command = Python manage.py export_data 

class Command(BaseCommand):
    help='Export Data from database to CSV '
    def handle(self, *args, **options):
        students=Student.objects.all().order_by('-roll_number')
        print(students)
        
        
        time_stamp=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        file_path=f'exported_students_data_{time_stamp}.csv'
        print(file_path)
        
        with open(file_path,'w',newline='') as file:
            writer=csv.writer(file)
            
            writer.writerow(['roll_number','name','age'])
            
            for student in students:
                writer.writerow([student.roll_number,student.name,student.age])
                # self.stdout.write(f'Student {student.roll_number} added Successfully')
                
            self.stdout.write(self.style.SUCCESS(f'file generated and all students added successfully'))
            