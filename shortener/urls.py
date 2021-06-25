from django.urls import path
from shortener.views import get_user_urls, generate_url, get_original_url

urlpatterns = [
    path('userurls/', get_user_urls),
    path('generateurl/', generate_url),
    path('geturl/<str:link>/', get_original_url),
]
