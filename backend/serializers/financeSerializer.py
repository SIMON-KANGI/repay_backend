from rest_framework import serializers
from backend.models.finance import Account, Categories, Transaction


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id', 'name', 'created_at']
        
        def create(self, validated_data):
            return Categories.objects.create(name=validated_data['name'])
        
class AccountSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)
    
    class Meta:
        model = Account
        fields = ['id', 'user', 'number', 'balance', 'category', 'password']
        
    def create(self, validated_data):
        user = validated_data['user']
        account = Account.objects.create(
            user=user,
            number=validated_data['number'],
            balance=validated_data['balance'],
            category=validated_data['category'],
            _password=validated_data['password']  # Password hashing is done automatically by Django
        )
        return account
    
class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'date', 'type', 'user', 'third_party', 'account', 'created_at']
    
    # Overriding validate method to add custom validation logic
    def validate(self, attrs):
        account = attrs.get('account')
        user = attrs.get('user')
        password = self.context['request'].data.get('password')  # Getting password from request data
        amount = attrs.get('amount')
        third_party = attrs.get('third_party')
        
        # Check if the account password matches
        if password and not account._password == password:
            raise serializers.ValidationError({'password': 'Invalid password.'})
        
        # Check if user is allowed to perform the transaction
        if not account.user == user:
            raise serializers.ValidationError({'account': 'This account does not belong to the user.'})

        # You can add more validations if needed (e.g., checking for sufficient balance)
        
        return attrs

    # Overriding create method to handle transaction creation
    def create(self, validated_data):
        # Extract the validated data
        user = validated_data['user']
        account = validated_data['account']
        amount = validated_data['amount']
        transaction_type = validated_data['type']
        third_party = validated_data.get('third_party', None)
        
        # Create the transaction instance
        transaction = Transaction.objects.create(
            amount=amount,
            date=validated_data['date'],
            type=transaction_type,
            user=user,
            account=account,
        )
        
        # If there is a third party, assign it
        if third_party:
            transaction.third_party = third_party
        
        # Save the transaction object
        transaction.save()

        return transaction