from django.db import models
from django.contrib.auth.models import AbstractUser

class Company(models.Model):
    name = models.CharField(max_length=150)
    cnpj = models.CharField(max_length=25)
    profit = models.DecimalField(decimal_places=2, max_digits=5)
    
    def __str__(self) -> str:
        return self.name

class CustomUser(AbstractUser):
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING, blank=True, null=True)

class Employee(models.Model):
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=100)
    cpf = models.CharField(max_length=15)
    salary = models.DecimalField(decimal_places=2, max_digits=7)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'
    
class Expense(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(decimal_places=2, max_digits=7)
    variable = models.BooleanField(default=False)
    company = models.ForeignKey(Company, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return f'{self.name} - {self.company.name}'
    