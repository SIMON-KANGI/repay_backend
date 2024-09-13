from rest_framework import viewsets
from rest_framework.permissions import  AllowAny
from backend.serializers.financeSerializer import AccountSerializer, CategoriesSerializer, TransactionSerializer
from backend.models.finance import Account,Categories, Transaction
from rest_framework.authentication import TokenAuthentication 
class FinanceViewSet(viewsets.ModelViewSet):
    queryset=Account.objects.all()
    serializer_class=AccountSerializer
    permission_classes=[AllowAny]
    authentication_classes = [TokenAuthentication]
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Categories.objects.all()
    serializer_class=CategoriesSerializer
    permission_classes=[AllowAny]
    authentication_classes = [TokenAuthentication]
    
class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    permission_classes=[AllowAny]
    authentication_classes = [TokenAuthentication]