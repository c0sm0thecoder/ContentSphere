from django.shortcuts import (
    render,
    get_object_or_404,
    redirect,
)
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.mail import send_mail

from blogapp.forms import PostForm, ContactForm
from blogapp.models import (
    Post,
    Category,
    PostCategory,
    Comment,
    Like,
    AboutUs,
    Contact
)


def home(request):
    # Fetch the featured category posts
    featured_posts = Post.objects.filter(
        postcategory__category=Category.FEATURED
    ).distinct()

    # Assuming there might be multiple featured posts, take the first one
    featured_post = featured_posts.first() if featured_posts else None

    # Prepare categories excluding the featured
    categories = Category.choices
    categories_with_posts = {}

    for category_code, category_name in categories:
        if category_code == Category.FEATURED:
            continue

        posts = Post.objects.filter(
            postcategory__category=category_code
        ).distinct().order_by('-created_at')

        if posts:
            categories_with_posts[category_name] = {
                "code": category_code, "posts": posts}

    context = {
        'featured_post': featured_post,
        'categories_with_posts': categories_with_posts,
    }
    return render(request, 'blogapp/home.html', context)


def category_posts(request, category_code):
    category_name = dict(Category.choices).get(
        category_code, "Unknown Category")
    # Retrieve all PostCategory instances that match the category_code
    post_categories = PostCategory.objects.filter(category=category_code)
    # Extract the Post instances from the PostCategory queryset
    posts = [pc.post for pc in post_categories][::-1]
    return render(request, 'blogapp/category_news.html', {'category_name': category_name, 'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == 'POST':
        if request.user.is_authenticated:
            content = request.POST.get('comment')
            Comment.objects.create(
                post=post, author=request.user, contents=content)
            return redirect('post_detail', post_id=post_id)
    return render(request, 'blogapp/post_detail.html', {'post': post})


def add_like(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.is_authenticated:
        user = request.user
        like, created = Like.objects.get_or_create(post=post, user=user)
        if not created:
            like.delete()
    else:
        session_id = request.session.session_key
        if not session_id:
            request.session.create()
            session_id = request.session.session_key
        like, created = Like.objects.get_or_create(
            post=post, session_id=session_id)
        if not created:
            like.delete()
    like_count = post.likes.count()
    return JsonResponse({'like_count': like_count})


@login_required
def add_comment(request, post_id):
    if request.method == 'POST':
        post = get_object_or_404(Post, id=post_id)
        comment_content = request.POST.get('comment')
        Comment.objects.create(
            post=post, author=request.user, contents=comment_content)
        return redirect('post_detail', post_id=post_id)


@login_required
def profile_view(request):
    user = request.user
    posts = Post.objects.filter(author=user).order_by('-created_at')
    comments = Comment.objects.filter(author=user)
    liked_posts = Post.objects.filter(likes__user=user)

    context = {
        'user': user,
        'posts': posts,
        'comments': comments,
        'liked_posts': liked_posts,
    }
    return render(request, 'blogapp/profile.html', context)


@login_required
def create_post_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            selected_categories = form.cleaned_data['categories']
            for category in selected_categories:
                PostCategory.objects.create(post=post, category=category)

            return redirect('profile')
    else:
        form = PostForm()

    return render(request, 'blogapp/create_post.html', {'form': form})


@login_required
def edit_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)
    return render(request, 'blogapp/edit_post.html', {'form': form, 'post': post})


@login_required
def delete_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id, author=request.user)
    if request.method == 'POST':
        post.delete()
        return redirect('profile')
    return redirect('post_detail', post_id=post.id)


def about_us(request):
    about_us_content = AboutUs.objects.first()
    return render(request, 'blogapp/about_us.html', {'content': about_us_content})


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = Contact.objects.first()
            contact_email = contact.contact_email if contact else 'defaultemail@example.com'
            
            # send_mail(
            #     subject='Contact Form Submission',
            #     message=form.cleaned_data['message'],
            #     from_email=form.cleaned_data['email'],
            #     recipient_list=[contact_email],
            # )
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'blogapp/contact.html', {'form': form})
