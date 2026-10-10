from django.core.management.base import BaseCommand

class Command(BaseCommand):
    # وصف لعمل الكوماند
    help="Prints Hello World"
    
    def handle(self, *args, **options):
        # Logic to preform for command
        
        # Write Message in Terminal
        self.stdout.write('Hello World')
        # return super().handle(*args, **options)