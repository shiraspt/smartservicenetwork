from django.urls import path
from . import views
app_name='Admin_'
urlpatterns=[
    path("login",views.login,name='login')
]

