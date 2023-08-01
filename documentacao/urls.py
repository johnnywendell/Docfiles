from django.urls import path
from documentacao import views as v


app_name ='documentacao'

urlpatterns =[
    path('departamento/', v.dept_create, name='dept_create'),
    path('departamentolist/', v.DepartamentoList.as_view(), name='dept_list'),
]