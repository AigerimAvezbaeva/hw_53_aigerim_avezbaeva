from django.shortcuts import render

from to_do_app.models import ToDoParagraph


def delete_paragraph(request):
    paragraph_pk = request.GET.get('pk')
    paragraph = ToDoParagraph.objects.get(pk=paragraph_pk)
    paragraph.delete()
    paragraphs = ToDoParagraph.objects.all()
    context = {
        'paragraphs': paragraphs
    }
    return render(request, 'to_do_index.html', context=context)
