from django.urls import path, include

urlpatterns = [
    path('account', include('account.urls')),
    # path('recipe', include('recipe.urls'))
]
