from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True) # hold in db_index and unique

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name  # here return the name of the model in every places

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])  # after submitting form the redirect this url
    # in shop app the url name product_list_by_category takes parameter slug,this slug is same as url file slug


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE) # here category is the primary key,so in a category there are so many products
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/', blank=True) # image can be blank
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2) # using decimal field instead of using float field for avoiding rounding issues
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True) # store when the object is created
    updated = models.DateTimeField(auto_now=True)   # store when the object is updated

    class Meta:
        ordering = ('-created',) # ordering the created time
        index_together = (('id', 'slug'),) # for indexing,both fields perform together for imporove query

    def __str__(self):
        return self.name  # here return the name of the product in every case

    def get_absolute_url(self): # after submitting then redirect to product detail page of shop app
        return reverse('shop:product_detail', args=[self.id, self.slug]) # in product_detail url it takes id and slug





