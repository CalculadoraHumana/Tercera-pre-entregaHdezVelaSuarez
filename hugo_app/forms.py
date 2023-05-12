from django import forms
from .models import MiModelo, SegundoModelo, TercerModelo

class MiModeloForm(forms.ModelForm):
    class Meta:
        model = MiModelo
        fields = '__all__'


class SegundoModelo(forms.ModelForm):
    class Meta:
        model = SegundoModelo
        fields = '__all__'


class TercerModelo(forms.ModelForm):
    class Meta:
        model = TercerModelo
        fields = '__all__'


