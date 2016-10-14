from backenddata.models import *
from rest_framework import serializers

class ToppingsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Toppings
        fields = ('id', 'topping', 'price')


class PizzaSizeSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = PizzaSize
        fields = ('id', 'size', 'price')


class CrustsSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Crusts
        fields = ('id', 'crust', 'price')


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ('id', 'topping', 'size', 'crust', 'finalprice')




