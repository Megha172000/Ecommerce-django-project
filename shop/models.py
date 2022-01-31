from django.db import models


class product(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category = models.CharField(max_length=50, default="")
    sub_category = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    product_desc=models.CharField(max_length=300)
    pub_date=models.DateField()
    image = models.ImageField(upload_to="shop/image", default="")

    def __str__(self):
        return self.product_name

