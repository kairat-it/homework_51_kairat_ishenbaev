from django import forms

class GreetForm(forms.Form):
    name = forms.CharField(max_length=15, label='Введите имя кота', widget=forms.TextInput(attrs={'placeholder': 'Имя кота'}))

class InteractForm(forms.Form):
    ACTIONS = [
        ('feed', 'Покормить'),
        ('play', 'Играть'),
        ('sleep', 'Спать'),
    ]
    action = forms.ChoiceField(choices=ACTIONS, widget=forms.RadioSelect)
