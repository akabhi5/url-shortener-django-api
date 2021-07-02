from users.custom_token import MyTokenObtainPairSerializer
from django.urls import path
from users.views import SignUp
from users.custom_token import MyTokenObtainPairView


urlpatterns = [
    path('signup/', SignUp.as_view()),
    path('login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
]
