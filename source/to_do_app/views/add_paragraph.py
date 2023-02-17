from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from to_do_app.models import ToDoParagraph


def add_paragraph(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_paragraph.html')

    paragraph_data = {
        'title': request.POST.get('title'),
        'description': request.POST.get('description'),
        'status': request.POST.get('status'),
        'completion_date': request.POST.get('completion_date')
    }
    paragraph = ToDoParagraph.objects.create(**paragraph_data)
    return redirect(f'/to_do_list/?pk={paragraph.pk}')


def paragraph_view(request):
    paragraph_pk = request.GET.get('pk')
    paragraph = ToDoParagraph.objects.get(pk=paragraph_pk)
    context = {'paragraph': paragraph}
    return render(request, 'to_do_paragraph.html', context=context)
