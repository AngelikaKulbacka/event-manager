from django.urls import path
from .views import EventListView
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('events/', EventListView.as_view(), name='event-list'),
    path('graphql', GraphQLView.as_view(schema=schema), name='graphql'),
]
