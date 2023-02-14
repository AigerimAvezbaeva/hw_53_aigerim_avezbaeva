from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

from to_do_app.models import ToDoParagraph


def add_paragraph(request: WSGIRequest):
    if request.method == 'GET':
        return render(request, 'add_paragraph.html')

    paragraph_data = {
        'title': request.POST.get('title'),
        'status': request.POST.get('status'),
        'completion_date': request.POST.get('completion_date')
    }
    ToDoParagraph.objects.create(**paragraph_data)
    statuses = ToDoParagraph.return_choices()
    context = {
        'statuses': statuses
    }
    render(request, 'add_paragraph.html', context=context)
    return redirect(request, 'to_do_list.html')


