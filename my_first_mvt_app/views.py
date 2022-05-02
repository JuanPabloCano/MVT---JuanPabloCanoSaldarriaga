import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from .models import Relatives


# Create your views here.


def relatives(request):
    relatives_instances()
    relatives_list = Relatives.objects.all()
    context = {'relatives': relatives_list}
    template = loader.get_template('relatives.html')
    template_render = template.render(context)
    return HttpResponse(template_render)


def relatives_instances():
    mom = Relatives(name="María",
                    last_name="Smith",
                    age=45,
                    email="maria@gmail.com",
                    birthday=datetime.date(1977, 2, 19),
                    family_relationship="Madre", )
    dad = Relatives(name="John",
                    last_name="Doe",
                    age=50, email="jhon@gmail.com",
                    birthday=datetime.date(1972, 6, 25),
                    family_relationship="Padre")
    sister = Relatives(name="Sofie",
                       last_name="Doe",
                       age=20,
                       email="sofie@gmail.com",
                       birthday=datetime.date(2002, 9, 17),
                       family_relationship="Hermana")
    mom.save()
    dad.save()
    sister.save()
    return mom, dad, sister
