from rest_framework import status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from . import customers_model
from . import customers_serializer


def getAllCustomers(request):
    try:
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

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def getCustomerById(pk):
    try:
        customer = customers_model.Customer.objects.get(pk=pk)
        serializer = customers_serializer.CustomerSerializer(customer)
        data_response = {
            'status': "success",
            'data': serializer.data,
        }
        return Response(data_response)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def addCustomer(request):
    try:
        serializer = customers_serializer.ActCustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data_response = {
                'status': "success add customer",
            }
            return Response(data_response, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def deleteCustomer(pk):
    try:
        customer = customers_model.Customer.objects.get(pk=pk)
        customer.delete()
        data_response = {
            'status': "success delete customer",
        }
        return Response(data_response, status=status.HTTP_204_NO_CONTENT)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def editCustomer(request, pk):
    try:
        customer = customers_model.Customer.objects.get(pk=pk)
        serializer = customers_serializer.ActCustomerSerializer(customer, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            data_response = {
                'status': "success edit customer",
            }
            return Response(data_response, status=status.HTTP_200_OK)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)