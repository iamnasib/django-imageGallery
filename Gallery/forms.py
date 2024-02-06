from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm,AuthenticationForm
from .models import Images

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        for field_name in ('username', 'email', 'password1', 'password2'):
            self.fields[field_name].help_text = None


    

class LoginForm(AuthenticationForm):
    

    class Meta:
        model = User
        fields = ['username', 'password',]

class UploadImageForm(forms.ModelForm):
    image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file d-none',
                                                      'id':'dp','onchange' : "readURL(this);"}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                    'placeholder':'description', 'required':'false',
                                                    'rows': 3}))
    title=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder':'title', 'required':'false',
                                                    
                                                    }))

    class Meta:
        model=Images
        fields=['image','description','title']

class EditPostForm(forms.ModelForm):
    post_image=forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file ',
                                                      'id':'dp'}))
    descriptionn = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                    'placeholder':'description', 'required':'false',
                                                    'rows': 3}))
    titlee=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                    'placeholder':'title', 'required':'false',
                                                    
                                                    }))
    class Meta:
        model=Images
        fields=['image','descriptionn','titlee']