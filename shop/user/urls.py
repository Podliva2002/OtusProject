from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, CurrentUserView, UserRegistrationView

app_name = 'users'

router = DefaultRouter()
router.register(
    prefix=r'users',
    viewset=UserViewSet,
    basename= 'user',

)


urlpatterns = [
    path('current-user/', CurrentUserView.as_view(), name='current-user'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    *router.urls,
]
