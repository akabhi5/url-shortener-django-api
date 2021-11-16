from django.urls import path
from shortener import views

urlpatterns = [
    path('urllist/', views.URLShortenerList.as_view()),
    path('urldetail/<str:link>/', views.URLShortenerDetail.as_view()),
]
