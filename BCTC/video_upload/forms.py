from django import forms
from .models import Document
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Submit, Layout, Field
# from crispy_forms.bootstrap import (
#     PrependedText, PrependedAppendedText, FormActions)

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', 'tv')

