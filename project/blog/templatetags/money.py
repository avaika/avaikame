from django import template
from django.db.models import Sum
from project.partner.models import Payment, Transaction

register = template.Library()


@register.assignment_tag
def money(user):
    money_all = Payment.objects.filter(user_id=user)
    rmoney = {}
    rmoney['all'] = int(money_all.aggregate(s=Sum('summ'))['s'] or 0) * 0.08
    money_out = money_all.filter(payment__isnull=False)
    rmoney['out'] = int(money_out.aggregate(s=Sum('summ'))['s'] or 0) * 0.08
    money_in = Transaction.objects.filter(user_id=user, payment__isnull=True)
    rmoney['in'] = int(money_in.aggregate(s=Sum('summ'))['s'] or 0) * 0.08
    rmoney['all'] += rmoney['in']
    return rmoney


@register.simple_tag()
def multiply(price, *args, **kwargs):
        # you would need to do any localization of the result here
        return float(price) * 0.08
