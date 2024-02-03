from rest_framework.decorators import api_view


from . import test_img_controller


@api_view(['POST'])
def upload_file(request):
    return test_img_controller.fileSave(request)