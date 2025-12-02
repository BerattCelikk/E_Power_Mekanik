from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200,verbose_name="Product Title")
    
    description = models.TextField(verbose_name="Product Description")
    
    image = models.ImageField(upload_to='products/', verbose_name="Product Image",blank=True,null=True)
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    
    def __str__(self):
        return self.title
    
    class Meta : 
        verbose_name = "Product"
        verbose_name_plural = "Products"