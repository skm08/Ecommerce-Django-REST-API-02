from django.db import models


class Category(models.Model):
    title=models.CharField(max_length=256,unique=True)
    slug=models.SlugField(unique=True)
    featured=models.BooleanField(default=False)
    created_date=models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['title']

    def __str__(self) -> str:
        return self.title
    
class Product(models.Model):
    category=models.ForeignKey(Category,related_name='products',on_delete=models.CASCADE)
    title=models.CharField(max_length=256,unique=True)
    slug=models.SlugField(unique=True)
    featured=models.BooleanField(default=False)
    thumbnail=models.URLField()
    price=models.DecimalField(max_digits=8, decimal_places=2)
    description=models.TextField(null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    updated_date=models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title