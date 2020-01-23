from django.forms import ModelForm
from members.models import Address


class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = [
            "streetname",
            "housenumber",
            "floor",
            "door",
            "placename",
            "city",
            "zipcode",
            "dawa_id",
        ]
