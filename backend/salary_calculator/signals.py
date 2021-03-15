from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from salary_calculator.models import Day, Payout


@receiver(post_save, sender=Day)
def update_payout_monthly_earnings(sender, instance, created, **kwargs):
    """Signal updating the monthly earnings for the Payout object when creating or editing a day object."""
    if created:
        Payout.objects.get_or_create(salary=instance.user.salary, month=instance.month, user=instance.user)
    payout = Payout.objects.get(month=instance.month)
    payout.save()


@receiver(post_delete, sender=Day)
def remove_payout_monthly_earnings(sender, instance, **kwargs):
    """Signal updating the monthly earnings for the Payout model when removing a day object."""
    payout = Payout.objects.get(month=instance.month)
    payout.save()
