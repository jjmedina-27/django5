from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "tittle",
        "body",
        "author",
    )
    list_filter = (
      "author",
      "tittle",
    )

admin.site.register(Post, PostAdmin)