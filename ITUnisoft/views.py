from django.shortcuts import redirect, render


def index(requests):
    return render(requests, 'index.html')


