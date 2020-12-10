from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import ProductModel
from .serializer import ProductSerializer


# Create your views here.
class ProductsListCreateView(ListCreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()


class ProductsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    # authentication_classes = [JWTAuthentication]
    serializer_class = ProductSerializer
    queryset = ProductModel.objects.all()

#     # Дістаємо продукти певного юзера
#     def get_queryset(self):
#         return ProductModel.objects.filter(user=self.request.user)
