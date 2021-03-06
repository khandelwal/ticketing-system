import json

from django.shortcuts import render
from django.http import HttpResponse

from recordlocator import generator

def record_locators(request):
    """ View that generates at least one record locator, generating 'n' if
    specified through a query parameter. """

    num_locators = int(request.GET.get('n', 1))

    record_locators = generate_locators(num_locators)
    data = {'record_locators': record_locators}
    response = json.dumps(data)
 
    return HttpResponse(response, content_type='application/json')


def generate_locators(n=1):
    """ Generate 'n' unique record locators. """

    record_locators = [generator.safe_generate() for r in range(0, n)]
    return record_locators
