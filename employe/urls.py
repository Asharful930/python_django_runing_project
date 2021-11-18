from django.urls import path
from.import views
urlpatterns = [
    path('', views.employe),
    path('profile/',views.profile,name='profile'),
    
]