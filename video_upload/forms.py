from django import forms
from .models import Document, Television, Config
from django.contrib.auth.forms import UserChangeForm
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row
# from crispy_forms.bootstrap import (
#     PrependedText, PrependedAppendedText, FormActions)

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

