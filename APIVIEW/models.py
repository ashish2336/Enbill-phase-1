from django.db import models

class Marketing_Profile(models.Model):  
    Phone_number= models.CharField(
    max_length=10,null=True, unique=True, blank=True, error_messages={'unique': "This mobile no is already registered."})  
    Name= models.CharField(max_length=60)
    Employee_no= models.CharField(max_length=6)
    Address= models.CharField(max_length=60)
    Pincode=models.CharField(max_length=60)
    State=models.CharField(max_length=60)
    Town=models.CharField(max_length=60)
    City=  models.CharField(max_length=60)
    def __str__(self):
        return self.Name 

class Add_items(models.Model):
    Item_name = models.CharField(max_length=60)
    Price = models.CharField(max_length=60)
    GST_percentage= models.CharField(max_length=60,choices=[('1', '0%'), ('2', '5%'),('3', '12%'),('4', '18%'),('5', '28%')])
    def __str__(self):
        return self.Item_name

class Create_bill(models.Model):
    Bill_no=models.CharField(max_length=60,default=1,)
    Time= models.TimeField("Time", max_length=255, null=True, blank=True)
    Date=models.DateField("Date", max_length=25, null=True, blank=True)
    Toal_Amt=models.CharField(max_length=60)
    Item_Name=models.CharField(max_length=60)
    Phone_number=models.CharField(max_length=60)
    
    def __str__(self):
        return self.Item_Name

class Signup(models.Model):
    Phone_number= models.CharField(
    max_length=10,null=True, unique=True, blank=True, error_messages={'unique': "This mobile no is already registered."})
    OTP= models.CharField(max_length=60,blank=True)
    def __str__(self):
        return self.Phone_number

class Profile(models.Model):
    Name= models.CharField(max_length=60)
    Shop_name = models.CharField(max_length=60)
    Address= models.CharField(max_length=60)
    Pincode=models.CharField(max_length=60)
    State=models.CharField(max_length=60)
    Town=models.CharField(max_length=60)
    City=  models.CharField(max_length=60)
    country=models.CharField(max_length=60)
    signup = models.ForeignKey(
        Signup,
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.Name

class Catelog(models.Model):
    Item_name= models.CharField(max_length=60)
    Item_pic = models.FileField(null=False)
    Item_selling_price= models.FloatField(max_length=60)
    Item_discount=models.FloatField(max_length=60)

    def __str__(self):
        return self.Item_name

class Sales_team(models.Model):
    Sales_person_Name= models.CharField(max_length=60)
    Sales_person_Identity = models.FileField(null=False)
    Sales_person_Phone_number = models.CharField(
    max_length=10, unique=True, null=True, blank=True, error_messages={'unique': "This mobile no is already registered."})
    Sales_person_Image = models.FileField(null=False)
   
    def __str__(self):
        return self. Sales_person_Name

class Customer_Profile(models.Model):
    Name=models.CharField(max_length=60)
    Phone_number= models.CharField(
    max_length=10, unique=True, null=True, blank=True, error_messages={'unique': "This mobile no is already registered."})
    Pincode=models.CharField(max_length=60)
    Customer_pic = models.FileField(null=False)
    
    
    def __str__(self):
        return self.Name