from rest_framework.decorators import api_view

from . import customers_controller

@api_view(['GET'])
def customersList(request):
    return customers_controller.getAllCustomers(request)