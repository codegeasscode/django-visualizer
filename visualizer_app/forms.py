from django import forms

class VisualizationForm(forms.Form):
    json_data = forms.CharField(widget=forms.Textarea, label="enter JSON data")
