from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import customers_model
from . import customers_serializer


def getAllCustomers(request):
    customers = customers_model.Customer.objects.all().order_by('id')
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(customers, request)
    serializer = customers_serializer.CustomerSerializer(result_page, many=True)
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