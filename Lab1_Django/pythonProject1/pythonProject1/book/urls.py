from django.urls import path
from .views import *

urlpatterns = [
     path('list/',book_list,name='book_list'),
     path('add/',book_add,name='book_add'),
     path('show/<int:id>',book_details,name='book_details'),
     path('delete/<int:id>',book_delete,name='book_delete'),
     path('update/<int:id>',book_update,name='book_update')
]