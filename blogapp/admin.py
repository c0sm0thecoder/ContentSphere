from django.contrib import admin

from .models import (
    Post,
    PostCategory,
    Comment,
    Like,
    AboutUs,
    Contact
)

admin.site.register(Post)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(AboutUs)
admin.site.register(Contact)
