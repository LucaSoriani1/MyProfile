from django.forms import ModelForm, Textarea
from .models import ContactForm, ContactItForm

class ContactModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = ContactForm
        fields='__all__'
        widgets={
            'message': Textarea(
                attrs={
                    'style':'resize:none;',
                    'rows':'6',
                    'id':'message'
                }
            )
        }
class ContactItModelForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = ContactItForm
        fields='__all__'
        widgets={
            'message': Textarea(
                attrs={
                    'style':'resize:none;',
                    'rows':'6',
                    'id':'message'
                }
            )
        }