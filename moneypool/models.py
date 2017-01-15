from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Masterprofile(models.Model):
    group_id = models.IntegerField(primary_key=True)
    balance = models.IntegerField(null=True)

    def __str__(self):
        return "Masterprofile: {}".format(self.group_id)

@python_2_unicode_compatible
class Profile(models.Model):
    phone_number = models.IntegerField(primary_key=True)
    group_id = models.IntegerField()
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    relationship = models.CharField(max_length=20)
    mail_id = models.CharField(max_length=50)
    address_1 = models.CharField(max_length=50)
    address_2 = models.CharField(max_length=50)
    pincode = models.IntegerField()
    custom_filter = models.IntegerField(null=True,blank=True)
    customer_type = models.IntegerField(null=True,blank=True)
    vendor_type = models.IntegerField(null=True,blank=True)
    card_number = models.IntegerField(null=True,blank=True)
    name_on_card = models.CharField(null= True,blank=True,max_length=100)
    expiry = models.CharField(null= True,blank=True,max_length=20)

    def __str__(self):
        return "Profile: {}".format(self.phone_number)

@python_2_unicode_compatible
class Transaction(models.Model):
    from_user = models.IntegerField()
    to_user = models.IntegerField()
    amount = models.IntegerField()
    transaction_id = models.AutoField(primary_key=True)
    group_id = models.IntegerField()
    timestamp = models.CharField(max_length=100)
    transaction_type = models.CharField(null= True,max_length=100)
    location = models.CharField(null=True,max_length=100)

    def __str__(self):
        return "Transaction: {}".format(self.transaction_id)
