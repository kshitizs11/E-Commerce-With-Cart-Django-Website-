from django.db import models

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300)
    category = models.CharField(max_length=50,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    image = models.ImageField(upload_to="shop/images",default="")
    pub_date = models.DateField()

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=5000,default="")
    email = models.CharField(max_length=50,default="")
    phone = models.CharField(max_length=50,default="")
    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id =  models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    name = models.CharField(max_length=500)
    email = models.CharField(max_length=500,default="")
    address = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=500,default="")
    state = models.CharField(max_length=500,default="")
    zip_code = models.CharField(max_length=500,default="")
    phone = models.CharField(max_length=500,default="")


class orderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."