
def format_city_country(city, country, population=''):
    """Formats the city and country nicely"""

    if population:
        formatted_name = f"{city}, {country}-population:{population}"
    else:
        formatted_name = f"{city}, {country}"
    return formatted_name.title()

print(format_city_country('denver','united states',5000000))