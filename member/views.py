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

def findpw(request):
    template = loader.get_template( "findpw.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def q5(request):
    template = loader.get_template( "q5.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def q6(request):
    template = loader.get_template( "q6.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def q7(request):
    template = loader.get_template( "q7.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def q8(request):
    template = loader.get_template( "q8.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def findteam(request):
    template = loader.get_template( "findteam.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def detail(request):
    template = loader.get_template( "teamdetail.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def findprj(request):
    template = loader.get_template( "findprj.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def prjdetail(request):
    template = loader.get_template( "prjdetail.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )  

def chat(request):
    template = loader.get_template( "chat.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )

def app(request):
    template = loader.get_template( "application.html" )
    context ={}
    return HttpResponse( template.render( context, request ) )