from django.db import models

class Category(models.Model):
    parent = models.ForeignKey('self', blank=True, null=True, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='categories/')
    is_enable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        db_table = 'categories'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        
    def __str__(self):
        return self.title
class File(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    file = models.FileField(upload_to='files/%Y/%m/%d/')
    is_enable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'files'
        verbose_name = 'File'
        verbose_name_plural = 'Files'
        
    def __str__(self):
        return self.title
    
class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    avatar = models.ImageField(blank=True, upload_to='products/')
    category = models.ManyToManyField(Category, blank=True)
    file = models.ManyToManyField(File, blank=True)
    is_enable = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.title

