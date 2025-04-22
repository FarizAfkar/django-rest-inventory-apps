from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import authenticate
from .models import Inventory
from .serializers import InventoryCreate, InventoryDetail, InventoryUpdate,\
    LoginSerializer, TokenRefreshSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.parsers import MultiPartParser


class CustomTokenObtainPairView(APIView):
    """
    Token Authenctication Using Simple JWT
    request username & password
    authenticate user
    response token acccess & refresh
    """

    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @swagger_auto_schema(
        request_body=LoginSerializer,
        operation_description="Login endpoint using username and password.",
        responses={200: "Login success"}
    )

    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(username=username, password=password)
        if user is None:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        refresh = RefreshToken.for_user(user)
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })


class CustomTokenRefreshView(APIView):
    """
    Token Authenctication Using Simple JWT
    request token refresh
    response token acccess
    """

    permission_classes = [AllowAny]
    serializer_class = TokenRefreshSerializer

    @swagger_auto_schema(
        request_body=TokenRefreshSerializer,
        operation_description="Token Refresh to get access.",
        responses={200: "Token refresh success"}
    )

    def post(self, request):
        refresh_token = request.data.get('refresh')
        if not refresh_token:
            return Response({'error': 'Refresh token required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh = RefreshToken(refresh_token)
            access_token = refresh.access_token
            return Response({'access': str(access_token)})
        except Exception:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)


class CreateInventoryAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.all()
    serializer_class = InventoryCreate
    parser_classes = (MultiPartParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        inventory = serializer.save()
        return Response({
            "message": "Inventory created successfully.",
            "data": InventoryDetail(inventory).data
        }, status=status.HTTP_201_CREATED)


class ListInventoryAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.all()
    serializer_class = InventoryDetail

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({
            "message": "Inventory list retrieved.",
            "count": queryset.count(),
            "data": serializer.data
        })


class DetailInventoryAPIView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.all()
    serializer_class = InventoryDetail
    lookup_field = 'id'

    def retrieve(self, request, *args, **kwargs):
        inventory = self.get_object()
        serializer = self.get_serializer(inventory)
        return Response({
            "message": "Inventory detail retrieved.",
            "data": serializer.data
        })


class UpdateInventoryAPIView(generics.UpdateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.all()
    serializer_class = InventoryUpdate
    parser_classes = (MultiPartParser,)
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        inventory = self.get_object()
        serializer = self.get_serializer(inventory, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        inventory = serializer.save()
        return Response({
            "message": "Inventory updated successfully.",
            "data": InventoryDetail(inventory).data
        })


class DeleteInventoryAPIView(generics.DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Inventory.objects.all()
    lookup_field = 'id'

    def destroy(self, request, *args, **kwargs):
        inventory = self.get_object()
        inventory.delete()
        return Response({
            "message": "Inventory deleted successfully."
        }, status=status.HTTP_204_NO_CONTENT)
