from rest_framework.views import APIView
#from app.controller.CodeRelease import
from django.http import JsonResponse


class Release(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(['get', 'release'],safe=False)

    def post(self, request, *args, **kwargs):
        return JsonResponse(['success', 'this is the success message'],safe=False)