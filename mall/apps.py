from django.apps import AppConfig


class MallConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mall'

    def ready(self):
        from django.db.models.signals import post_save
        from mall.signals import basket_creation, user_s_answer, message, create_balance
        from mall.models import User
        post_save.connect(basket_creation, sender=User)
        post_save.connect(user_s_answer, sender=User)
        post_save.connect(message, sender=User)
        post_save.connect(create_balance, sender=User)
