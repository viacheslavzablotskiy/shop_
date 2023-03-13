from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from mall.models import *
from django.db.models import signals
from mall.tasks import CreationBasket


@transaction.atomic
@receiver(post_save, sender=Basket)
def basket_creation(sender, instance, created, signal, list_basket=None,
                    *args, **kwargs):
    if created:
        CreationBasket.make_basket()
    # if list_basket is None:
    #     list_basket = list(Basket.objects.filter(activate=True))
    # if created:
    #     if list_basket:
    #         CreationBasket.make_basket(list_basket=list_basket).delay()


# сообщение о ответе коментария
@transaction.atomic
@receiver(post_save, sender=Answer)
def user_s_answer(sender, instance, created, signal, list_basket=None,
                    *args, **kwargs):
    if created:
        CreationBasket.answer()


@transaction.atomic
@receiver(post_save, sender=Chat)
def message(sender, instance, created, signal, list_basket=None,
                    *args, **kwargs):
    if created:
        CreationBasket.message()


@transaction.atomic
@receiver(post_save, sender=User)
def create_balance(sender, instance, created, signal, *args, **kwargs):
    if created:
        Balance.objects.create(user=instance, balance=0)

# @transaction.atomic
# @receiver(post_save, sender=User)
# def register_account(sender, instance, created, signal, *args, **kwargs):
#     if not instance.is_verified:
#         send_verification_email.delay(instance.pk)
