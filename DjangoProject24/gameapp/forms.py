from django import forms


class GameForm(forms.Form):
    game_name = forms.ChoiceField(
        choices=[('coin', 'Игра в монетку'), ('cube', 'Игра в кости'), ('number', 'Случайное число')])
    count = forms.IntegerField(min_value=1, max_value=50)
