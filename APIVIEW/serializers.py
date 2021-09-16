from rest_framework import serializers
from .models import *

class Marketing_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marketing_Profile
        fields =['id','Phone_number','Name','Employee_no','Address','Pincode','State','Town']
        
class Add_itemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Add_items
        fields =['id','Item_name','Price','GST_percentage']

class Create_billSerializer(serializers.ModelSerializer):
    class Meta:
        model = Create_bill
        fields = ['id','Bill_no','Time','Date','Toal_Amt','Item_Name','Phone_number']

class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signup
        fields = ['id','Phone_number','OTP']   

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','Name','Shop_name','Address','Pincode','State','Town','City','country'] 

class CatelogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catelog
        fields = ['id','Item_name','Item_pic','Item_selling_price','Item_discount'] 

class Sales_teamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales_team
        fields = ['id','Sales_person_Name','Sales_person_Identity','Sales_person_Phone_number','Sales_person_Image']   

class Customer_ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer_Profile
        fields =    ['id','Name','Phone_number','Pincode','Customer_pic']