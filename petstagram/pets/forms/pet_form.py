from django import forms

from pets.models import Pet


class PetForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_all_pet_form_control()

    def get_all_pet_form_control(self):
        for _, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Pet
        fields = '__all__'
        widget = {
            'image_url': forms.TextInput(
                attrs={
                    'id': 'img_input'
                }
            )
        }
