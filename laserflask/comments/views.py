from django.shortcuts import render
from django.template.loader import render_to_string
from .models import Comment


def get_comments_quantity(request):
    comment_count = Comment.objects.all().count()
    return render_to_string(
        'comments.html',
        {'comments_count': comment_count}
    )