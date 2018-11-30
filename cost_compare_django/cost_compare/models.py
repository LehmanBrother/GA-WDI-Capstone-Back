from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Agency(models.Model):
	name = models.CharField(max_length=128)
	agency_id = models.IntegerField(default=0)
	budget_authority_amount = models.FloatField()
	budget_total = models.FloatField()
	budget_pct = models.FloatField()

	def __str__(self):
		return self.name

class Federal_Account(models.Model):
	name = models.CharField(max_length=128)
	account_id = models.IntegerField(default=0)
	amount = models.FloatField()
	parent = models.ForeignKey('Agency', on_delete=models.CASCADE, related_name="federal_accounts")

	def __str__(self):
		return self.name

class Consumer_Reference(models.Model):
	name = models.CharField(max_length=128)
	price = models.FloatField()
	user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="consumer_references")

	def __str__(self):
		return self.name

class Agency_Raw(models.Model):
	name = models.CharField(max_length=128, default="no name")
	agency_id = models.CharField(max_length=4)
	amount = models.FloatField(default=0)
	code = models.CharField(max_length=4, default="000")
	category = models.CharField(max_length=32, default="agency")

	def __str__(self):
		return self.name

class Federal_Account_Raw(models.Model):
	name = models.CharField(max_length=256)
	account_id = models.IntegerField(default=0)
	account_number = models.CharField(max_length=16)
	code = models.CharField(max_length=4, default=0)
	amount = models.FloatField()
	category = models.CharField(max_length=32, default="federal_account")

	def __str__(self):
		return self.name

class List_Agency_Raw(models.Model):
	cgac_code = models.CharField(max_length=4)
	name = models.CharField(max_length=256)
	toptier_agency_id = models.IntegerField(default=0)

	def __str__(self):
		return self.name

class Account_Key(models.Model):
	federal_account_id = models.IntegerField(default=0)
	federal_account_name = models.CharField(max_length=256)
	agency_id = models.IntegerField(default=0)

	def __str__(self):
		return self.federal_account_name