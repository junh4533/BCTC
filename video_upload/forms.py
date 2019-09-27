from django import forms
from .models import Document, Television, Config
from django.contrib.auth.forms import UserChangeForm

#update note: description is no longer needed
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('document', 'tv')

class TelevisionForm(forms.ModelForm):
    class Meta:
        model = Television
        fields = ('tv_name', 'tv_ip')

#TV Config Form
class ConfigForm(forms.ModelForm):
    class Meta:
        model = Config
        fields = ('TV',)

#IP update form for existing tv
class EditForm(UserChangeForm):
    class Meta:
        model = Television
        fields = ('tv_ip',)

