from django import forms
import re #REGEX

#Le indico las características que deben cumplir los recuadros que darán lugar al tablero
class CreaFormularioForm(forms.Form): #forms es la librería y form es la clase
    username = forms.CharField(label='UserName')
    password = forms.CharField(label='Password', min_length=8)
    #fechaHora = forms.DateTimeField(label='Fecha y Hora')


    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            if username == password:
                raise forms.ValidationError("Error: El usuario no puede coincidir con la contraseña.")

        # Verificar si el nombre de usuario está presente en la contraseña (ignorando mayúsculas y minúsculas)
        if username and password and re.search(username, password, re.IGNORECASE):
            raise forms.ValidationError("La contraseña no puede contener el nombre de usuario.")

        # Verificar que la contraseña tenga al menos un carácter especial, una letra mayúscula, una letra minúscula y un número
        if not re.match(r'^(?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\d])(?=.*[A-Z])(?=.*[a-z])', password):
            raise forms.ValidationError(
                "La contraseña debe contener al menos un carácter especial, una letra mayúscula, una letra minúscula y un número.")

        # (?=.*[!@#$%^&*()_+{}\[\]:;<>,.?~\\\/\d]): Debe haber al menos un carácter especial en la contraseña.
        # (?=.*[A-Z]): Debe haber al menos una letra mayúscula en la contraseña.
        # (?=.*[a-z]): Debe haber al menos una letra minúscula en la contraseña.








