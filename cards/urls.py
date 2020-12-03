from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:deck>/<slug:name>/', views.detail, name='detail'),
]
