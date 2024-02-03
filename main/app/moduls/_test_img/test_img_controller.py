from rest_framework import status, settings
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
import os

from . import test_img_model
from . import test_img_serializer


def fileSave(request):
    file_obj = request.FILES.get('file')

    if not file_obj:
        return Response({'error': 'No file provided'}, status=status.HTTP_400_BAD_REQUEST)

    file_name = file_obj.name

    # Save the file name in the database
    test_img_model.Picture.objects.create(file_name=file_name)

    # Specify the path where you want to store the file within the media directory
    file_path = os.path.join(settings.MEDIA_ROOT, 'path_within_your_app', file_name)

    # Save the file in the specified path
    with open(file_path, 'wb') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

    return Response({'status': 'File uploaded successfully'}, status=status.HTTP_201_CREATED)