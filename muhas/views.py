from django.shortcuts import render
from .forms import StudentForm
from time import strftime, gmtime

# Create your views here.

def index_view(request):
    form = StudentForm()
    if request.method == 'POST':
        print(request.POST)
    
    context = {
        'form': form
    }
    return render(request, 'muhas/index.html', context)

def data_received(request):
    if request.method == 'POST':
        print(request.POST)
    
    
    """if request.POST.get('action') == 'post':
        moment = strftime("%d%m%Y", gmtime())
        print('its a post request')
        name = request.POST['image'].split('\\')
        passport_name = f"{name[-1].split('.')[0]}-{moment}"
        request.POST['passport_name'] = passport_name
        print(request.POST)
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
        #school = request.POST['school']"""


def welcome_view(request):
    return render(request, 'muhas/welcome.html')


def select_view(request):
    return render(request, 'muhas/select.html')


def preview_view(request):
    return render(request, 'muhas/preview.html')