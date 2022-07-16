from django.shortcuts import render
from django.http import HttpResponse

from functions import *
from forms import WordCloudForm

def wordcloud(request):
    if request.method == 'POST':
        wc_form = WordCloudForm(request.POST)
        if wc_form.is_valid():
            wc_text = wc_form.cleaned_data['wc_text']
    else:
        wc_form = WordCloudForm()
    wc = gen_wordcloud(wc_text)
    
    context = {'wc':wc, 'wc_form': wc_form}
    return render(request, 'wordcloud.html', context)
