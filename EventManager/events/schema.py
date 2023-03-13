import graphene
from graphene import relay
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.utils import timezone
from graphql import GraphQLError
from django_filters import FilterSet, OrderingFilter
from .models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'uuid': ['exact', 'icontains', 'istartswith'],
            'source': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)


class EventFilter(FilterSet):
    class Meta:
        model = Event
        fields = {
            'name': ['exact', 'icontains', 'istartswith'],
            'uuid': ['exact', 'icontains', 'istartswith'],
            'source': ['exact', 'icontains', 'istartswith'],
            'description': ['exact', 'icontains', 'istartswith'],
        }
    order_by = OrderingFilter(
        fields=(
            ('created_at'),
            ('updated_at'),
        )
    )


class Group(DjangoObjectType):
  events = DjangoFilterConnectionField(EventType, filterset_class=EventFilter)

  class Meta:
      name = 'Group'
      model = Event
      interfaces = (relay.Node,)

  def resolve_events(self, info, **kwargs):
    return EventFilter(kwargs).qs


class Query(graphene.ObjectType):
    event = relay.Node.Field(EventType)
    events = DjangoFilterConnectionField(EventType, filterset_class=EventFilter)
    event_by_uuid = graphene.Field(EventType, uuid=graphene.UUID(required=True))

    # def resolve_events(self, info, order_by=None, **kwargs):
    #     events = Event.objects.all()
    #     if order_by:
    #         events = events.order_by(*order_by)
    #     return events

    def resolve_event_by_uuid(self, info, uuid):
        try:
            return Event.objects.get(uuid=uuid)
        except Event.DoesNotExist:
            return GraphQLError(f"Event with uuid {uuid} does not exist.")


class EventInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    source = graphene.String(required=True)
    description = graphene.String(required=True)


class CreateEvent(graphene.Mutation):
    class Arguments:
        input = EventInput(required=True)

    event = graphene.Field(EventType)

    def mutate(self, info, input):
        if not input.name:
            raise GraphQLError("Event name is required.")
        if not input.source:
            raise GraphQLError("Event source is required.")
        if not input.description:
            raise GraphQLError("Event description is required.")

        event = Event(name=input.name, source=input.source, description=input.description)
        event.save()
        return CreateEvent(event=event)


class UpdateEvent(graphene.Mutation):
    class Arguments:
        event_uuid = graphene.UUID(required=True)
        input = EventInput(required=True)

    event = graphene.Field(EventType)

    def mutate(self, info, event_uuid, input):
        try:
            event = Event.objects.get(uuid=event_uuid)
            event.name = input.name
            event.source = input.source
            event.description = input.description
            event.updated_at = timezone.now()
            event.save()
            return UpdateEvent(event=event)
        except Event.DoesNotExist:
            return None


class DeleteEvent(graphene.Mutation):
    class Arguments:
        event_uuid = graphene.UUID(required=True)

    success = graphene.Boolean()

    def mutate(self, info, event_uuid):
        try:
            event = Event.objects.get(uuid=event_uuid)
            event.delete()
            return DeleteEvent(success=True)
        except Event.DoesNotExist:
            return DeleteEvent(success=False)


class Mutation(graphene.ObjectType):
    create_event = CreateEvent.Field()
    update_event = UpdateEvent.Field()
    delete_event = DeleteEvent.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)