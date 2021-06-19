from django import forms

from app.forms.Disable_delete_form_mixin import DisForMixIn
from app.models import Expense


class ExpensesForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'


class DisForm(ExpensesForm, DisForMixIn):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        DisForMixIn.__init__(self)
#inherit forms from EXPENSESFORM and use DISFORMIXIN
# to froze the str in fields when delete reusable !!