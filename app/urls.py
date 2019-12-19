from django.urls import path, include


urlpatterns = [
    path('codehub/', include('app.routers.codehub')),
    path('coderelease/',include('app.routers.coderelease'))
]
