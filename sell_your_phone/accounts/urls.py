from django.urls import path
from sell_your_phone.accounts.views import LoginUserView, logout_user, RegisterView, profile_details

urlpatterns = [
    path('login/', LoginUserView.as_view(), name='log in user'),
    path('logout/', logout_user, name='log out user'),
    path('register/', RegisterView.as_view(), name='register user'),
    path('profile/', profile_details, name='profile details'),
]
