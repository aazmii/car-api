from rest_framework.views import APIView
from rest_framework.response import Response
from car_dekho_app.api_files.serializers import ShowroomSerializer
from car_dekho_app.models.showroom import Showrooms
class ShowroomView(APIView): 
    def get(self, request): 
       showrooms = Showrooms.objects.all()
       serializer = ShowroomSerializer(showrooms, many=True)
       return Response(serializer.data)
    def post (self,request): 
        serializer = ShowroomSerializer(data = request.data)
        if serializer.is_valid(): 
            serializer.save()
            return Response(serializer.data)
        else : 
            return Response(serializer.errors)