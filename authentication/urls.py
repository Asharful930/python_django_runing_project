
from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_page,name='login'),
    path('forgot', views.forgot_page,name='forgot'),
    path('regstions', views.regstions_page,name='regstions'),
]
