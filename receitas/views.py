from django.http import HttpResponse
from django.shortcuts import render


def home(request):

    return HttpResponse('Pagina inicial Denise')


def sobre(request):

    return HttpResponse('Pagina sobre o site da Denise')


def contato(request):

    return HttpResponse('Pagina de contatos da Denise')
