from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from carMng.forms import CarForm
from carMng.models import MainMenu, Car
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
# Create your views here.


def index(request):
    return render(request,
                  'carMng/index.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )


def aboutUs(request):
    return render(request,
                  'carMng/aboutUs.html',
                  {
                      'item_list': MainMenu.objects.all(),
                  }
                  )


def postCar(request):
    submitted = False
    if request.method == 'POST':
        form = CarForm(request.POST, request.FILES)
        if form.is_valid():
            car = form.save(commit=False)
            try:
                car.username = request.user
            except Exception:
                pass
            car.save()
            return HttpResponseRedirect('/postCar?submitted=True')
    else:
        form = CarForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,
                  'carMng/postCar.html',
                  {
                      'form': form,
                      'item_list': MainMenu.objects.all(),
                      'submitted': submitted,
                  }
                  )


def home(request):
    featured_cars = Car.objects.filter(is_featured=True)
    for c in featured_cars:
        c.pic_path = c.picture.url[18:]
    return render(request,
                  'carMng/home.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'featured_cars': featured_cars,
                  }
                  )


def displayCars(request):
    cars = Car.objects.all()
    for c in cars:
        c.pic_path = c.picture.url[18:]
    return render(request,
                  'carMng/displayCars.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'cars': cars,
                  }
                  )


class Register(CreateView):
    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


def car_detail(request, car_id):
    car = Car.objects.get(id=car_id)
    car.pic_path = car.picture.url[18:]
    return render(request,
                  'carMng/car_detail.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'car': car,
                  })


def myCars(request):
    cars = Car.objects.filter(username=request.user)
    for c in cars:
        c.pic_path = c.picture.url[18:]
    return render(request,
                  'carMng/myCars.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'cars': cars,
                  }
                  )


def carDelete(request, car_id):
    car = Car.objects.get(id=car_id)
    car.delete()
    return render(request,
                  'carMng/carDelete.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'car': car,
                  }
                  )


def search(request):
    query = request.GET.get('query', '')
    cars = (Car.objects.filter(model__icontains=query) | Car.objects.filter(make__icontains=query)
            | Car.objects.filter(year__icontains=query))
    for c in cars:
        c.pic_path = c.picture.url[18:]
    return render(request,
                  'carMng/search.html',
                  {
                      'item_list': MainMenu.objects.all(),
                      'cars': cars,
                  }
                  )
