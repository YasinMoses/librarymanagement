from django.urls import path, include
from rest_framework.routers import DefaultRouter
from library.views import BookViewSet, MemberViewSet, TransactionViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'members', MemberViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
