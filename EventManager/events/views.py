from django.views import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListCreateAPIView

from .models import Event
from .serializers import EventSerializer


@method_decorator(csrf_exempt, name='dispatch')
class EventListView(ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    def get(self, request, *args, **kwargs):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = EventSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

class EventCreateView(CreateAPIView):
    serializer_class = EventSerializer