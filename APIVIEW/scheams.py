import coreapi
import coreschema

from rest_framework import schemas
from rest_framework.schemas import ManualSchema
from rest_framework.schemas.openapi import AutoSchema
from drf_yasg import openapi

bill_body = openapi.Schema(
        type=openapi.TYPE_OBJECT,
        responses={200: 'OK'},
        properties={
            'customer_name': openapi.Schema(type=openapi.TYPE_STRING),
            'Phone_number': openapi.Schema(type=openapi.TYPE_STRING),
            'Item_Name': openapi.Schema(type=openapi.TYPE_STRING),
            'MRP': openapi.Schema(type=openapi.TYPE_STRING),
            'Item_discount': openapi.Schema(type=openapi.TYPE_STRING),
            'GST': openapi.Schema(type=openapi.TYPE_STRING),
            'quantity': openapi.Schema(type=openapi.TYPE_STRING),
            
        }
    )