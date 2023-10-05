from django.db import models

# Create your models here.

class Product(models.Model):
    category = models.CharField(max_length=30, default="")
    subCategory = models.CharField(max_length=20, default="")
    product_id = models.AutoField
    product_name = models.CharField(max_length=50, default="")
    product_desc = models.CharField(max_length=300, default="")
    product_image = models.ImageField(upload_to="shop/images", default="")
    price = models.IntegerField(default=0)
    pub_date = models.DateField()

    def __str__ (self):
        return self.product_name
    
class TopDeal(models.Model):
    deals_id = models.AutoField
    deals_name = models.CharField(max_length=50, default="")
    deals_desc = models.CharField(max_length=300, default="")
    deals_image = models.ImageField(upload_to="shop/deals", default="")
    deals_price = models.IntegerField(default=0)

    def __str__ (self):
        return self.deals_name
    

class Contact(models.Model):
    mssg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    mssg = models.CharField(max_length=3000, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default=0)

    def __str__ (self):
        return self.name
    

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000, default="")
    name = models.CharField(max_length=90, default="")
    email = models.CharField(max_length=50, default="")
    phone = models.IntegerField(default=0)
    amount = models.IntegerField(default=0)
    address = models.CharField(max_length=100, default="")
    zip_code = models.CharField(max_length=7)
    city = models.CharField(max_length=50, default="")
    state = models.CharField(max_length=50, default="")
    mssg = models.CharField(max_length=500, default="")

    def __str__ (self):
        return self.name


class Coupon(models.Model):
    coupon_code = models.CharField(max_length = 6)
    discount_price = models.IntegerField(default="0")

    def __str__ (self):
        return self.coupon_code


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."