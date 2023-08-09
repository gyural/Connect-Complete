# from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import CompareList, Obj
from .serializers import CompareListSerializer, ObjSerializer
from rest_framework import status, generics


# Blog의 목록을 보여주는 역할
# class CompareListCreate(APIView):
#     permission_classes = [IsAuthenticated]
#     def post(self, request):
#         serializer = CompareListSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save(user=request.user)
#             res = Response(
#                 {
#                     "message": "register successs",
#                 },
#                 status=status.HTTP_200_OK,
#             )
#             return res
#         else:
#             return Response(status=status.HTTP_400_BAD_REQUEST)
#
#     def get(self, request):
#         comparelist = CompareList.objects.all()
#         serializer = CompareListSerializer(instance=comparelist, many=True)
#         return Response(serializer.data)

class CompareListCreate(ModelViewSet):
   queryset = CompareList.objects.all()
   serializer_class = CompareListSerializer



class ObjListCreate(ModelViewSet):
    queryset = Obj.objects.all()
    serializer_class = ObjSerializer