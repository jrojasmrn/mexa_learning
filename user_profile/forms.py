# Import Form libary
from django import forms
# Import models
from .models import UserProfile

# Update user_profile form class
class UpdateProfile(forms.ModelForm):
    user_image = forms.ImageField()
    class Meta:
        # Le pasamos nuestro modelo a una variable interna
        model = UserProfile

        # Declaramos los campos que estarán dentro de nuestro form
        fields = [
            'description',
            'user_image',
            'location',
            'languaje'
        ]
        # Obtenemos los campos del admin de Django para la integración al template
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
            'languaje': forms.Select(attrs={'class': 'form-control'}),
        }