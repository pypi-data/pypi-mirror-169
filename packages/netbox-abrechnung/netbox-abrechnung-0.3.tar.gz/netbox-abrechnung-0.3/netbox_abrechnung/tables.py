import django_tables2 as tables

from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import SLA, Kunde, SLADevice


class SLADeviceTable(NetBoxTable):
    device = tables.Column(
        linkify=True
    )
    sla = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = SLADevice
        fields = ('pk','device','sla')
        default_columns = ('pk','device','sla')

class SLATable(NetBoxTable):
    name = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = SLA
        fields = ('pk','kunde','name', 'device_count')
        default_columns = ('pk','kunde','name', 'device_count')

class KundeTable(NetBoxTable):
    name = tables.Column(
        linkify=True,
    )
    sla_count = tables.Column()
    class Meta(NetBoxTable.Meta):
        model = Kunde
        fields = ('pk','name','sla_count')
        default_columns = ('name','sla_count')