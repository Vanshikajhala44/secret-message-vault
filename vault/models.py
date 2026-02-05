import uuid
from django.db import models

class SecretMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    encrypted_message = models.TextField()
    expires_at = models.DateTimeField(null=True, blank=True)
    viewed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
