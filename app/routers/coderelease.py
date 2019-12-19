from django.urls import path
from app.views import codeRelease


urlpatterns = [
    path('',codeRelease.Release.as_view()),
]