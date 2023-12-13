from django import template
from django.contrib.auth import get_user_model
from core.models import Order, User

register = template.Library()

@register.filter
def cart_item_count(user):
    if user is not None:
        qs = Order.objects.filter(user=user, ordered=False)
    else:
        User = get_user_model()
        anonymous, created = User.objects.get_or_create(username='anonymous', defaults={'email': 'anonymous@example.com'})
        qs = Order.objects.filter(user=anonymous, ordered=False)
    
    if qs.exists():
        return qs[0].items.count()
    return 0

