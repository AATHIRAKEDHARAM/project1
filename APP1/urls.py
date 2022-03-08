from django.urls import path
from . import views
urlpatterns = [
    path('index',views.program),
    path('html',views.index)
    
]