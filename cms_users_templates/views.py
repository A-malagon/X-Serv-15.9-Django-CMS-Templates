from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from models import apple
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.template import Context

# Create your views here.


def dispositivos(request):
    lista = apple.objects.all()
    salida = "<ul>\n"
    for fila in lista:
        salida += "<li><a href=dispositivos/" + fila.dispositivo + ">" +\
                  fila.dispositivo + "</a></li>\n"
    salida += "</ul>\n"
    salida += autenticacion(request)
    return HttpResponse(salida)

def dispositivosPlantilla(request):
    lista = apple.objects.all()
    (mensaje, admin, logger, usuario) = autenticacionPlantillas(request)
    template = get_template("index.html")
    c = Context({'contenido': "Todos tus dispositivos son:",
                 'salida': "========",
                 'lista': lista,
                 'mensaje': mensaje,
                 'administrador': admin,
                 'logger': logger})
    return HttpResponse(template.render(c))

@csrf_exempt
def info(request, recurso):
    if request.method == "GET":
        lista = apple.objects.filter(dispositivo=recurso)
        if not lista:
            return notFound(request, recurso)
        salida = " "
        for fila in lista:
            salida += "Dispositivo: " + fila.dispositivo + " Modelo: " +\
                      fila.modelo + " Precio: " + str(fila.precio)
    if request.method == "PUT":
        if request.user.is_authenticated():
            (modelo, precio) = request.body.split(";")
            nuevo = apple(dispositivo=recurso, modelo=modelo, precio=precio)
            nuevo.save()
            salida = ("Recurso(dispositivo) guardado")
        else:
            salida = ("Tienes que registrarte")
    salida += autenticacion(request)
    return HttpResponse(salida)

@csrf_exempt
def infoPlantillas(request, recurso):
    if request.method == "GET":
        lista = apple.objects.filter(dispositivo=recurso)
        if not lista:
            return notFound(request, recurso)
        salida = " "
        for fila in lista:
            salida += "Dispositivo: " + fila.dispositivo + " Modelo: " +\
                      fila.modelo + " Precio: " + str(fila.precio)
    if request.method == "PUT":
        if request.user.is_authenticated():
            (modelo, precio) = request.body.split(";")
            nuevo = apple(dispositivo=recurso, modelo=modelo, precio=precio)
            nuevo.save()
            salida = ("Recurso(dispositivo) guardado")
        else:
            salida = ("Tienes que registrarte")
    return salida

def elementoPlantilla(request, recurso):
    salida = infoPlantillas(request, recurso)
    (mensaje, admin, logger, usuario) = autenticacionPlantillas(request)
    template = get_template("index.html")
    c = Context({'contenido': "El dispositivo pedido:",
                 'salida': salida,
                 'mensaje': mensaje,
                 'administrador': admin,
                 'logger': logger})
    return HttpResponse(template.render(c))


def autenticacionPlantillas(request):
    if request.user.is_authenticated():
        mensaje = "Tu usuario es: " + request.user.username
        admin = "/admin/logout/"
        logger = "Logout"
    else:
        mensaje = "No registrado,inicie sesion"
        admin = "/admin/"
        logger = "Login"
    return (mensaje, admin, logger, request.user.username)

def autenticacion(request):
    if request.user.is_authenticated():
        return ("<br>Tu usuario es: " + request.user.username +
                "<br><a href='/admin/logout/'>Logout</a>")
    else:
        return ("<br>No registrado,inicie sesion\n<a href='/admin/'>Login</a>")



def notFound(request, recurso):
    salida = ("El dispositivo " + recurso + " no existe en Apple")
    salida += autenticacion(request)
    return HttpResponseNotFound(salida)
