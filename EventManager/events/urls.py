from django.urls import path
from .views import EventListView, EventCreateView

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
]
