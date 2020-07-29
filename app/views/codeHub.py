from django.http import FileResponse,JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from app.controller.CodeHub import checkfile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile


class Data(APIView):
    def get(self, request, *args, **kwargs):
        return JsonResponse(checkfile.openFileList(),safe=False)

    def post(self, request):
        code_file = request.FILES['file']
        default_storage.save('./codehub/'+code_file.name, ContentFile(code_file.read()))
        return Response({"success", code_file.name})

    def getFileCont(request, file_name):
        return JsonResponse(checkfile.getFileContent(file_name),safe=False)

    def getTarFile(request,file_name):
        file = open('/var/www/html/codehub/' + file_name, 'rb')
        return FileResponse(file)