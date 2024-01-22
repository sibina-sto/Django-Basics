import datetime
import random

from django.shortcuts import render
from django.urls import reverse


class Person:
    def __init__(self, first_name, last_name, age=None):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


def index(request):
    person = Person(
        "John",
        "Doe",
    )
    context = {
        "title": "Employees list",  # valid
        "1as": "567",  # valid

        "new.employee": "John",  # invalid
        "new employee": "John",  # invalid
        "123": "456",  # invalid

        "person": {
            "first_name": "John",
            "last_name": "Doe",
        },
        "person_obj": person,
        "person_dict": person.__dict__,

        "names": ["John", "Gosho", "Maria"],
        "ages": [random.randrange(1, 100) for _ in range(10)],
        "ages_empty": [],

        "date": datetime.date.today(),
        "get_params": request.GET,
    }
    print(reverse('index'))

    print(context["person"]["first_name"])
    print(context["person"].items())

    return render(request, "employees/index.html", context)


def employee_details(request, pk):
    context = {
        "pk": pk,
    }

    return render(request, 'employees/details.html', context)
# ll = [1, 2, 3]
# for e in ll:
#     print(e)
