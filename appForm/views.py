from django.shortcuts import render
from .forms import CreaFormularioForm


def index(request):
    return render(request, 'appForm/index.html', {})


def formulario(request):
    # Si se ha enviado el formulario
    formulario_form = CreaFormularioForm()
    username = None
    password = None
    if request.method == 'POST':
        formulario_form = CreaFormularioForm(request.POST)
        # Ejecutamos la validacion
        if formulario_form.is_valid():
            # Los datos se cogen del diccionario cleaned_data
            username = formulario_form.cleaned_data['username']
            password = formulario_form.cleaned_data['password']
            #fechaHora = formulario_form.cleaned_data['fechaHora']

            # Crear un nuevo formulario vacío después de procesar la información
            #formulario_form = CreaFormularioForm() //Esto serviría para limpiar el formulario
            #Lo he desactivado porque pide limpiarlo en una ocasión determinada
    else:
        # Si la solicitud no es POST, simplemente inicializa el formulario
        formulario_form = CreaFormularioForm()
    return render(request, 'appForm/formulario.html', {'form': formulario_form, 'username': username, 'password': password})


