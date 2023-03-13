from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Subquery
from django.http import HttpResponse
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from . import *
from .models import *
from .permissions import IsAdminOrReadOnly
from .serializers import *


class NameProduct(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Name.objects.all()
    serializer_class = NameSerializers
    permission_classes = (IsAuthenticated,
                          )

    # def get_queryset(self):
    #     user = self.request.user
    #     return Name.objects.filter(user=user.id)


class ListReviewProduct(mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = ListReview.objects.all()
    serializer_class = ListReviewSerializers
    permission_classes = (IsAuthenticated,
                          )
    # def get_queryset(self):
    #     user = self.request.user
    #     return Name.objects.filter(user=user.id)


class SelfProduct(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    permission_classes = (IsAuthenticated,
                          )

    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(user=user.id)


class SelfBasket(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = (IsAuthenticated,
                          )

    def get_queryset(self):
        user = self.request.user
        return Basket.objects.filter(user=user.id)


class SelfBalance(mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    queryset = Balance.objects.all()
    serializer_class = BalanceSerializer
    permission_classes = (IsAuthenticated,
                          )

    def get_queryset(self):
        user = self.request.user
        return Balance.objects.filter(user=user.id)


class SelfReview(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (IsAuthenticated,
                          )

    def get_queryset(self):
        user = self.request.user
        return Review.objects.filter(user=user.id)


class SelfAnswer(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
                 viewsets.GenericViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializers
    permission_classes = (IsAuthenticated,
                          )


class SelfMail(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin,
               viewsets.GenericViewSet):
    queryset = UserMail.objects.all()
    serializer_class = MailSerializers
    permission_classes = (IsAuthenticated,
                          )

    def get_queryset(self):
        user = self.request.user
        return UserMail.objects.filter(user=user.id)


class SelfAuthor(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated, IsAdminOrReadOnly,
                          )


class SelfListProduct(mixins.ListModelMixin,
                      mixins.DestroyModelMixin,
                      viewsets.GenericViewSet):
    queryset = ListProduct.objects.all()
    serializer_class = ListProductSerializer
    permission_classes = (IsAuthenticated,
                          )


class SelfChat(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializers
    permission_classes = (IsAuthenticated,
                          )

    def get_queryset(self):
        user = self.request.user
        return Chat.objects.filter(friend_id=user.id)

        # for message in chat:
        #     if message.friend_id == user.id:
        #         user_message = message.user
        #         return Chat.objects.filter(user=user_message)
        #     else:
        #         return Chat.objects.filter(user=user.id)


    # def get_queryset(self):
    #     user = self.request.user
    #     friends = MyFriends.objects.all()
    #     for one in friends:
    #         chat = Chat.objects.all()
    #         for one_message in chat:
    #             if one_message.id in one.my_friends.all():
    #                 return Chat.objects.filter(user=user.id) and Chat.objects.filter(user=one.user)
    #             else:
    #                 return Chat.objects.filter(user=user.id) and Chat.objects.filter(user=one_message.user)


# class SelfMyFriends(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
#     queryset = MyFriends.objects.all()
#     serializer_class = MyFriendsSerializers
#     permission_classes = (IsAuthenticated, IsAdminOrReadOnly,
#                           )
