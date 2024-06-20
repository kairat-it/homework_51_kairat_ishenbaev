from django.urls import path
from . import views

urlpatterns = [
    path('cat/', views.cat_info, name='cat_info'),
    path('greet/', views.greet, name='greet'),
    path('', views.greet),
]
