from django import forms
from calc.models import Operation


class Calculator(forms.ModelForm):
    operators = [('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')]
    a = forms.FloatField()
    operators = forms.ChoiceField(operators, required=True)
    b = forms.FloatField()

    class Meta:
        model = Operation
        fields = ["a", "operators", "b"]