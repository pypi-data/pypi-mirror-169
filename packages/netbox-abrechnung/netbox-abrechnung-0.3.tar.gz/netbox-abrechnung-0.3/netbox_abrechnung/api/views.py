from django.db.models import Count

from netbox.api.viewsets import NetBoxModelViewSet

from .. import filtersets, models
from .serializers import SLADeviceSerializer, KundeSerializer, SLADeviceSerializer,SLASerializer

class SLAViewSet(NetBoxModelViewSet):
     filterset_class = filtersets.SLAFilterSet
     queryset = models.SLA.objects.all()
     serializer_class = SLASerializer


class SLADeviceViewSet(NetBoxModelViewSet):
     queryset = models.SLADevice.objects.all()
     serializer_class = SLADeviceSerializer


class KundeViewSet(NetBoxModelViewSet):
     queryset = models.Kunde.objects.all()
     serializer_class = KundeSerializer

