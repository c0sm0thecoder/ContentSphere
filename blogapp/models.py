from django.db import models
from django.conf import settings
from django.db.models.constraints import UniqueConstraint


class Category(models.TextChoices):
    TECHNOLOGY = 'TECH', 'Technology'
    STARTUPS = 'START', 'Startups'
    GAMES = 'GAME', 'Games'
    AI = 'AI', 'AI'
    APPS = 'APP', 'Apps'
    ENTERTAINMENT = 'ENTE', 'Entertainment'
    FEATURED = "FEAT", "Featured"
    OTHER = 'OTHR', 'Other'


class Post(models.Model):
    title = models.CharField(max_length=150, blank=False, null=False)
    cover_image = models.ImageField(
        upload_to='post_cover_images/', blank=False, null=False)
    contents = models.TextField(blank=False, null=False)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.CharField(
        max_length=6,
        choices=Category.choices,
        blank=False,
        null=False
    )

    class Meta:
        unique_together = ('post', 'category')
        constraints = [
            models.UniqueConstraint(
                fields=['post', 'category'], name='unique_category')
        ]


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    contents = models.TextField(blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'


class Like(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    session_id = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['post', 'user'], name='unique_like')
        ]

    def __str__(self):
        return f'Like by {self.user} on {self.post}'


class AboutUs(models.Model):
    content = models.TextField()

    def __str__(self):
        return "About Us Content"


class Contact(models.Model):
    contact_email = models.EmailField(max_length=254, help_text="Email address to receive contact form messages.")

    def __str__(self):
        return "Site Settings"
