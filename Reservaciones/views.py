from django.shortcuts import render

def main(request):
    render(request, 'base.html')