from rest_framework import generics
from .serializers import LandmarkSerializer
from .models import Landmark


class LandmarkList(generics.ListCreateAPIView):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer

class LandmarkDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Landmark.objects.all()
    serializer_class = LandmarkSerializer




# from django.shortcuts import render, redirect

# from .models import Landmark

# from .forms import LandmarkForm

# from django.http import JsonResponse

# # Create your views here.

# # def landmark_list(request):
# #     landmarks = Landmark.objects.all()
# #     return render(request, 'nyc/landmark_list.html', {'landmarks': landmarks})

# def landmark_list(request): 
#     landmarks = Landmark.objects.all().values('name', 'photo_url', 'description')
#     landmarks_list = list(landmarks) # convert our landmarks to a list instead of Queryset
#     return JsonResponse(landmarks_list, safe=False) # safe=fale is neede if the first parameter is not a dictionary. 

# def landmark_detail(request, pk):
#     landmarks = Landmark.objects.get(id=pk)
#     return render(request, 'nyc/landmark_detail.html', 
#     {'landmarks': landmarks})

# def landmark_create(request):
#     if request.method == 'POST':
#         form = LandmarkForm(request.POST)
#         if form.is_valid():
#             Landmark = form.save()
#             return redirect('landmark_detail', pk=Landmark.pk)
#         else: 
#             form = LandmarkForm()
#         return render(request, 'nyc/landmark_form.html', {'form': form})

# def landmark_edit(request, pk):
#     landmark = Landmark.objects.get(pk=pk)
#     if request.method == "POST":
#         form = LandmarkForm(request.POST, instance=landmark)
#         if form.is_valid():
#             landmark = form.save()
#             return redirect('landmark_detail', pk=landmark.pk)
#     else:
#         form = LandmarkForm(instance=landmark)
#     return render(request, 'nyc/landmark_form.html', {'form': form})

# def artist_delete(request, pk):
#     Landmark.objects.get(id=pk).delete()
#     return redirect('artist_list')