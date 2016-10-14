from backenddata.models import *
from django.db.models import F, Count
from rest_framework import viewsets
from backenddata.serializers import *
from importlib import import_module
from django.conf import settings
from rest_framework import permissions
from rest_framework.response import Response


SessionStore = import_module(settings.SESSION_ENGINE).SessionStore


class ToppingsViewSet(viewsets.ModelViewSet):
    queryset = Toppings.objects.all()
    serializer_class = ToppingsSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}


class CrustViewSet(viewsets.ModelViewSet):
    queryset = Crusts.objects.all()
    serializer_class = CrustsSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}


class SizeViewSet(viewsets.ModelViewSet):
    queryset = PizzaSize.objects.all()
    serializer_class = PizzaSizeSerializer
    permission_classes = {permissions.IsAuthenticatedOrReadOnly}


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    pricelist = {'pepperoni': 0.50, 'canadianbacon': 0.50, 'pineapple': 0.50, 'sausage': 0.50, 'olives':0.50,
                 'cheese': 0.00, 'regular': 0.00, 'thincrust': 0.50, 'stuffedcrust': 1.50, 'small': 6.00,
                 'medium': 8.00, 'large': 10.00}


    def create(self, request, *args, **kwargs):
        permission_classes = []
        queryset = Order.objects.all()
        if request.method == 'POST':
            finalprice = 0.00
            table = {}

            for key, value in request.data.items():
                if value:
                    price = self.pricelist[key]
                    item = {key: price}
                    finalprice += price
                    table.update(item)
                    table['finalprice'] = finalprice

            serializer = OrderSerializer(data=table)
            serializer.is_valid(raise_exception=True)
            serializer.save()

            return Response(OrderSerializer(instance=queryset, many=True).data)
