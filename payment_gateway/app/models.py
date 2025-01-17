from django.db import models
from django.db.models.fields import CharField
from django.utils.translation import gettext_lazy as _
from .constants import PaymentStatus
# Create your models here.
class Order(models.Model):
    name= CharField(_("Customer Name"), max_length=254, blank=False, null=False)
    amount=models.FloatField(_("Account"),null=False, blank=False)
    status=CharField(
        _("Payment_Status"),
        default=PaymentStatus.PENDING,
        max_length=254,
        blank=False,
        null=False
    )
    provider_order_id =models.CharField(
        _("order ID"), max_length=40, null=False, blank=False
    )
    payment_id =models.CharField(
        _("order ID"), max_length=36, null=False, blank=False
    )
    signature_id =models.CharField(
        _("order ID"), max_length=128, null=False, blank=False
    )

    def _str_(self):
        return f"{self.id}-{self.name}-{self.status}"

    