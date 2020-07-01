from django.db import models

# Create your models here.
class bank(models.Model):
    ifsc=models.CharField(max_length=128,blank=True,null=True,default="")
    bank_id=models.CharField(max_length=128,blank=True,null=True,default="")
    branch=models.CharField(max_length=128,blank=True,null=True,default="")
    address=models.CharField(max_length=800,blank=True,null=True,default="")
    city=models.CharField(max_length=128,blank=True,null=True,default="")
    district=models.CharField(max_length=128,blank=True,null=True,default="")
    state=models.CharField(max_length=128,blank=True,null=True,default="")
    bank_name=models.CharField(max_length=128,blank=True,null=True,default="")
    

