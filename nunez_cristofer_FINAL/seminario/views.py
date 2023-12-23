from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import generics
from django.views import View
from .models import Inscrito, Institucion
from .serializers import InscritoSerializer, InstitucionSerializer
from .forms import InscritoForm, InstitucionForm
from django.http import HttpResponse

# Vistas basadas en funciones (FBV) para la interfaz HTML
def home(request):
    return render(request, 'home.html')

def inscritos_list(request):
    inscritos = Inscrito.objects.all()
    search_id = request.GET.get('id')

    if search_id:
        inscrito = get_object_or_404(Inscrito, id=search_id)
        return render(request, 'inscritos_list.html', {'inscritos': [inscrito]})

    return render(request, 'inscritos_list.html', {'inscritos': inscritos})

class InscritoList(View):
    template_name = 'inscritos_list.html'

    def get(self, request, *args, **kwargs):
        id_query = request.GET.get('id')
        
        if id_query:
            try:
                inscrito = get_object_or_404(Inscrito, id=id_query)
                return render(request, self.template_name, {'inscritos': [inscrito]})
            except Inscrito.DoesNotExist:
                return HttpResponse("ID no existente")
        else:
            inscritos = Inscrito.objects.all()
            return render(request, self.template_name, {'inscritos': inscritos})

def agregar_inscrito(request):
    instituciones = Institucion.objects.all()
    if request.method == 'POST':
        form = InscritoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inscritos-list')
    else:
        form = InscritoForm()
    return render(request, 'agregar_inscrito.html', {'instituciones': instituciones, 'form': form})

def instituciones_list(request):
    instituciones = Institucion.objects.all()
    search_id = request.GET.get('id')

    if search_id:
        institucion = get_object_or_404(Institucion, id=search_id)
        return render(request, 'instituciones_list.html', {'instituciones': [institucion]})

    return render(request, 'instituciones_list.html', {'instituciones': instituciones})

class InstitucionList(View):
    template_name = 'instituciones_list.html'

    def get(self, request, args, kwargs):
        id_query = request.GET.get('id')
        
        if id_query:
            try:
                institucion = Institucion.objects.get(id=id_query)
                return render(request, self.template_name, {'instituciones': [institucion]})
            except Institucion.DoesNotExist:
                return HttpResponse("ID no existente")
        else:
            instituciones = Institucion.objects.all()
            return render(request, self.template_name, {'instituciones': instituciones})

def agregar_institucion(request):
    if request.method == 'POST':
        form = InstitucionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instituciones-list')
    else:
        form = InstitucionForm()
    return render(request, 'agregar_institucion.html', {'form': form})

# Vistas basadas en clases (CBV) para la API con DRF
class InscritoList(generics.ListCreateAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InscritoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inscrito.objects.all()
    serializer_class = InscritoSerializer

class InstitucionList(generics.ListCreateAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer

class InstitucionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Institucion.objects.all()
    serializer_class = InstitucionSerializer
