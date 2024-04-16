from django.urls import path
from .views import add_grossary,show_grossary,update_grossary,delete_grossary

urlpatterns = [

    path('add/',add_grossary ,name='add_url'),
    path('show/',show_grossary ,name='show_url'),
    path('update/<int:pk>/',update_grossary ,name='update_url'),
    path('delete/<int:pk>/',delete_grossary ,name='delete_url')
]