from django.contrib import admin
from comments.models import Comment


@admin.register(Comment)
class CommentsAdmin(admin.ModelAdmin):
    list_display = [
        'comment_text', 'created_by',
        'publication',
        'created_at', 'updated_at'
    ]
    list_filter = ['created_by', 'created_at']
    search_fields = [
        'comment_text',
        'publication__title',
        'created_by__username',
    ]
    list_editable = ['created_by']
