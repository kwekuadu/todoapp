from django.urls import path    

from .views import todolist,add,update,delete

urlpatterns = [ 
                path('',todolist,name='todo_list'),
               path('add/',add,name='add'),
                path('update/',update,name='update'),
               path('delete/',delete,name='delete'),
              
              
               ]