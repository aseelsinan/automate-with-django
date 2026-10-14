from django.db import models

class Student(models.Model):
    roll_number=models.CharField( max_length=10)
    name=models.CharField( max_length=20)
    age=models.PositiveIntegerField()
    
    
    def __str__(self):
        return f'{self.name}'
    
    
    
class Customer(models.Model):
    customer_name=models.CharField( max_length=10)
    country=models.CharField( max_length=20)
    
    
    def __str__(self):
        return self.customer_name

class FifaPlayer(models.Model):
    id = models.BigIntegerField(primary_key=True)  # ليتطابق مع الـ ID الموجود في ملف الـ CSV
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    overall_rating = models.IntegerField()        # بما أنها أقيم رقمية في ملف الـ CSV
    position = models.CharField(max_length=50)
    club = models.CharField(max_length=50)
    league = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    preferred_foot = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"