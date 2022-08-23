from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count

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

class OperatorViewSet(viewsets.ModelViewSet):
    queryset = Operator.objects.all()
    serializer_class = OperatorSerializer
    permission_classes = [permissions.AllowAny]


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.AllowAny]


class MailingViewSet(viewsets.ModelViewSet):
    queryset = Mailing.objects.all()
    serializer_class = MailingSerializer
    permission_classes = [permissions.AllowAny]


class MessageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [permissions.AllowAny]


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.AllowAny]


@api_view(['GET'])
def get_statistics_for_all_mailings(request):
    statistics = {
        "mailings": []
    }

    mailings = Mailing.objects.all()
    for mailing in mailings:
        messages = Message.objects.filter(mailing=mailing)
        mailing_statistics = messages \
            .values('status') \
            .annotate(messages=Count('status')) \
            .order_by()

        print(mailing_statistics)
        for mailing_statistic in mailing_statistics:
            statistics['mailings'].append(
                {
                    "status": mailing_statistic['status'],
                    "messages": mailing_statistic['messages']
                })

    return Response(statistics)

@api_view(['GET'])
def get_statistics_for_mailing(request, mailing_uuid):
    try:
        mailing = Mailing.objects.get(uuid=mailing_uuid)
        request_status = status.HTTP_200_OK
    except:
        request_status = status.HTTP_404_NOT_FOUND
    
    statistics = {
        "mailing": mailing_uuid,
        "messages": []
    }

    messages = Message.objects.filter(mailing=mailing).order_by('status')

    for message in messages:
        statistics['messages'].append(
            {
                "status": message.status,
                "customer": message.customer.phone,
                "created_date": message.created_date
            })

    return Response(statistics, status=request_status)