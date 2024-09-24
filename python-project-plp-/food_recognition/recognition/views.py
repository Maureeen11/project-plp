from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os

def home(request):
    return render(request, 'home.html')

def analyze_food(request):
    if request.method == 'POST' and request.FILES['foodImage']:
        uploaded_file = request.FILES['foodImage']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)
        # Add your food recognition logic here
        return render(request, 'result.html', {'file_url': file_url})
    return render(request, 'home.html')
import tensorflow as tf

def analyze_food(request):
    if request.method == 'POST' and request.FILES['foodImage']:
        uploaded_file = request.FILES['foodImage']
        fs = FileSystemStorage()
        filename = fs.save(uploaded_file.name, uploaded_file)
        file_url = fs.url(filename)

        # Load your food recognition model here and perform the prediction
        # model = tf.keras.models.load_model('path_to_your_model')
        # image = tf.keras.preprocessing.image.load_img(fs.path(filename), target_size=(224, 224))
        # result = model.predict(image)

        return render(request, 'result.html', {'file_url': file_url})
    return render(request, 'home.html')
