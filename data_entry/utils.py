import csv

import django.core.mail
from django.apps import apps
from django.conf import settings
from django.core.management import CommandError
from django.db import DataError


def get_all_custom_models():
    default_models = [
        "ContentType",
        "LogEntry",
        "Permission",
        "Group",
        "Session",
        "User",
        "Upload",
    ]
    custom_models = []
    for model in apps.get_models():
        if model.__name__ not in default_models:
            custom_models.append(model.__name__)

    return custom_models


def check_csv_errors(file_path, model_name):
    model = None
    for app_config in apps.get_app_configs():
        try:
            model = apps.get_model(app_config.label, model_name)
            break
        except LookupError:
            continue

    if not model:
        raise CommandError(f"model {model_name} not found in any app")
    # Compare CSV header with
    # get all the field names of the model
    model_fields = [field.name for field in model._meta.fields]
    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            reader = csv.DictReader(file)
            csv_reader = reader.fieldnames

            if csv_reader != model_fields:
                raise DataError(
                    f"CSV file dosen't match with the {model_name} table fields"
                )

    except Exception as e:  # noqa: TRY203
        raise e  # noqa: TRY201

    return model;




def send_email_notification(mail_subject,message,to_email):  

    try:
        email_sender=settings.DEFAULT_FROM_EMAIL
        email=django.core.mail.EmailMessage(mail_subject,message,email_sender,to=[to_email])
        email.send()
    except Exception as e:  # noqa: TRY203
        raise e  # noqa: TRY201
