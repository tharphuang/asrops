from django.db import models

# Create your models here.

class CodeFile(models.Model):
    id = models.AutoField(primary_key=True)
    filename = models.CharField(max_length=50)
    filepath = models.FilePathField(max_length=100)
    codefile = models.FileField(upload_to=None,max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)


