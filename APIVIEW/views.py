from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from drf_yasg.utils import swagger_auto_schema
# from .schema import*
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 


"""Marketing person"""
class Marketing_ProfileAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            Marketing=Marketing_Profile.objects.get(id=id)
            serializer=Marketing_ProfileSerializer(Marketing)
            return Response({'msg':'Data Fetched', "data": serializer.data},status=status.HTTP_201_CREATED)

        Marketing=Marketing_Profile.objects.all()
        serializer=Marketing_ProfileSerializer(Marketing, many=True)
        return Response(serializer.data)

        # try:
        #      Marketing_Profile.objects.get(id=id)
        # except Marketing_Profile.DoesNotExist:
        #     raise Http404

        

    def post(self, request, format=None):
        serializer=Marketing_ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id=pk
        Marketing=Marketing_Profile.objects.get(pk=id)
        serializer=Marketing_ProfileSerializer(Marketing,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        Marketing=Marketing_Profile.objects.get(pk=id)
        serializer=Marketing_ProfileSerializer(Marketing,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id=pk
        Marketing=Marketing_Profile.objects.get(pk=id)
        Marketing.delete()
        return Response({'msg':' Data Deleted'})


""""Add_items"""
class Add_itemsAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            items=Add_items.objects.get(id=id)
            serializer=Add_itemsSerializer(items)
            return Response(serializer.data)

        items=Add_items.objects.all()
        # items=Add_items.objects.all()
        serializer=Add_itemsSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=Add_itemsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id=pk
        items=Add_items.objects.get(pk=id)
        serializer=Add_itemsSerializer(items,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        items=Add_items.objects.get(pk=id)
        serializer=Add_itemsSerializer(items,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id=pk
        items=Add_items.objects.get(pk=id)
        items.delete()
        return Response({'msg':' Data Deleted'})


"""Create_Bill"""
class Create_billAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            Bill=Create_bill.objects.get(id=id)
            serializer=Create_billSerializer(Bill)
            return Response(serializer.data)

        Bill=Create_bill.objects.all()
        serializer=Create_billSerializer(Bill, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=Create_billSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id=pk
        Bill=Create_bill.objects.get(pk=id)
        serializer=Create_billSerializer(Bill,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        Bill=Create_bill.objects.get(pk=id)
        serializer=Create_billSerializer(Bill,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id=pk
        Bill=Create_bill.objects.get(pk=id)
        Bill.delete()
        return Response({'msg':' Data Deleted'})

"""Profile"""
class ProfileAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            Profiles=Profile.objects.get(id=id)
            serializer=ProfileSerializer(Profiles)
            return Response(serializer.data)

        Profiles=Profile.objects.all()
        serializer=ProfileSerializer(Profiles, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id=pk
        Profiles=Profile.objects.get(pk=id)
        serializer=ProfileSerializer(Profiles,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        Profiles=Profile.objects.get(pk=id)
        serializer=ProfileSerializer(Profiles,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id=pk
        Profiles=Profile.objects.get(pk=id)
        Profiles.delete()
        return Response({'msg':' Data Deleted'})


"""Catelog"""
class CatelogAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            Catelogs=Catelog.objects.get(id=id)
            serializer=CatelogSerializer(Catelogs)
            return Response(serializer.data)

        Catelogs=Catelog.objects.all()
        serializer=CatelogSerializer(Catelogs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=CatelogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id=pk
        Catelogs=Catelog.objects.get(pk=id)
        serializer=CatelogSerializer(Catelogs,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        Catelogs=Catelog.objects.get(pk=id)
        serializer=CatelogSerializer(Catelogs,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id=pk
        Catelogs=Catelog.objects.get(pk=id)
        Catelogs.delete()
        return Response({'msg':' Data Deleted'})
   
"""Sales_team"""
class Sales_teamAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            Sales=Sales_team.objects.get(id=id)
            serializer=Sales_teamSerializer(Sales)
            return Response(serializer.data)

        Sales=Sales_team.objects.all()
        serializer=Sales_teamSerializer(Sales, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=Sales_teamSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id=pk
        Sales=Sales_team.objects.get(pk=id)
        serializer=Sales_teamSerializer(Sales,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        Sales=Sales_team.objects.get(pk=id)
        serializer=Sales_teamSerializer(Sales,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id=pk
        Sales=Sales_team.objects.get(pk=id)
        Sales.delete()
        return Response({'msg':' Data Deleted'})

"""Customer_Profile"""
class Customer_ProfileAPI(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            Profile=Customer_Profile.objects.get(id=id)
            serializer=Customer_ProfileSerializer(Profile)
            return Response(serializer.data)

        Profile=Customer_Profile.objects.all()
        serializer=Customer_ProfileSerializer(Profile, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer=Customer_ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        id=pk
        Profile=Customer_Profile.objects.get(pk=id)
        serializer=Customer_ProfileSerializer(Profile,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Complete Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk, format=None):
        id=pk
        Profile=Create_bill.objects.get(pk=id)
        serializer=Customer_ProfileSerializer(Profile,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partial Data Updated'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        id=pk
        Profile=Customer_Profile.objects.get(pk=id)
        Profile.delete()
        return Response({'msg':' Data Deleted'})
   
