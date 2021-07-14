from django.shortcuts import render
from django.template import loader
from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def main(request):
    template = loader.get_template( "main.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )
    
def profile(request):
    template = loader.get_template( "profile.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

@csrf_exempt
def login(request):
    template = loader.get_template( "login.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

@csrf_exempt
def signup(request):
    template = loader.get_template( "signup.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

@csrf_exempt
def congrats(request):
    template = loader.get_template( "congrats.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def q2(request):
    template = loader.get_template( "q2.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def q3(request):
    template = loader.get_template( "q3.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def q4(request):
    template = loader.get_template( "q4.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )