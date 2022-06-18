from django.shortcuts import render

def forum(request):
    template_name = 'forum/forum.html'
    context = {
        'home':True
    }
    return render(request, template_name, context)
