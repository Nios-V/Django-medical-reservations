from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import DoctorProfileSerializer
from .services import create_doctor_profile, get_doctor_profile
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class DoctorProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile = get_doctor_profile(request.user)
        if profile:
            serializer = DoctorProfileSerializer(profile)
            return Response(serializer.data)
        return Response({"detail": "Profile not found."}, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        if hasattr(request.user, 'doctor_profile'):
            return Response({"detail": "Profile already exists,"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = DoctorProfileSerializer(data=request.data)
        if serializer.is_valid():
            profile = create_doctor_profile(
                serializer.validated_data, user=request.user)
            return Response(DoctorProfileSerializer(profile).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
