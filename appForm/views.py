from django.shortcuts import render
from .forms import CreaFormularioForm


def index(request):
    return render(request, 'appForm/index.html', {})


def formulario(request):
    # Si se ha enviado el formulario
    formulario_form = CreaFormularioForm()
    if request.method == 'POST':

        formulario_form = CreaFormularioForm(request.POST)
        # Ejecutamos la validacion
        if formulario_form.is_valid():
            # Los datos se cogen del diccionario cleaned_data
            fechaInicio = formulario_form.cleaned_data['fechaInicio']
            fechaFin = formulario_form.cleaned_data['fechaFin']
            diasSemana = formulario_form.cleaned_data['diasSemana']
            email = formulario_form.cleaned_data['email']
            return render(request, 'appForm/respuesta_formulario.html',
                          {'fechaInicio': fechaInicio, 'fechaFin': fechaFin, 'diasSemana': diasSemana,
                           'email': email})
    return render(request, 'appForm/formulario.html', {'form': formulario_form})


from django.shortcuts import render

# Create your views here.
