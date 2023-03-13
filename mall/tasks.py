from __future__ import absolute_import, unicode_literals

import logging

from celery import shared_task
from mall.models import Name, Review, Basket, Balance, UserMail, Answer, Chat
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import OutstandingToken
from django.core.mail import send_mail
from django.urls import reverse
from rest_framework.authtoken.models import Token
# можно не отнимать изначально баланс а сделать модель для потверждения и после потверждения
# создать уже функцию для разности баланса


class CreationBasket:
    # для создании корзины и изменения его баланса только вот стоимость вычислять нужно после создания
    # потому что нельзя обращаться к many to many во время создания, а жалко !!!!!
    @classmethod
    def make_basket(cls):
        list_basket = list(Basket.objects.filter(activate=True))
        for one_basket in list_basket:
            balance = Balance.objects.filter(user=one_basket.user).first()
            for i in one_basket.name.all():
                price = 0
                price += i.total_price * i.quantity
                if price < balance.balance:
                    one_basket.total_amount += i.total_price * i.quantity
                    balance.balance -= i.total_price * i.quantity
                    i.activate = False
                    one_basket.activate = False
                    one_basket.save()
                    balance.save()
                    i.save()
                else:
                    one_basket.activate = False
                    one_basket.save()

    # создание сообщения для комментария либо можно путем писбма на почту из репозитория treiding(письмо на email)
    @classmethod
    def answer(cls):
        answer = list(Answer.objects.filter(activate=True))
        for one_answer in answer:
            review = list(Review.objects.filter(id=one_answer.review_id))
            review = review[0]
            UserMail.objects.create(user=review.user, mail=f"тебе ответил на комментарий{one_answer.user}",
                                    text=one_answer.answer)
            one_answer.activate = False
            one_answer.save()
    # на подобии оправки сообщения и для отображения что пришло сообщение
    # нужно желательно чтобы видель не только свои но и отпрааленые но для return нужно только одно
    # также желательно длбавить поле дата времени для отображенния времени когла оно было отправлено
    @classmethod
    def message(cls):
        chat = list(Chat.objects.filter(activate=True))
        for message in chat:
            UserMail.objects.create(user=message.user, mail=f"you got one message at {message.user}",
                                    text=message.message)
            message.activate = False
            message.save()
