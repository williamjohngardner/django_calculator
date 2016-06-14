from django.shortcuts import render
from django.http import HttpResponseRedirect
from calc.forms import Calculator


def index_view(request):
    result = ""
    form = Calculator
    print(request.POST)
    if request.method == "POST":
        form = Calculator(request.POST)
        if form.is_valid():
            if form.cleaned_data['operators'] == '+':
                result = form.cleaned_data['a'] + form.cleaned_data['b']
            elif form.cleaned_data['operators'] == '-':
                result = form.cleaned_data['a'] - form.cleaned_data['b']
            elif form.cleaned_data['operators'] == '*':
                result = form.cleaned_data['a'] * form.cleaned_data['b']
            elif form.cleaned_data['operators'] == '/':
                result = form.cleaned_data['a'] / form.cleaned_data['b']
    return render(request, "index.html", {"form": form, "result": result})
