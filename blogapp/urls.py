from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.home, name='landing'),
    path('category/<str:category_code>/',
         views.category_posts, name='category_news'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/<int:post_id>/like/', views.add_like, name='add_like'),
    path('post/<int:post_id>/comment/', views.add_comment, name='add_comment'),
    path('profile/', views.profile_view, name='profile'),
    path('create_post/', views.create_post_view, name='create_post'),
    path('post/<int:post_id>/edit/', views.edit_post_view, name='edit_post'),
    path('post/<int:post_id>/delete/',
         views.delete_post_view, name='delete_post'),
    path('about-us/', views.about_us, name='about_us'),
    path('contact/', views.contact_view, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
