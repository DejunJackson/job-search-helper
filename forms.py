from django import forms

class WordCloudForm(forms.Form):
    wc_text = forms.CharField(widget=forms.Textarea, label='')