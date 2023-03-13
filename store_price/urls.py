from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView, TokenRefreshView


from mall.views import *
from django.contrib import admin
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r"name", NameProduct),
router.register(r"product", SelfProduct),
router.register(r"basket", SelfBasket),
router.register(r"review", SelfReview)
router.register(r"list_product", SelfListProduct),
router.register(r"balance", SelfBalance),
router.register(r"author", SelfAuthor),
router.register(r"list_review", ListReviewProduct),
router.register(r"answer", SelfAnswer)
router.register(r"mail", SelfMail),
router.register(r"chat", SelfChat),

# router.register(r"my_friends", SelfMyFriends),

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('djoser.urls')),
    path('api/login/', include("rest_framework.urls")),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
urlpatterns += router.urls
