from django import forms
from chapters.models import Chap, Pair, Call
from django.forms import Textarea, RadioSelect
# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

# from django.forms import inlineformset_factory

class ChapForm(forms.ModelForm):
  required_css_class = 'required'
  class Meta():
    model = Chap
    exclude = ('author', 'sum1', 'sum2', 'lr', 'rs', 'toCallNum0')
    # fields = ('name',)
    # fields = ('name', 'author', 'sum1', 'sum2', 'lr', 'rs', 'toCallNum0')
    widgets = {
      'name': Textarea(attrs={'cols': 40, 'rows':1, 'autofocus': True}),
    }
    # exclude = ('author', 'sum1', 'sum2')
    # fields = ('name', 'author', 'sum1', 'sum2')

  # class Media:
  #   css = {'all': ('chapters.css',)}

# ChapFormset = inlineformset_factory(Chap, fields=('name'))


class CallForm(forms.ModelForm):
  required_css_class = 'required'
  class Meta():
    model = Call
    fields = ('textAnswered',)
    widgets = {
      'textAnswered': Textarea(attrs={'cols': 50, 'rows': 3, 'class':'form-control', 'autofocus': True}),
    }
  # class Media:
  #   css = {'all': ('form.css',)}


class SettingsForm(forms.Form):
  CHOICES_LR = [('L', 'Links'),
                ('R', 'Rechts')]
  CHOICES_rs = [('r', 'zufällige Abfrage'),
                ('s', 'der Reihe nach abfragen')]

  LR = forms.ChoiceField(
    label = "Abfrageart",
    choices = CHOICES_LR,
    widget = forms.RadioSelect,
    initial= 'L'
  )


class PairForm(forms.ModelForm):
  required_css_class = 'required'
  class Meta():
    model = Pair
    exclude = ('chap', 'status')
    # fields = ('chap', 'textL', 'textR', 'status')
    widgets = {
      'textL': Textarea(attrs={'cols': 55, 'rows':3, 'class':'form-control', 'autofocus': True}),
      'textR': Textarea(attrs={'cols': 55, 'rows':3}),
    }

  class Media:
    css = {'all': ('form.css',)}