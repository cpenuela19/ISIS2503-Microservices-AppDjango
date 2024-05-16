from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^places/', views.VariableList, name='variableList'),
    url(r'^placecreate/$', csrf_exempt(views.VariableCreate), name='variableCreate'),
]