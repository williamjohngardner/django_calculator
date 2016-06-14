from django.shortcuts import render
from calc.forms import CalcForm


def index_view(request):
    print(request.POST)
    if request.POST:
        form = CalcForm(request.POST)
        if form.is_valid():
            form.save()
    return render(request, "index.html", {"form": CalcForm})
