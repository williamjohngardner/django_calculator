from django import forms


class CalcForm(forms.ModelForm):

    class Meta:
        fields = ["input"]
