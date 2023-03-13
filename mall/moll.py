import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "store_price.settings")
import django

django.setup()

from mall.models import *

# x = 0
# price = Basket.objects.all().first()
# for i in price.name.all():
#     x += i.total_price
#     price.total_amount = x
#     print(price.total_amount)
p = Name.objects.get(pk=1)
s = Review.objects.all()
for i in s:
    if p.id == i.product_id:
        g = list(Review.objects.filter(product_id=p.id))
        print(g)




# @receiver(post_save, sender=Basket)
#     def create_user_balance(sender, instance, created, **kwargs):
#         if created:
#             basket = Basket.objects.filter(user=instance.user).first()
#             product = list(Product.objects.filter(user=instance.user))
#             for amount in product:
#                 if amount in basket.name.all():
#                     basket.total_amount += amount.total_price
#                     basket.save()
#                 else:
#                     continue