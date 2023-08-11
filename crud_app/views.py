from django.shortcuts import render, redirect

data = {
    "name":"pawan",
    "age":21,
}  # Simulated data storage

def create(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        age = request.POST.get('age')
        city = request.POST.get('city')
        data[name] = {'age': age, 'city': city}
        return redirect('/read')
    return render(request, 'create.html')

def read(request):
    return render(request, 'read.html', {'data': data})

def update(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name in data:
            age = request.POST.get('age')
            city = request.POST.get('city')
            data[name] = {'age': age, 'city': city}
        return redirect('/read')
    return render(request, 'update.html', {'data': data})

def delete(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if name in data:
            del data[name]
        return redirect('/read')
    return render(request, 'delete.html', {'data': data})
