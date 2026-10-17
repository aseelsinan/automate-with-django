import csv

from django.core.management.base import BaseCommand

from data_entry.utils import check_csv_errors

# Proposed Command = Python manage.py import_data file_path model_name


class Command(BaseCommand):
    help = "insert specific CSV to Specific Model"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str, help="Enter CSV File Path")
        parser.add_argument("model_name", type=str, help="Enter Model Name")

    def handle(self, *args, **kwargs):
        file_path = kwargs["file_path"]
        model_name = kwargs["model_name"].capitalize()

        model = check_csv_errors(file_path, model_name)

        with open(file_path, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                model.objects.create(**row)
                print(row)
                self.stdout.write(self.style.SUCCESS("File added Successfully"))
