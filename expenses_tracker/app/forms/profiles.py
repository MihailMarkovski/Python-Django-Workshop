from django import forms

from app.forms.Disable_delete_form_mixin import DisForMixIn
from app.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'


class DeleteProfile(ProfileForm, DisForMixIn):
    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        DisForMixIn.__init__(self)
