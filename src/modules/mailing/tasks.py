from celery import shared_task
from django.utils import timezone

from .models import (
    Operator,
    Tag,
    Mailing,
    Customer,
    Message,
)
from .services.api import send_message
from .selectors import get_customers_for_mailing

@shared_task
def activate_mailings():
    mailings = Mailing.objects.filter(
        is_started=False, 
        start_date__lte=timezone.now(),
        stop_date__gte=timezone.now(),
        )

    for mailing in mailings:
        mailing.is_started = True
        mailing.save()

        customers = get_customers_for_mailing(mailing)
        for customer in customers:
            status = send_message(customer.phone, mailing.message_text)
            Message.objects.create(mailing=mailing, customer=customer, status=status)

        mailing.is_completed = True
        mailing.save()

    
