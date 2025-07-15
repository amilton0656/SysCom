from django.shortcuts import render
from django.contrib import messages

def index(request):
    context = {
        'mensagem': messages.success(request, "Esta é uma mensagem de sucesso!")
    }
    return render(request, 'index.html', context)
