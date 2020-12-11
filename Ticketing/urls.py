from django.conf.urls import url
from django.urls import include, re_path, path
from Ticketing import views
from .views import CreateTicketView, TicketCommentView, GetTicketsByMe, GetTicketsByArea,\
ResolveTicket


urlpatterns = [
    path('ticket/create', CreateTicketView.as_view(), name='create-ticket'),
    path('ticket/comment', TicketCommentView.as_view(), name='comment-ticket'),
    path('ticket/mytickets', GetTicketsByMe.as_view(), name='my-ticket'),
    path('ticket/area', GetTicketsByArea.as_view(), name='tickets-area'),
    path('ticket/resolve', ResolveTicket.as_view(), name='resolve-ticket'),
]
