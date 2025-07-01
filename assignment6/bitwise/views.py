from django.shortcuts import render
from .forms import NumberInputForm
from .models import CalculationResult

def input_view(request):
    if request.method == 'POST':
        form = NumberInputForm(request.POST)
        if form.is_valid():
            # Extract values
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            c = form.cleaned_data['c']
            d = form.cleaned_data['d']
            e = form.cleaned_data['e']
            values = [a, b, c, d, e]
            
            # Process data
            ## 1. Validation
            negative_warning = any(x < 0 for x in values)
            
            ## 2. Create sorted list (values > 10)
            filtered_sorted = sorted([x for x in values if x > 10])
            
            ## 3. Calculate average
            average = sum(values) / len(values)
            average_check = average > 50
            
            ## 4. Count positive values and check parity
            positive_count = sum(1 for x in values if x > 0)
            positive_parity = "even" if positive_count & 1 == 0 else "odd"
            
            # Save to MongoDB
            CalculationResult.objects.create(
                original_values=values,
                sorted_values=filtered_sorted,
                average=average,
                average_check=average_check,
                positive_count=positive_count,
                positive_parity=positive_parity
            )
            
            # Prepare context
            context = {
                'original': values,
                'sorted': filtered_sorted,
                'average': round(average, 2),
                'average_check': average_check,
                'positive_count': positive_count,
                'parity': positive_parity,
                'negative_warning': negative_warning,
                'results': CalculationResult.objects.all()[:10]
            }
            return render(request, 'bitwise/results.html', context)
    else:
        form = NumberInputForm()
    
    return render(request, 'bitwise/input.html', {'form': form})

def history_view(request):
    results = CalculationResult.objects.all()
    return render(request, 'bitwise/history.html', {'results': results})