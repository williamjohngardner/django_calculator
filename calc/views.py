from calc.forms import Calculator
from calc.models import Operation
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponseRedirect


def index_view(request):
    result = ""
    a = ''
    b = ''
    operators = ''

    print(request.POST)
    if request.method == "POST":
        form = Calculator(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            operators = form.cleaned_data['operators']
            if form.cleaned_data['operators'] == '+':
                result = form.cleaned_data['a'] + form.cleaned_data['b']
            elif form.cleaned_data['operators'] == '-':
                result = form.cleaned_data['a'] - form.cleaned_data['b']
            elif form.cleaned_data['operators'] == '*':
                result = form.cleaned_data['a'] * form.cleaned_data['b']
            elif form.cleaned_data['operators'] == '/':
                result = form.cleaned_data['a'] / form.cleaned_data['b']
        if request.user.is_authenticated():
            Operation.objects.create(a=a, operators=operators, b=b, result=result, user=request.user)
    return render(request, "index.html", {"form": Calculator(), "result": result, "a": a, "b": b, "operators": operators})


@login_required
def profile_view(request):
    print(request.user)
    user_data = {"data": Operation.objects.filter(user=request.user)}
    return render(request, "profile.html", user_data)


def create_user(request):
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "create_user.html", {"form": form})
    form = UserCreationForm()
    return render(request, "create_user.html", {"form": form})
