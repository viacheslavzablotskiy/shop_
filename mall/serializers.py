from mall.models import *

from rest_framework import serializers


class NameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Name
        fields = "__all__"


class ListReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = ListReview
        fields = "__all__"


class ProductSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Product
        fields = "__all__"


class BasketSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Basket
        fields = ("user", "name", "total_amount", "id",)


class BalanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Balance
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Review
        fields = '__all__'


class AnswerSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Answer
        fields = "__all__"


class MailSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = UserMail
        fields = "__all__"


class AuthorSerializer(serializers.ModelSerializer):
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Author
        fields = '__all__'


class ListProductSerializer(serializers.ModelSerializer):
    phone = serializers.ListField(child=serializers.ReadOnlyField(read_only=True))
    computer = serializers.ListField(child=serializers.ReadOnlyField(read_only=True))
    fruit = serializers.ListField(child=serializers.ReadOnlyField(read_only=True))
    shoes = serializers.ListField(child=serializers.ReadOnlyField(read_only=True))

    class Meta:
        model = ListProduct
        fields = ("id", "name", "phone", "computer", "shoes", "fruit",)


class ChatSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Chat
        fields = "__all__"


# class MyFriendsSerializers(serializers.ModelSerializer):
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#
#
#     class Meta:
#         model = MyFriends
#         fields = "__all__"
