from django.contrib import admin

from FINAL_EXAM.common.models import Like, Comment


# Register your models here.
@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'to_drawing')
    list_per_page = 20

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'to_drawing')
    list_per_page = 20
