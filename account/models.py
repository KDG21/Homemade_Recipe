from django.db import models

class Account(models.Model):
    user_id      = models.CharField(max_length=50)
    password     = models.CharField(max_length=100)
    name         = models.CharField(max_length=100)
    nickname     = models.CharField(max_length=100)
    email        = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=50, blank=True, null=True)
    birthday     = models.CharField(max_length=50, blank=True, null=True)
    leave_date   = models.DateTimeField(blank=True, null=True)
    del_yn       = models.BooleanField(default=False)
    login_date   = models.DateTimeField(blank=True, null=True)
    ins_date     = models.DateTimeField(auto_now_add=True)
    upd_date     = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'accounts'