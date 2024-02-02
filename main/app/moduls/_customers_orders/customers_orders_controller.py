from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import customers_orders_model
from . import customers_orders_serializer

def getItemsCheckOut(request, pk):
    items = customers_orders_model.OrderContainer.objects.filter(customer=pk)
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(items, request)
    serializer = customers_orders_serializer.ItemsCheckOutSerializer(result_page, many=True)
    data_response = {
        'status': "success",
        'total_data': paginator.page.paginator.count,
        'total_pages': paginator.page.paginator.num_pages,
        'current_page': paginator.page.number,
        'next': paginator.get_next_link(),
        'previous': paginator.get_previous_link(),
        'data': serializer.data,
    }
    return Response(data_response)