from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('output', views.OutputView.as_view(), name='output'),
]