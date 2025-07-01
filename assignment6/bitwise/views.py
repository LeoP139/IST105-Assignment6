from django.shortcuts import render
from .forms import NumberForm
from .models import Submission

def home(request):
    result = {}
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = form.cleaned_data['d']
            e = form.cleaned_data['e']
            inputs = [a, b, c, d, e]

            average = sum(inputs) / 5
            is_above_50 = average > 50
            positives = sum(1 for i in inputs if i > 0)
            even_odd = ["Par" if i % 2 == 0 else "Impar" for i in inputs]
            greater_than_10 = sorted([i for i in inputs if i > 10])

            result = {
                'original': inputs,
                'average': average,
                'is_above_50': is_above_50,
                'positives': positives,
                'even_odd': even_odd,
                'greater_than_10': greater_than_10
            }

            Submission.objects.create(
                input_a=a, input_b=b, input_c=c, input_d=d, input_e=e,
                average=average,
                is_above_50=is_above_50,
                positives=positives,
                even_odd=even_odd,
                greater_than_10=greater_than_10
            )
    else:
        form = NumberForm()
    
    return render(request, 'result.html', {'form': form, 'result': result})
