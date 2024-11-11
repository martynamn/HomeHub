import calendar
from typing import List

from django.http import JsonResponse

from myapp.models import Property


def get_dashboard(user_id: str):
    properties = list(Property.objects.filter(userId=user_id).exclude(adType='sold').values())
    dashboard = [
        {
            "name": 'sale',
            'value': count_ad_type(properties, 'sale')
        },
        {
            "name": 'rent',
            'value': count_ad_type(properties, 'rent')
        },
        {
            "name": 'country',
            'value': count_locations(properties, 'country')
        },
        {
            "name": 'city',
            'value': count_locations(properties, 'city')
        }
    ]

    return JsonResponse(dashboard, safe=False)


def get_revenue_for_year(year: int, user_id: str):
    properties = list(Property.objects.filter(userId=user_id).values())
    property_for_current_year = get_properties_for_year(properties, year)
    property_for_last_year = get_properties_for_year(properties, year - 1)

    revenue = 0
    dashboard_revenue = {
        "currentYear": [],
        "lastYear": [],
        "totalRevenue": 0
    }

    for i in range(1, 13):
        current_year_data = {
            'revenue': get_revenue_for_month(property_for_current_year, i),
            'month': calendar.month_abbr[i],
            'year': year
        }

        last_year_data = {
            'revenue': get_revenue_for_month(property_for_last_year, i),
            'month': calendar.month_abbr[i],
            'year': year - 1
        }

        dashboard_revenue["currentYear"].append(current_year_data)
        dashboard_revenue["lastYear"].append(last_year_data)
        revenue += current_year_data['revenue'] + last_year_data['revenue']

    dashboard_revenue["totalRevenue"] = revenue

    response = JsonResponse(dashboard_revenue, safe=False)
    return response


def count_locations(properties: List[Property], name: str) -> int:
    return len(set(property.get('address').get(name) for property in properties if
                   property.get('address') and property.get('address').get(name)))


def count_ad_type(properties: List[Property], ad_type: str) -> int:
    return sum(1 for property in properties if property.get('adType') == ad_type)


def get_properties_for_year(properties, year):
    property_for_year = []
    for property in properties:
        creation_date = property.get('creationDate')
        if creation_date and creation_date.year == year:
            property_for_year.append(property)
    return property_for_year


def get_revenue_for_month(properties, month):
    return sum(obj.get('price') for obj in properties if
               obj.get('creationDate') and obj['creationDate'].month == month and obj.get('adType') == 'sold')
