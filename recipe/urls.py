from django.urls import path

from recipe.views import MainPageView, DetailPageView, CommentCreateView, CommentDeleteView, CommentUpdateView, RecipeLikeView, RecipeDeleteView, RecipeCreateView, RecipeUpdateView, ReCommentCreateView, ReCommentDeleteView, ReCommentUpdateView, RecipeSearchView

urlpatterns = [
    path('/mainpage', MainPageView.as_view()),
    path('/detailpage', DetailPageView.as_view()),
    path('/comment_create', CommentCreateView.as_view()),
    path('/comment_delete', CommentDeleteView.as_view()),
    path('/comment_update', CommentUpdateView.as_view()),
    path('/recipe_like', RecipeLikeView.as_view()),
    path('/recipe_create', RecipeCreateView.as_view()),
    path('/recipe_delete', RecipeDeleteView.as_view()),
    path('/recipe_update', RecipeUpdateView.as_view()),
    path('/recomment_create', ReCommentCreateView.as_view()),
    path('/recomment_delete', ReCommentDeleteView.as_view()),
    path('/recomment_update', ReCommentUpdateView.as_view()),
    path('/recipe_search', RecipeSearchView.as_view()),
]