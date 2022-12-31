from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework.views import APIView


# Create your views here.


@api_view(['GET'])
def children(request):
    childrens= Children.objects.all()
    serializer= ChildrenSerializer(childrens, many=True)
    return Response({'status': 200, 'payload': serializer.data})


class PeopleAPI(APIView):
    

    def get(self, request):
        people_objs= People.objects.all()
        serializer= PeopleSerializer(people_objs, many=True)
        return Response({'status': 200, 'payload': serializer.data})

    def post(self, request):
        data= request.data
        serializer = PeopleSerializer(data= request.data)

        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status': 403, 'message' : 'Something went wrong'})
             
        serializer.save()
        return Response({'status': 200, 'payload': serializer.data, 'message': 'you data is saved'})

    def patch(self, request):
        try:
             people_obj = People.objects.get(id=request.data['id'])
             serializer = PeopleSerializer(people_obj, data= request.data,partial=True)    
             if not serializer.is_valid():
                 print(serializer.errors)
                 return Response({'status': 403,'errors': serializer.errors ,'message' : 'Something went wrong'})
           
             serializer.save()
             return Response({'status': 200, 'payload': serializer.data, 'message': 'your data is updated'})
        except Exception as e:
            print(e)
            return Response({'status' : 403, 'message': 'Invalid id'})
        


    def delete(self, request):
        try:
            id= request.GET.get('id')
            people_obj = People.objects.get(id=id)
            people_obj.delete()
            return Response({'status':200,'message': 'deleted'})

        except Exception as e:
            print(e)
            return Response({'status':403, 'message': 'Invalid id'})

