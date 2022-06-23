from django.shortcuts import render
from .models import ForumCategory, ForumPost, ForumPostComment, ForumTopics
from forum.forms import ForumCategoryForm, ForumPostCommentForm, ForumTopicsForm, CreateForumPostForm
def forum(request):
    template_name = 'forum/forum.html'
    categories = ForumCategory.objects.all()
    topics = ForumTopics.objects.all()

    context = {
        'home':True,
        'categories': categories,
        'topics': topics,
    }
    return render(request, template_name, context)
