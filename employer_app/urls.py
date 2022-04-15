from django.urls import path
from . import views 

urlpatterns =[
    path('form/', views.employee_form, name='form' ),
    path('list/', views.employee_list, name='list'),
    path('delete/<int:id>', views.employee_delete,name='delete'),
    path('update/<int:id>', views.employee_update,name='update'),
]
