from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import cookie_stand
from .permissions import IsOwnerOrReadOnly
from .serializers import cookie_standSerializer


class cookie_standList(ListCreateAPIView):
    queryset = cookie_stand.objects.all()
    serializer_class = cookie_standSerializer


class cookie_standDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = cookie_stand.objects.all()
    serializer_class = cookie_standSerializer
