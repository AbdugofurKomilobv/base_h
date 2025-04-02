from django.urls import path

from user_app.views import register_page, logout_view,login_page
from .views import *


app_name = 'pages'

urlpatterns = [
    path('',home_page,name='home'),
    path('register/',register_page,name='register'),
    path('logout/', logout_view, name='logout'),
    path('login/',login_page,name='login')


]