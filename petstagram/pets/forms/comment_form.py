from django import forms

from pets.models import Comment


class CommentForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',

    })
    )

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    # def get_all_form_control(self):
    #
    #     for _, field in self.fields.items():
    #         field.widget.attrs['class'] = 'form-control'
    # class Meta:
    #     model = Comment
    #     fields = ['text']]

