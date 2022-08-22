from ast import operator
from rest_framework import serializers
from ..models import (
    Operator,
    Tag,
    Mailing,
    Customer,
    Message,
)

class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class MailingSerializer(serializers.ModelSerializer):
    operator = OperatorSerializer()
    tag = TagSerializer()

    class Meta:
        model = Mailing
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    operator = OperatorSerializer()
    tag = TagSerializer()

    class Meta:
        model = Customer
        fields = '__all__'


class MessageSerializer(serializers.ModelSerializer):
    mailing = MailingSerializer()
    operator = OperatorSerializer()

    class Meta:
        model = Message
        fields = '__all__'