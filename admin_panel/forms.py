# Import Django Users model & Forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# Import courses models
from courses.models import ContentHeader, ContentMedia, SubscribeCourse
# Import User_profile models
from user_profile.models import UserCourse
# Import core models
from core.models import Advertisements, AssistanceUser
# Import Form libary
from django import forms

# Create user form
class CreateUserForm(UserCreationForm ,forms.ModelForm):
     class Meta:
        # Model name
        model = User
        # Form Fields
        fields = [
            'first_name',
            'last_name',
            'username',
            'email'
        ]

# Update user form
class UpdateUserForm(forms.ModelForm):
     class Meta:
        # Model name
        model = User
        # Form Fields
        fields = [
            'first_name',
            'last_name',
            'username',
            'email',
            'is_active',
            'is_staff'
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

# Create course form
class CreateCourseForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        #Model name
        model = ContentHeader
        # Form fields
        fields = [
            'title',
            'description',
            'image',
        ]

# Update course form
class UpdateCourseForm(forms.ModelForm):
    image = forms.ImageField()
    class Meta:
        # Model name
        model = ContentHeader
        # Form fields
        fields = [
            'title',
            'description',
            'image',
            'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

# Create media form
class CreateMediaForm(forms.ModelForm):
    pdf = forms.FileField(required=False)
    images = forms.ImageField(required=False)
    class Meta:
        # Model name
        model = ContentMedia
        # Model Fields
        fields = [
            'name',
            'description',
            'notes',
            'g_suite',
            'video',
            'pdf',
            'images',
            'activity_name',
            'activity_description',
            'content'
        ]

# Update media form
class UpdateMediaForm(forms.ModelForm):
    pdf = forms.FileField(required=False)
    images = forms.ImageField(required=False)
    class Meta:
        # Model name
        model = ContentMedia
        # Model Fields
        fields = [
            'name',
            'description',
            'notes',
            'g_suite',
            'video',
            'pdf',
            'images',
            'activity_name',
            'activity_description',
            'status'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'notes': forms.TextInput(attrs={'class': 'form-control'}),
            'g_suite': forms.URLInput(attrs={'class': 'form-control'}),
            'video': forms.URLInput(attrs={'class': 'form-control'}),
            'activity_name': forms.TextInput(attrs={'class': 'form-control'}),
            'activity_description': forms.Textarea(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

# Assign course form
class AssignCourseForm(forms.ModelForm):
    class Meta:
        #Model name
        model = UserCourse
        #Model fields
        fields = [
            'user',
            'course'
        ]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'})
        }

# UpdateAssign course form
class UpdateAssignCourseForm(forms.ModelForm):
    class Meta:
        #Model name
        model = UserCourse
        #Model fields
        fields = [
            'user',
            'course',
            'status'
        ]
        widgets = {
            'user': forms.Select(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }

# Create advertisements form
class CreateAdvertisementForm(forms.ModelForm):
    class Meta:
        # Model name
        model = Advertisements
        # Model fields
        fields = [
            'title',
            'content',
            'user'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.SelectMultiple(attrs={'class': 'form-control'})
        }

# Update advertisements form
class UpdateAdvertisementsForm(forms.ModelForm):
    class Meta:
        # Model name
        model = Advertisements
        # Model fields
        fields = [
            'title',
            'content',
            'user',
            'status'
        ]
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.TextInput(attrs={'class': 'form-control'}),
            'user': forms.SelectMultiple(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'})
        }