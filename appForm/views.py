from django.shortcuts import render
from .forms import CreaFormularioForm
from datetime import datetime, timezone



def index(request):
    return render(request, 'appForm/index.html', {})


def formulario(request):
    # Si se ha enviado el formulario
    formulario_form = CreaFormularioForm()
    username = None
    password = None
    error = None

    if request.method == 'POST':
        formulario_form = CreaFormularioForm(request.POST)

        # Ejecutamos la validacion
        if formulario_form.is_valid():

            # Los datos se cogen del diccionario cleaned_data
            username = formulario_form.cleaned_data['username']
            password = formulario_form.cleaned_data['password']


    else:
        # formulario_form = CreaFormularioForm() SI quisiera que me vaciase el form
        formulario_form = CreaFormularioForm(initial={'fechahora': datetime.now(timezone.utc)})



    return render(request, 'appForm/formulario.html', {'form': formulario_form, 'username': username, 'password': password, 'error': error})


