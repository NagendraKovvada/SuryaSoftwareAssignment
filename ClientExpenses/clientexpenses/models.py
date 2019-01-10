from django.db import models
import uuid

# Create your models here.

class Client(models.Model):
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	name = models.CharField(max_length=250)
	def __str__(self):
		return "{0}".format(self.name)

class Expense(models.Model):
	CURRENCY_CHOICES = (
	(u"USD", u"$"),
	(u"EUR", u"&euro;"),
	(u"INR", u"&#8377;"),
)
	uuid = models.UUIDField(default=uuid.uuid4, editable=False)
	expense_timestamp = models.DateTimeField(blank=True, null=True,auto_now_add=True)
	client = models.ForeignKey('Client',
                                 related_name='client_expense',
                                 blank=True,
                                 null=True,
                                 on_delete=models.SET_NULL)	
	currency = models.CharField(
		max_length=3,
		choices=CURRENCY_CHOICES,
		default='INR',
		blank=True
	)
	amount = models.DecimalField(decimal_places=1, max_digits=4, default=0)
	title = models.CharField(max_length=100,blank=True, null=True)
	description = models.CharField(max_length=100,blank=True, null=True)
	def clean(self):
		if self.amount and self.currency:
			return "{0} at {1} ".format(self.amount, self.currency)

	def __str__(self):
		return "{0} at {1} ".format(self.client,self.title)