import json

from django.views import View
from django.http  import JsonResponse,HttpResponse

from account.models import Account
from recipe.models import Recipe, RecipeLike, Comment, ReComment

# 메인페이지
# recipe부터 출발
class RecipeListView(View):
    def get(self, request):
        food_recipe = 
        recipe_list = [
            {
                'nickname'           : recipe.nickname,
                'recipe_title'       : [
                    recipe_detail.title for recipe_detail in recipe.recipe_set.all()
                ],
                'recipe_image'       : [
                    recipe_detail.image_url for recipe_detail in recipe.recipe_set.all()
                ],
                'recipe_view_ count' : [
                    recipe_detail.view_count for recipe_detail in recipe.recipe_set.all()
                ],
                'recipe_like'        : ,
            }for recipe in food_recipe
        ]

# 상세페이지

# 게시글 작성

# 게시글 삭제

# 게시글 수정

# 댓글 작성

# 댓글 삭제

# 댓글 수정

# 대댓글 작성

# 대댓글 삭제

# 대댓글 수정

# 게시글 좋아요

# 게시글 좋아요 취소

# 레시피 검색