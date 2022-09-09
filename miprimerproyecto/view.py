#from xml.dom.minidom import Document
#from django.http import HttpResponse
#import pathlib
#from django.template import Template, Context
#
#path = pathlib.Path(__file__).parent.resolve()
#
#def saludar(request):
#    return HttpResponse("Hola Mundo")
#
#def segundavista(request):
#    return HttpResponse('<div style="background-color: blue; width: 100%; height: 100%; position: absolute; color: white; border : 0px; margin: 0px">Hola equipo coder</div>'
#)
#
#def nombre(self, nombre):
#    documentoTexto = f'mi nombre es{nombre}'
#    return HttpResponse(documentoTexto)
#
#def template(self):
#    mihtml = open(f'{path}/template/index.html')
#    planilla = Template(mihtml.read())
#    mihtml.close()
#    miContexto = Context()
#    documento = planilla.render(miContexto)
#    return HttpResponse(documento)

from django.http import HttpResponse
from django.template import loader

def home(self, name):
    return HttpResponse(f"Hola soy {name}")

def homePage(self):
    lista = [1,2,3,4,5]
    data = {'nombre':'David','apellido':'casanoves','lista':lista}
    planilla = loader.get_template('home.html')
    documento = planilla.render(data)
    return HttpResponse(documento)    

def cursos(self):
    planilla = loader.get_template('cursos.html')
    documento = planilla.render()
    return HttpResponse(documento)   