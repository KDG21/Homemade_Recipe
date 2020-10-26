import json

from django.utils import timezone
from django.views import View
from django.http  import JsonResponse,HttpResponse
from django.views.generic import ListView

from account.models import Account
from account.utils import login_check
from recipe.models import Recipe, RecipeLike, Comment, ReComment

# 메인페이지
class MainPageView(ListView):
    @login_check
    def get(self, request):
        paginate_by = 10
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
    @login_check
    def get(self, request):
        # food_recipe
        recipe = request.GET.get('recipe')
        food_recipe = Recipe.objects.filter(del_yn=False) and Recipe.objects.prefetch_related('account', 'recipelike_set', 'comment_set__recomment_set').get(id=recipe)
        recipe_detail = {
            'id'                : food_recipe.id,
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
class RecipeView(View):
    @login_check
    def post(self, request):
        account = Account.objects.get(id=request.user.id)
        Recipe.objects.create(
            account = account,
            title   = request.POST.get('title'),
            detail  = request.POST.get('detail'),
        )
        return HttpResponse(status=200)

# 게시글 삭제
class RecipeDeleteView(View):
    @login_check
    def post(self, request):
        Recipe.objects.filter(id=request.GET.get('recipe')).update(
            del_yn   = True,
            upd_date = timezone.now()
        )
        return HttpResponse(status=200)
        
# 게시글 수정
class CommentUpdateView(View):
    @login_check
    def post(self, request):
        Recipe.objects.filter(id=request.GET.get('recipe')).update(
            title    = request.POST.get('title'),
            detail   = request.POST.get('detail'),
            upd_date = timezone.now()
        )
        return HttpResponse(status=200)

# 댓글 작성
class CommentCreateView(View):
    @login_check
    def post(self, request):
        account = Account.objects.get(id=request.user.id)
        recipe = Recipe.objects.get(id=request.GET.get('recipe'))
        Comment.objects.create(
            account  = account,
            recipe   = recipe,
            content  = request.POST.get('content'),
        )
        return HttpResponse(status=200)

# 댓글 삭제
class CommentDeleteView(View):
    @login_check
    def post(self, request):
        Comment.objects.filter(id=request.POST.get('comment_id')).update(
            del_yn   = True,
            upd_date = timezone.now()
        )
        return HttpResponse(status=200)

# 댓글 수정
class CommentUpdateView(View):
    @login_check
    def post(self, request):
        Comment.objects.filter(id=request.POST.get('comment_id')).update(
            content  = request.POST.get('content'),
            upd_date = timezone.now()
        )
        return HttpResponse(status=200)

# 대댓글 작성
class ReCommentCreateView(View):
    @login_check
    def post(self, request):
        account = Account.objects.get(id=request.user.id)
        recipe = Recipe.objects.get(id=request.GET.get('recipe'))
        comment = Comment.objects.get(id=request.POST.get('comment_id'))
        ReComment.objects.create(
            account  = account,
            recipe   = recipe,
            comment  = comment,
            content  = request.POST.get('content')
        )
        return HttpResponse(status=200)

# 대댓글 삭제
class ReCommentDeleteView(View):
    @login_check
    def post(self, request):
        ReComment.objects.filter(id=request.POST.get('recomment_id')).update(
            del_yn   = True,
            upd_date = timezone.now()
        )
        return HttpResponse(status=200)

# 대댓글 수정
class ReCommentUpdateView(View):
    @login_check
    def post(self, request):
        ReComment.objects.filter(id=request.POST.get('recomment_id')).update(
            content  = request.POST.get('content'),
            upd_date = timezone.now()
        )
        return HttpResponse(status=200)

# 게시글 좋아요
class RecipeLikeView(View):
    @login_check
    def post(self, request):
        account = request.user.id
        recipe = Recipe.objects.get(id=request.POST.get('recipe_id'))
        if RecipeLike.objects.filter(account=account, recipe=recipe, like_yn=True).exists():
            RecipeLike.objects.filter(account=account, recipe=recipe, like_yn=True).update(
                like_yn  = False,
                upd_date = timezone.now()
            )
            return HttpResponse(status=200)

        if RecipeLike.objects.filter(account=account, recipe=recipe, like_yn=False).exists():
            RecipeLike.objects.filter(account=account, recipe=recipe, like_yn=True).update(
                like_yn  = True,
                upd_date = timezone.now()
            )
            return HttpResponse(status=200)

        if not RecipeLike.objects.filter(account=account, recipe=recipe).exists():
            RecipeLike.objects.filter(account=account, recipe=recipe, like_yn=True).update(
                like_yn  = True,
                upd_date = timezone.now()
            )
            return HttpResponse(status=200)

# 레시피 검색

# 조회수