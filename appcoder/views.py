from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from appcoder.models import Integrante

def listaIntegrantes(self):
	integrantes = Integrante.objects.all()
	cadena_respuesta = {"listaIntegrantes": integrantes}
	
	# for i in integrantes:
	# 	cadena_respuesta = f"<tr><td>{i.nombre}</td><td>{i.fecnac}</td><td>{i.telefono}</td></tr>"
    
	plantilla = loader.get_template("template1.html")
	
	documento =  plantilla.render(cadena_respuesta)
	
	return HttpResponse(documento)