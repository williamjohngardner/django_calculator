from django import forms


class Calculator(forms.Form):
    operators = [('+', '+'), ('-', '-'), ('*', '*'), ('/', '/')]
    a = forms.FloatField()
    operators = forms.ChoiceField(operators, required=True)
    b = forms.FloatField()
