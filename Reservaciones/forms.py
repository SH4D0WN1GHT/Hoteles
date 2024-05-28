# C:\repos\Hoteles\Reservaciones\forms.py
from django import forms
from .models import Reservacion
from datetime import datetime
from django.core.exceptions import ValidationError

class ReservacionForm(forms.ModelForm):
    class Meta:
        model = Reservacion
        fields = ['tipo', 'lugar', 'numero_tarjeta', 'fecha']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'datepicker'}),
        }

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha:
            try:
                datetime.strptime(str(fecha), '%Y-%m-%d')
            except ValueError:
                raise ValidationError('El formato de la fecha debe ser YYYY-MM-DD')
        return fecha
