from django.contrib import admin
from app.models import CodeFile


# Register your models here.
@admin.register(CodeFile)
class CodeFile(admin.ModelAdmin):
    list_display = ('id', 'filename', 'filepath', 'codefile', 'created')

