import json

from django.views import View
from django.http  import JsonResponse,HttpResponse

from account.models import Account
from recipe.models import Recipe, RecipeLike, Comment, ReComment

# 메인페이지
class MainPageView(View):
    def get(self, request):
        # food_recipe
        food_recipe = Recipe.objects.prefetch_related('account', 'recipelike_set', 'comment_set', 'recomment_set').filter(del_yn=False)[::-1]
        recipe_list = [
            {
                'nickname'             : recipe.account.nickname,
                'recipe_title'         : recipe.title,
                'recipe_image'         : recipe.image_url,
                'recipe_view_count'    : recipe.view_count,
                'recipe_like_count'    : recipe.recipelike_set.filter(like_yn=True).count(),
                'recipe_comment_count' : (recipe.comment_set.filter(del_yn=False).count()) + (recipe.recomment_set.filter(del_yn=False).count()),
            }for recipe in food_recipe
        ]
        return JsonResponse({'recipe_list':recipe_list}, status=200)

# 상세페이지
class DetailPageView(View):
    def get(self, request):
        # food_recipe
        recipe = request.GET.get('recipe')
        food_recipe = Recipe.objects.filter(del_yn=False) and Recipe.objects.prefetch_related('account', 'recipelike_set', 'comment_set__recomment_set').get(id=recipe)
        recipe_detail = {
                'nickname'          : food_recipe.account.nickname,
                'recipe_title'      : food_recipe.title,
                'recipe_image'      : food_recipe.image_url,
                'recipe_detail'     : food_recipe.detail,
                'recipe_view_count' : food_recipe.view_count,
                'recipe_like_count' : food_recipe.recipelike_set.filter(like_yn=True).count(),
        }
        # comment
        recipe_comment = [
            {
                'comment_nickname'   : comment.account.nickname,
                'comment'            : comment.content,
                'recomment_nickname' : [recomment.account.nickname for recomment in comment.recomment_set.filter(del_yn=False)],
                'recomment'          : [recomment.content for recomment in comment.recomment_set.filter(del_yn=False)],
            }for comment in food_recipe.comment_set.filter(del_yn=False)
        ]
        return JsonResponse({'recipe_detail':recipe_detail, 'recipe_comment':recipe_comment}, status=200)

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

# 조회수