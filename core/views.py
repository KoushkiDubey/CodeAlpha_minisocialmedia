from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Post, Comment, Profile
from .forms import PostForm, CommentForm, UserRegisterForm, ProfileUpdateForm
from django.contrib.auth.models import User
import cloudinary.uploader


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'core/auth/register.html', {'form': form})


@login_required
def home(request):
    following_users = request.user.following.all()
    posts = Post.objects.filter(author__profile__in=following_users).order_by('-date_posted')
    form = PostForm()

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user

            if 'image' in request.FILES:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['image'],
                    folder="post_images"
                )
                post.image = upload_result['secure_url']

            post.save()
            return redirect('home')

    return render(request, 'core/home.html', {'posts': posts, 'form': form})


@login_required
def profile(request, username):
    user = get_object_or_404(User, username=username)
    posts = Post.objects.filter(author=user).order_by('-date_posted')
    is_following = request.user in user.profile.followers.all()

    if request.method == 'POST':
        if is_following:
            user.profile.followers.remove(request.user)
        else:
            user.profile.followers.add(request.user)
        return redirect('profile', username=username)

    return render(request, 'core/profile/profile.html', {
        'user': user,
        'posts': posts,
        'is_following': is_following
    })


@login_required
def update_profile(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            if 'image' in request.FILES:
                upload_result = cloudinary.uploader.upload(
                    request.FILES['image'],
                    folder="profile_pics"
                )
                request.user.profile.image = upload_result['secure_url']

            form.save()
            messages.success(request, 'Your profile has been updated!')
            return redirect('profile', username=request.user.username)
    else:
        form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'core/profile/update_profile.html', {'form': form})


@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all().order_by('-date_posted')
    form = CommentForm()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.pk)

    return render(request, 'core/posts/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


@login_required
def like_post(request):
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True

        return JsonResponse({
            'liked': liked,
            'like_count': post.likes.count(),
            'post_id': post.id
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)


@login_required
def explore(request):
    return render(request, 'core/explore.html', {
        'posts': Post.objects.all().order_by('-date_posted'),
        'users': User.objects.exclude(id=request.user.id)
    })