from django.urls import path

from .views import *

app_name = 'pages'

urlpatterns = [
    path('',home_page,name='home'),
    # path('', register_page, name='register')

]