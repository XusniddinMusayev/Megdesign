from django import forms
from .models import Rate


class RateCommentForm(forms.ModelForm):                   
    class Meta:
        model = Rate
        fields = "__all__"
        exclude = ['blog']

    def __init__(self, *args, **kwargs):
        super(RateCommentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            # field.widget.attrs['placeholder'] = field_name
