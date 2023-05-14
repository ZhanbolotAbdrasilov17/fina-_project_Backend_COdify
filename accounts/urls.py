from django.urls import path
from .views import SignupView, UserUpdateView, UserInfoView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('user/info/', UserInfoView.as_view()),
    path('user/update/', UserUpdateView.as_view()),

]