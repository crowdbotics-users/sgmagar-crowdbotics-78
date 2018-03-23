from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

def home(request):
    packages = [
	{'name':'django-oauth-twitter', 'url': 'http://pypi.python.org/pypi/django-oauth-twitter/1.11'},
	{'name':'django-paypal', 'url': 'http://pypi.python.org/pypi/django-paypal/0.4.1'},
    ]
    context = {
        'title': 'sgmagar-crowdbotics-78',
        'packages': packages
    }
    return render(request, 'home/index.html', context)
