from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FileUploadParser


from . import test_img_controller


@api_view(['POST'])
@parser_classes([FileUploadParser])
def upload_file(request):
    return test_img_controller.fileSave(request)