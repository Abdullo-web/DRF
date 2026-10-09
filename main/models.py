from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    title = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    
