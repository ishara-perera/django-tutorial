from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.

monthly_challenges = {
    'january': 'God First',
    'february': 'Build a Website using Django for LKR 150K',
    'march': 'No liquor',
    'april': 'Be Patient',
    'may': 'Virtusa Engineering First',
    'june': 'Business First',
    'july': 'AI Learning',
    'august': 'Angular Learning',
    'september': 'Work for promotion',
    'october': 'Get the Promotion',
    'november': 'Fill the bank account with $ 100k',
    'december': 'Get a vehicle and repair house'
}

def home(request):
    list_items = ''
    month_list = list(monthly_challenges.keys())
    
    for month in month_list:
        capitalized_month = month.capitalize()
        redirect_month = reverse('month', args=[month])
        list_items += f'<li><a href={redirect_month}>{capitalized_month}</a></li>'
    
    response_data = f'<ul>{list_items}</ul>'
    return HttpResponse(response_data)

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound('This month is not supported!')
    redirect_month = months[month-1]
    redirect_path = reverse('month', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    # challenge_txt = None
    # for m,c in monthly_challenges.items():
    #     if month == m:
    #         challenge_txt = c
    #         return HttpResponse(challenge_txt)
    # return HttpResponseNotFound()
    try:
        challenge_txt = monthly_challenges[month]
        response_data = f'<h1>{challenge_txt}</h1>'
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound('This month is not supported!')
