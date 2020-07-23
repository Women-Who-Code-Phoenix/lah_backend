from rest_framework import viewsets

from .field_choices import ACTIVE
from .models import Resource
from .serializers import ResourceSerializer


class ResourceViewSet(viewsets.ModelViewSet):
    queryset = Resource.objects.filter(status=ACTIVE).order_by("-id")
    serializer_class = ResourceSerializer
