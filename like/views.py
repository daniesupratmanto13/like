from django.shortcuts import redirect, render
from django.http import JsonResponse

# Create your views here.
from .models import *


def index(request):
    posts = Post.objects.order_by('-created')[:10]
    user = request.user
    context = {
        'posts': posts,
        'user': user,
    }
    return render(request, 'like/index.html', context)


def likePost(request):
    user = request.user
    if request.method == 'POST':
        post_id = request.POST.get('post-id')
        post = Post.objects.get(id=post_id)

        if user in post.liked.all():
            post.liked.remove(user)
        else:
            post.liked.add(user)

        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'
            else:
                like.value = 'Like'
        like.save()

        data = {
            'value': like.value,
            'likes': post.totalLike,
        }

        return JsonResponse(data, safe=False)

    return JsonResponse('likePost', safe=False)
