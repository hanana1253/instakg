import time
from django.db import models

class BaseFields(models.Model):
    is_deleted = models.BooleanField(default=False)
    created_at = models.TextField(default=time.time())
    updated_at = models.TextField(null=True, blank=True)
  
    class Meta:
        abstract = True
