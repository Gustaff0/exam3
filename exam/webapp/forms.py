from django import forms
from django.forms import widgets
from webapp.models import Feedback, Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name', 'category', 'description', 'img')

class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Найти')


class FeedbackForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('feedback_text', 'appraisal')


class FeedbackModerForm(forms.ModelForm):

    class Meta:
        model = Feedback
        fields = ('moder_check',)
