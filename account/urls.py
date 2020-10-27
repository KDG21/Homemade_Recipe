from django.urls import path
from account.views import SignUpView, SignInView, MyPage

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SignInView.as_view()),
    path('/mypage', MyPage.as_view()),
]
