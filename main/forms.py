from django.utils import timezone

from main.models import Subscription
from users.forms import StyleFormMixin
from django import forms


class SubscriptionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Subscription
        fields = []

    def create_subscription(self, user, blog):
        subscription = self.save(commit=False)
        subscription.user = user
        subscription.blog = blog
        subscription.status = True
        subscription.payment_status = True
        subscription.payment_date = timezone.now()
        subscription.save()
