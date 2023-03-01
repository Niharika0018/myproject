from django.db import models

class ProductMainModel(models.Model):
	title = models.CharField(max_length=20)
	description = models.CharField(max_length=20)
	unique_id = models.CharField(max_length=20, unique=True)
	price = models.CharField(max_length=20)

class ProductImageModel(models.Model):
	product = models.ForeignKey(ProductMainModel, on_delete=models.CASCADE)