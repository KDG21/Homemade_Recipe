from django.urls import path

from recipe.views import MainPageView, DetailPageView

urlpatterns = [
    path('/mainpage', MainPageView.as_view()),
    path('/detailpage', DetailPageView.as_view()),
]