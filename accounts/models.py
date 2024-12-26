from django.db import models
from django.contrib.auth.models import User
from .constants import ACCOUNT_TYPE, GENDER_TYPE
from django.utils.timezone import now
# django amaderke built in user niye kaj korar facility dey


class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPE,null=True, blank=True)
    account_no = models.IntegerField(unique=True, null=True, blank=True) # account no duijon user er kokhono same hobe na
    birth_date = models.DateField(default=now, null=True, blank=True)
    gender = models.CharField(max_length=10, choices=GENDER_TYPE, null=True, blank=True)
    initial_deposite_date = models.DateField(default=now, null=True, blank=True)    
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2, null=True, blank=True) # ekjon user 12 digit obdi taka rakhte parbe, dui doshomik ghor obdi rakhte parben 1000.50
    def __str__(self):
        return str(self.account_no)
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length= 100, null=True, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return str(self.user.email)
    