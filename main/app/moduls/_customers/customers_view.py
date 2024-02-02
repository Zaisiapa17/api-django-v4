from rest_framework.decorators import api_view

from . import customers_controller

@api_view(['GET'])
def customersList(request):
    return customers_controller.getAllCustomers(request)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def customer(request, pk):
    if request.method == 'GET':
        return customers_controller.getCustomerById(pk)
    
    elif request.method == 'POST':
        return customers_controller.addCustomer(request)
    
    elif request.method == 'DELETE':
        return customers_controller.deleteCustomer(request, pk)
    
    elif request.method == 'PUT':
        return customers_controller.editCustomer(request, pk)