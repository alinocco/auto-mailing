from rest_framework import serializers
from drf_writable_nested.mixins import UniqueFieldsMixin, NestedUpdateMixin

from ..models import (
    Operator,
    Tag,
    Mailing,
    Customer,
    Message,
)

class OperatorSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = '__all__'

    def create(self, validated_data):
        operator = Operator.objects.get_or_create(**validated_data)
        return operator


class TagSerializer(UniqueFieldsMixin, serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

    def create(self, validated_data):
        tag = Tag.objects.get_or_create(**validated_data)
        return tag


class MailingSerializer(NestedUpdateMixin, serializers.ModelSerializer):
    operator = OperatorSerializer(required=False)
    tag = TagSerializer(required=False)

    class Meta:
        model = Mailing
        fields = '__all__'

    def create(self, validated_data):
        if 'operator' in validated_data.keys():
            operator_data = validated_data.pop('operator')
            operator, _ = Operator.objects.get_or_create(**operator_data)

        if 'tag' in validated_data.keys():
            tag_data = validated_data.pop('tag')
            tag, _ = Tag.objects.get_or_create(**tag_data)

        if 'operator' in validated_data.keys() or 'tag' in validated_data.keys():
            mailing = Mailing.objects.create(operator=operator, tag=tag, **validated_data)
        else:
            mailing = Mailing.objects.create(**validated_data)

        return mailing

    def update(self, instance, validated_data):
        if 'operator' in validated_data.keys():
            operator_data = validated_data.pop('operator')
            operator, _ = Operator.objects.get_or_create(**operator_data)

        if 'tag' in validated_data.keys():
            tag_data = validated_data.pop('tag')
            tag, _ = Tag.objects.get_or_create(**tag_data)

        instance.operator = operator
        instance.tag = tag

        instance.start_date = validated_data.get('start_date', instance.start_date)
        instance.stop_date = validated_data.get('stop_date', instance.stop_date)
        instance.message_text = validated_data.get('message_text', instance.message_text)

        return instance


class CustomerSerializer(NestedUpdateMixin, serializers.ModelSerializer):
    operator = OperatorSerializer()
    tag = TagSerializer(required=False)

    class Meta:
        model = Customer
        fields = '__all__'
    
    def create(self, validated_data):
        operator_data = validated_data.pop('operator')
        operator, _ = Operator.objects.get_or_create(**operator_data)

        if 'tag' in validated_data.keys():
            tag_data = validated_data.pop('tag')
            tag, _ = Tag.objects.get_or_create(**tag_data)

        customer = Customer.objects.create(operator=operator, tag=tag, **validated_data)
        return customer

    def update(self, instance, validated_data):
        operator_data = validated_data.pop('operator')
        operator, _ = Operator.objects.get_or_create(**operator_data)

        if 'tag' in validated_data.keys():
            tag_data = validated_data.pop('tag')
            tag, _ = Tag.objects.get_or_create(**tag_data)

        instance.operator = operator
        instance.tag = tag

        instance.phone = validated_data.get('phone', instance.phone)
        instance.timezone = validated_data.get('timezone', instance.timezone)

        return instance


class MessageSerializer(serializers.ModelSerializer):
    mailing = MailingSerializer()
    operator = OperatorSerializer()

    class Meta:
        model = Message
        fields = '__all__'