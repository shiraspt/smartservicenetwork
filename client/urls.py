from django.urls import path
from . import views
app_name='client'
urlpatterns=[
    path("login",views.login,name='login'),
    path("reg_client",views.reg_client,name='reg_client'),
    path("client_login",views.client_login,name='client_login')
    
    
]