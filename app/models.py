from django.db import models
from django.conf import settings
import os

def document_upload_path(instance, filename):
    # 'instance' is the Document model instance
    # 'filename' is the original filename of the uploaded file
    return os.path.join('documents', instance.name, filename)

class Document(models.Model):
    name = models.CharField(max_length=100, verbose_name="Document Name")
    document = models.FileField(
        verbose_name="Documents",
        upload_to=document_upload_path
    )

    def __str__(self):
        return str(self.id)

