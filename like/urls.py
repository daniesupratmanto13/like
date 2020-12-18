from django.urls import path


from .views import *

app_name = 'like'

urlpatterns = [
    path('', index, name='index'),
    path('like_post/', likePost, name='like_post')
]
