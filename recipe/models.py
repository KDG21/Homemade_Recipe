from django.db import models

class Recipe(models.Model):
    account    = models.ForeignKey('account.Account',on_delete=models.CASCADE)
    title      = models.CharField(max_length=200, blank=True, null=True)
    detail     = models.CharField(max_length=5000, blank=True, null=True)
    image_url  = models.CharField(max_length=500, blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    del_yn     = models.BooleanField(default=False)
    ins_date   = models.DateTimeField(auto_now_add=True)
    upd_date   = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recipes'

class Comment(models.Model):
    account  = models.ForeignKey('account.Account',on_delete=models.CASCADE)
    recipe   = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    content  = models.CharField(max_length=5000, blank=True, null=True)
    del_yn   = models.BooleanField(default=False)
    ins_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comments'

class ReComment(models.Model):
    account  = models.ForeignKey('account.Account',on_delete=models.CASCADE)
    recipe   = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    comment  = models.ForeignKey('Comment',on_delete=models.CASCADE)
    content  = models.CharField(max_length=5000, blank=True, null=True)
    del_yn   = models.BooleanField(default=False)
    ins_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 're_comments'

class RecipeLike(models.Model):
    account  = models.ForeignKey('account.Account',on_delete=models.CASCADE)
    recipe   = models.ForeignKey('Recipe', on_delete=models.CASCADE)
    like_yn  = models.BooleanField(default=False)
    ins_date = models.DateTimeField(auto_now_add=True)
    upd_date = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'recipe_likes'