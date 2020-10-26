from django.urls import path

from recipe.views import MainPageView, DetailPageView, CommentCreateView, CommentDeleteView, CommentUpdateView, RecipeLikeView

urlpatterns = [
    path('/mainpage', MainPageView.as_view()),
    path('/detailpage', DetailPageView.as_view()),
    path('/comment_create', CommentCreateView.as_view()),
    path('/comment_delete', CommentDeleteView.as_view()),
    path('/comment_update', CommentUpdateView.as_view()),
    path('/recipe_like', RecipeLikeView.as_view()),
]