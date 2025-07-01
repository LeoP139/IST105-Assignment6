from django.shortcuts import render
from .forms import NumberForm
from pymongo import MongoClient

def home(request):
    result = {}
    if request.method == 'POST':
        form = NumberForm(request.POST)
        if form.is_valid():
            nums = [form.cleaned_data['a'], form.cleaned_data['b'],
                    form.cleaned_data['c'], form.cleaned_data['d'],
                    form.cleaned_data['e']]

            warnings = []
            average = sum(nums) / len(nums)
            average_check = average > 50
            positive_count = sum(1 for n in nums if n > 0)
            even_odd = ["Par" if n & 1 == 0 else "Impar" for n in nums]
            greater_than_10 = sorted([n for n in nums if n > 10])

            result = {
                'original': nums,
                'even_odd': even_odd,
                'greater_than_10': greater_than_10,
                'average': average,
                'average_check': average_check,
                'positive_count': positive_count,
                'warnings': warnings
            }

            # Conexión MongoDB (reemplaza la IP por la real de tu MongoDB EC2)
            client = MongoClient("mongodb://cctb:cctb2025@<MONGO_EC2_PUBLIC_IP>:27017/cctbdb?authSource=cctbdb")
            db = client["cctbdb"]
            collection = db["submissions"]

            entry = {
                "input": nums,
                "results": result
            }
            collection.insert_one(entry)
    else:
        form = NumberForm()
    
    return render(request, 'result.html', {'form': form, 'result': result})
