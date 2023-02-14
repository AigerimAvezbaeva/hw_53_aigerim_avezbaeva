from django.urls import path
from to_do_app.views.base import to_do_view
from to_do_app.views.delete_paragraph import delete_paragraph
from to_do_app.views.add_paragraph import add_paragraph

urlpatterns = [
    path('', to_do_view),
    path('to_do_list', to_do_view),
    path('to_do_list/add/', add_paragraph),
    path('to_do_list/delete/', delete_paragraph)
]
