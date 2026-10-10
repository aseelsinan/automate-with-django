from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help='Greeting Command'
    def add_arguments(self, parser):
        parser.add_argument('name',type=str,help='Enter your username')
        
    def handle(self, *args, **options):
        name =options['name']
        greeting=f'Hi {name} Good morning'
        self.stdout.write(self.style.WARNING(greeting))


