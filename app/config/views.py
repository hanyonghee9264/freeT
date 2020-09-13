from django.shortcuts import render


def index(request):
    return render(request, 'test.html')

def swiper(request):
    return render(request, 'base.html')
