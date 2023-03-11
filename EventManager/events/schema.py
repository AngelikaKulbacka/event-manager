import graphene
from graphene_django import DjangoObjectType
from .models import Event


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        fields = '__all__'


class Query(graphene.ObjectType):
    events = graphene.List(
        EventType,
        name_contains=graphene.String(),
        source_contains=graphene.String()
    )
    event = graphene.Field(EventType, event_uuid=graphene.UUID(required=True))

    def resolve_events(self, info, name_contains=None, source_contains=None):
        qs = Event.objects.all()
        if name_contains:
            qs = qs.filter(name__icontains=name_contains)
        if source_contains:
            qs = qs.filter(source__icontains=source_contains)
        return qs

    def resolve_event(self, info, event_uuid):
        try:
            return Event.objects.get(uuid=event_uuid)
        except Event.DoesNotExist:
            return None


class EventInput(graphene.InputObjectType):
    name = graphene.String(required=True)
    source = graphene.String(required=True)
    description = graphene.String(required=True)


class CreateEvent(graphene.Mutation):
    class Arguments:
        input = EventInput(required=True)

    event = graphene.Field(EventType)

    def mutate(self, info, input):
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