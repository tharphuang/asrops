from django.urls import path
from app.views import codeHub


urlpatterns = [
    path('',codeHub.Data.as_view()),
    path('getFileContent/<file_name>', codeHub.Data.getFileCont),
    path('getTarFile/<file_name>',codeHub.Data.getTarFile)
]