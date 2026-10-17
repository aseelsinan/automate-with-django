
from django.urls import path

from . import views

urlpatterns = [
path('import-data/',views.data_entry,name='import-data')
]
 