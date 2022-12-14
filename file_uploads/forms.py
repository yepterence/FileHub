from django import forms
from .models import UploadedFile


class UploadedFileForm(forms.ModelForm):
    """ModelForm for Uploaded File model."""
    class Meta:
        model = UploadedFile
        fields = ('text', 'number', 'file', 'unique_identifier')
        widgets = {
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'number': forms.NumberInput(attrs={'class': 'form-control'}),
            'unique_identifier': forms.HiddenInput(),
            'session_id': forms.HiddenInput(),
            'file': forms.FileInput(attrs={'readonly': 'readonly'}),

        }
