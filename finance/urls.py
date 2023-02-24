"""
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from finance.views import CompanyCreationView, EmployeeCreationView, ExpenseCreationView, CompanyBalanceSheetView

urlpatterns = [
    path('company/', CompanyBalanceSheetView.as_view()),
    path('employee/', EmployeeCreationView.as_view()),
    path('expense/', ExpenseCreationView.as_view()),
]
