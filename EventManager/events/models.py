from django.db import models
import uuid

class Event(models.Model):
    name = models.CharField(max_length=225)
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    source = models.CharField(max_length=225)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.name