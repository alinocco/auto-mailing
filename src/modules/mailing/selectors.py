from .models import Customer

def get_customers_for_mailing(mailing):
    customers = Customer.objects.all()

    if mailing.operator:
        customers = customers.filter(operator=mailing.operator)

    if mailing.tag:
        customers = customers.filter(tag=mailing.tag)

    return customers