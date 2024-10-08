from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views.userView import UserViewSet
from .views.auth import CustomTokenObtainPairView
from .views.financeView import FinanceViewSet, CategoryViewSet, TransactionViewSet
from rest_framework_simplejwt.views import TokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'accounts', FinanceViewSet , basename='account')
router.register(r'categories', CategoryViewSet , basename='category')
router.register(r'transactions', TransactionViewSet, basename='transaction')
urlpatterns = [
    path('', include(router.urls)),
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Login endpoint
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),    # Token refresh endpoin # Separate path for token
]
