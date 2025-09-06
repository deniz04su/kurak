from django import forms
from .models import ProductMedia

class ProductMediaForm(forms.ModelForm):
    class Meta:
        model = ProductMedia
        fields = ['file', 'is_video']
        widgets = {
            'file': forms.ClearableFileInput(attrs={'multiple': True})
        }

