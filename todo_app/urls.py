from django.urls import path
from . import views

urlpatterns=[
    path('',views.task_view,name='task_view'),
    # path('task',views.task,name='task')
]

