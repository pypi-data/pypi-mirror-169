from django.core.exceptions import ObjectDoesNotExist
from extras.plugins import PluginTemplateExtension
from django.conf import settings
from packaging import version
from .models import *

class SLAContractStatus(PluginTemplateExtension):
    model = "dcim.device"

    def left_page(self):
        device = self.context["object"]
     
        try:
            c_device = SLADevice.objects.get(device=device)
            return self.render(
                "netbox_abrechnung/device.html", extra_context={
                    "cdevice": c_device
                    }
            )
        except:
             return ""

template_extensions = [SLAContractStatus]