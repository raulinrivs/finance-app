from django import forms
from finance.models import Company, Employee, Expense

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'cnpj', 'profit']
        
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        exclude = ['company']
        
class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        exclude = ['company']