from django import forms
from .models import Document, Television
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row
# from crispy_forms.bootstrap import (
#     PrependedText, PrependedAppendedText, FormActions)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'tv')

class TelevisionForm(forms.ModelForm):
    class Meta:
        model = Television
        fields = ('tv_name', 'tv_ip')

