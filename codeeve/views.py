from django.shortcuts import render


def home(request):
    return render(request, 'codeeve/home.html', context={})
