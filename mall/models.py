import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from rest_framework.exceptions import ValidationError
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserAccountManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Email address must be provided')

        if not password:
            raise ValueError('Password must be provided')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    objects = UserAccountManager()

    email = models.EmailField('email', unique=True, blank=False, null=False)
    username = models.CharField("username", max_length=122, blank=False, null=False)
    full_name = models.CharField('full name', blank=True, null=True, max_length=400)
    is_staff = models.BooleanField('staff status', default=False)
    is_active = models.BooleanField('active', default=True)
    is_verified = models.BooleanField('verified', default=False)  # Add the `is_verified` flag
    verification_uuid = models.UUIDField('Unique Verification UUID', default=uuid.uuid4)

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def __unicode__(self):
        return self.email


class Name(models.Model):
    RATE_CHOICES = (
        (1, 'Phone'),
        (2, 'Computer'),
        (2, 'Fruit'),
        (2, 'shoes'),
    )
    name = models.CharField(max_length=120)
    image = models.ImageField()
    type_function = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, max_length=10, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    @receiver(post_save, sender=User)
    def create_user_balance(sender, instance, created, **kwargs):
        if created:
            Balance.objects.create(user=instance, balance=0)


class Product(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    thing = models.ForeignKey("Name", null=True, blank=True, on_delete=models.CASCADE,
                              related_name="things", related_query_name="things")
    quantity = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, max_length=10, null=True, blank=True)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.thing.name}'

    def save(self, *args, **kwargs):
        self.total_price = self.quantity * self.thing.price
        super(Product, self).save(*args, **kwargs)


class Basket(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    name = models.ManyToManyField("Product", related_name="pizza", related_query_name="pizza")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, max_length=10, default=0)
    activate = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user}:{self.total_amount}'


class Balance(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, max_length=10, null=True, blank=True, default=0)

    def __str__(self):
        return f"{self.user}:{self.balance}"


class ListReview(models.Model):
    thing = models.ForeignKey("Name", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.thing}"

    def review(self):
        return []


class Review(models.Model):
    RATE_CHOICES = (
        (1, 'Bad'),
        (2, 'SO-SO'),
        (2, 'GOOD'),
        (2, 'Perfect'),
    )
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    product = models.ForeignKey("Name", on_delete=models.CASCADE,
                                related_name="product_basket", related_query_name="product_basket")
    type_function = models.PositiveIntegerField(choices=RATE_CHOICES, null=True)
    text = models.TextField(max_length=120, null=False, blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}:{self.text}"

    # @receiver(post_save, sender=User)
    # def create_user_balance(sender, instance, created, **kwargs):
    #     if created:
    #         review.delay()


class Author(models.Model):
    author = models.ForeignKey("User", blank=True, null=True, on_delete=models.CASCADE)
    email = models.EmailField(max_length=120)

    def __str__(self):
        return f"{self.author}:{self.email}"


class ListProduct(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self):
        return f"{self.name}"

    def phone(self):
        phone = list(Name.objects.filter(type_function=1).values())
        return phone

    def computer(self):
        product = Name.objects.filter(type_function=2).values()
        return product

    def fruit(self):
        product = Name.objects.filter(type_function=3).values()
        return product

    def shoes(self):
        product = Name.objects.filter(type_function=4).values()
        return product


# ответ на комменатрий


class Answer(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    review = models.ForeignKey("Review", null=False, on_delete=models.CASCADE)
    answer = models.TextField(max_length=120, null=False)
    activate = models.BooleanField(default=True)


# сообщение о том что ответил на ваш коментарий


class UserMail(models.Model):
    user = models.ForeignKey("User", on_delete=models.CASCADE)
    mail = models.TextField(max_length=120)
    text = models.CharField(max_length=200)


# class MyFriends(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     my_friends = models.ManyToManyField(User, related_name="my_friend", related_query_name="my_friend")
#
#     def __str__(self):
#         return f"{self.user} : {self.my_friends}"


class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=120, null=False, blank=False)
    friend = models.ForeignKey(User, max_length=200, null=False, blank=False, on_delete=models.CASCADE,
                               related_name="friend", related_query_name="friend")
    activate = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} : {self.message} to the {self.friend}"

    # def answer(self, request):
    #     user = request.user
    #     chat = Chat.objects.filter(frend_id=user.id)
    #     return chat
