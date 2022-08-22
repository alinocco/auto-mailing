from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..models import (
    Operator,
    Tag,
    Mailing,
    Customer,
    Message,
)
from .serializers import (
    OperatorSerializer,
    TagSerializer,
    MailingSerializer,
    CustomerSerializer,
    MessageSerializer,
)

class OperatorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OperatorSerializer
    permission_classes = [permissions.AllowAny]


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]


class MailingViewSet(viewsets.ModelViewSet):
    serializer_class = MailingSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Mailing.objects.all()


class OperatorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = OperatorSerializer
    permission_classes = [permissions.AllowAny]


class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        return Customer.objects.all()