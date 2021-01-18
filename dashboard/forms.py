# Import Form libary
from django import forms
# Import models
from user_profile.models import ActivityUsers

# Upload user activity form class
class UploadFile(forms.ModelForm):
    act_file = forms.FileField()
    class Meta:
        # Le pasamos nuestro modelo a una variable interna
        model = ActivityUsers

        # Declaramos los campos que estarán dentro de nuestro form
        fields = [
            'comment',
            'act_file'
        ]
        # Obtenemos los campos del admin de Django para la integración al template
        widgets = {
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }