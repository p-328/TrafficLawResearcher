from django import forms

class CreateChatbotForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}), min_length=1)

class QueryForm(forms.Form):
    query = forms.CharField(widget=forms.TextInput(attrs={'class': 'input'}))
    query_choices = [
        ('general', 'General'),
        ('report', 'Report')
    ]
    query_choice = forms.ChoiceField(choices=query_choices, widget=forms.Select(attrs={'class': 'select', 'onchange': 'dyn_change();'}))
    format_of_data = forms.CharField(empty_value='', widget=forms.HiddenInput(attrs={'class': 'input'}), required=False)
