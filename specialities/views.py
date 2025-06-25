from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SpecialitySerializer
from .services import create_speciality, get_specialities
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class SpecialityListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        specialities = get_specialities()
        serializer = SpecialitySerializer(specialities, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SpecialitySerializer(data=request.data)
        if serializer.is_valid():
            speciality = create_speciality(serializer.validated_data)
            return Response(SpecialitySerializer(speciality).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
