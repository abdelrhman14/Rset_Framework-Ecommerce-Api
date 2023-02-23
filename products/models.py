from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save


class Category(models.Model):
    CATname = models.CharField(max_length=50,null=True,blank=True,verbose_name='Category Name')
    CATdescription = models.TextField(null=True,blank=True,verbose_name='Description')
    CATparent = models.ForeignKey('self',limit_choices_to={'CATparent__isnull':True},null=True,blank=True,verbose_name='Category Parent',on_delete=models.CASCADE)
    image = models.ImageField(null=True,blank=True,verbose_name='Image')
    slug = models.SlugField(null=True,blank=True,verbose_name='Slug')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.CATname)
        return super(Category,self).save(*args, **kwargs)

    
    def get_category_url(self):
       return reverse("category", kwargs={'slug': self.slug})


    def __str__(self):
        return str(self.CATname)

class Products(models.Model):
    category = models.ForeignKey('Category',on_delete=models.CASCADE,verbose_name='Category')
    name = models.CharField(max_length=250,null=True,blank=True,verbose_name='Product Name')
    PRdescription = models.TextField(verbose_name=('Description'),null=True,blank=True)
    PRinformation = models.TextField(verbose_name=('Information'),null=True,blank=True)
    pr_code = models.CharField(max_length=250,null=True,blank=True,verbose_name='Product Code')
    price = models.FloatField(null=True,blank=True,verbose_name='Price')
    PRdiscount_price = models.FloatField(null=True,blank=True,verbose_name='Discount Price')
    PRstate = models.BooleanField(null=True,blank=True,verbose_name='is_active')
    PRimage = models.ImageField(verbose_name='Image',null=True,blank=True)
    PRnp_available = models.IntegerField(null=True,blank=True,verbose_name='Number Available')
    PRnew = models.BooleanField(default=True,verbose_name='New | Not')
    PRbestseller = models.BooleanField(default=False,verbose_name='Bestseller | Not')
    slug = models.SlugField(unique=True,blank=True, null=True,verbose_name='Slug')
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='created_at')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='updated_at')
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
    
    def save(self,*args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super(Products,self).save(*args, **kwargs)

    def get_product_details_url(self):
       return reverse("product_details", kwargs={'slug': self.slug})
 
    def get_add_to_cart_url(self):
        return reverse("add_to_cart", kwargs={
            'slug': self.slug
        })

    def get_remove_single_item_url(self):
        return reverse("remove_single_item", kwargs={
            'slug': self.slug
        })

    def discount_number(self):
        number = self.price - self.PRdiscount_price
        return number
    def discount_percentage(self):
        total =  (1 - self.PRdiscount_price / self.price) * 100
        return total
    
    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='created_at')

    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'


class Cart(models.Model):
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE,related_name='items')
    product = models.ForeignKey(Products, on_delete=models.CASCADE,related_name='cartitems')
    qunatity = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True,verbose_name='created_at')

    class Meta:
        verbose_name = 'Cart'
        verbose_name_plural = 'Cart'

    def get_total_item_price(self):
        return self.qunatity * self.product.price

    def get_total_discount_item_price(self):
        return self.qunatity * self.product.PRdiscount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.product.PRdiscount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


    def __str__(self):
        return f"{self.qunatity} of {self.product.name}"



    


    


