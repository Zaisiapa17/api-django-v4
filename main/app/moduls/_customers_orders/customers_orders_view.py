from rest_framework.decorators import api_view

from . import customers_orders_controller

@api_view(['GET'])
def orderList(request, pk):
    return customers_orders_controller.getItemsCheckOut(request, pk)