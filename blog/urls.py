from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index  , name='index'),
    path('single/<slug:slug>/' , views.single  , name='single'),
    path('categories/' , views.category_wiew, name='categories'),
    path('index/',views.index,name='index'),
]

