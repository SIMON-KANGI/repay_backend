from django.db import models
from backend.models.user import User
from django.contrib.auth.hashers import make_password
class Categories(models.Model):
    name = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        app_label = 'backend'
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.IntegerField()
    _password = models.CharField(max_length=255)  # Private password field
    balance = models.FloatField(default=50000, null=True, blank=True)
    currency = models.CharField(max_length=255, default='KSH')
    category = models.ForeignKey(Categories, on_delete=models.CASCADE, related_name='accounts')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='accounts')
    created_at = models.DateTimeField(auto_now_add=True)

    def to_dict(self):
        return {
            'id': self.id,
            'number': self.number,
            'balance': self.balance,
            'currency': self.currency,
            'category': self.category.name,  # Access the category name directly
            'created_at': self.created_at.strftime('%Y-%m-%d %H:%M:%S'),
        }
        
    def set_password(self, raw_password):
        self._password = make_password(raw_password)

    # def check_password(self, raw_password):
    #     return check_password(raw_password, self._password)
    def received(self, amount):
        self.balance += amount
        return self.balance
    
    def sent(self, amount):
        if self.balance < amount:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        return self.balance
    
    def withdraw(self, amount):
        if self.balance < amount:
            raise ValueError('Insufficient funds')
        self.balance -= amount
        return self.balance
    
    class Meta:
        verbose_name_plural = "Accounts"
        app_label = 'backend'
      


class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('sent', 'Sent'),
        ('received', 'Received'),
    )

    amount = models.IntegerField()
    date = models.DateTimeField()
    type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='transactions')
    third_party = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='third_party_transactions')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    created_at = models.DateTimeField(auto_now_add=True)

    
    def to_dict(self):
        account_one = self.account  # Access account details directly via ForeignKey
        receiver = self.third_party  # Access third party (receiver) details via ForeignKey

        return {
            'id': self.id,
            'amount': self.amount,
            'date': self.date.strftime('%Y-%m-%d %H:%M:%S'),
            'type': self.type,
            'user_id': self.user.id,
            'thirdParty_id': self.third_party.id if self.third_party else None,
            'account_id': self.account.id,
            'accountOne': account_one.number,
            'accountTwo': receiver.username if receiver else None,
            'accountTwoName': receiver.email if receiver else None,
        }

    class Meta:
        verbose_name_plural = "Transactions"
        app_label = 'backend'