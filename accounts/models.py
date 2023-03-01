from django.db import models
from django.contrib.auth.models import User
from product.models import ProductMainModel

GENDER_CHOICES = (
	    ("male", "Male"),
	    ("female", "Female"),
	    ("other", "Other")
	)

STATUS_CHOICES = (
	    ("pending", "Pending"),
	    ("completed", "Completed")
	)
class User(models.Model):
	phone_number = models.CharField(max_length=20, null=True, unique=True)
	email = models.EmailField(max_length=20)
	is_customer = models.BooleanField(default=False)
	is_admin = models.BooleanField(default=False)

	def __str__(self):
		return self.phone_number

class UserProfileModel(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	name = models.CharField(max_length=20)
	date_of_birth = models.DateField()
	gender = models.CharField(max_length=20, choices=GENDER_CHOICES, default="male")
	image = models.ImageField(upload_to='image/', default=None)

class UserLoginOtpModel(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	otp = models.IntegerField()
	active = models.BooleanField()

class UserCartProductModel(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)
	status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

class UserCartModel(models.Model):
	owner = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	products = models.ManyToManyField(UserCartProductModel)
	price = models.CharField(max_length=20)


