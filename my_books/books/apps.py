from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'), 
    path('detail_book/<int:book_id>/', views.detail_book, name='detail_book'), 
]
