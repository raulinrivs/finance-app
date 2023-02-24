from django.db import models
from finance.models import Company, Employee, Expense
from finance.forms import CompanyForm, EmployeeForm, ExpenseForm
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView

class CompanyCreationView(CreateView):
    template_name = 'company.html'
    model = Company
    form_class = CompanyForm
    
    def form_valid(self, form):
        form.save()

class CompanyBalanceSheetView(TemplateView):
    template_name = 'company_balance_sheet.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        employees = Employee.objects.filter(company=self.request.user.company)
        expenses = Expense.objects.filter(company=self.request.user.company)
        context = prepareContext(context, employees, expenses, self.request.user.company)
        return context
    
def prepareContext(context, employees, expenses, company):
    for employee in employees:
        pass
        ## Férias           2.778% (Sal/3 / 12)
        ## 13º Salário      8.83% (Sal/12)
        ## FGTS             8%
        ## FGTS 13º         0.889%
        ## Multa 40% FGTS   3.56% (FGTS + FGTS 13º * 40%)
    for expense in expenses:
        if expense.variable == False:
            context[expense.name] = expense.amount
        # else:
        #     context[expense.name] = expense.amount
    return context
    
        
class EmployeeCreationView(CreateView):
    template_name = 'company.html'
    model = Employee
    form_class = EmployeeForm
    
    def form_valid(self, form):
        Employee.objects.create(
            first_name = form.cleaned_data['first_name'],
            last_name = form.cleaned_data['last_name'],
            cpf = form.cleaned_data['cpf'],
            salary = form.cleaned_data['salary'],
            company = self.request.user.company
            ) 

class ExpenseCreationView(CreateView):
    template_name = 'company.html'
    model = Expense
    form_class = ExpenseForm
    
    def form_valid(self, form):
        Expense.objects.create(
            name = form.cleaned_data['name'],
            amount = form.cleaned_data['amount'],
            variable = form.cleaned_data['variable'],
            company = self.request.user.company
            ) 