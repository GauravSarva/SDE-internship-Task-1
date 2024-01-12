from django.urls import path
import myapp.views

urlpatterns = [
    path('', myapp.views.ui, name='front page'),
    path('task', myapp.views.task, name='task'),
]