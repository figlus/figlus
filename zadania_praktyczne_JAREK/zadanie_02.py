import requests
import Zadanie_1

# Korzystając z dokumentacji REST API Allegro oraz z napisanej w zadaniu pierwszym funkcji
# spróbuj wysłać zapytanie do Allegro które zwróci JSON z wyszukiwaniem przedmiotu który cię interesuje.
# zwróć uwagę na strukture otrzymanej odpowiedzi, spróbój wyciągnąć z niej same przedmioty promowane*
# Pomocna okaże się dokumentacja Allegro do której link znajduje się niżej, oraz zaimportowana biblioteka requests
# https://developer.allegro.pl/listing/


def get_some_offers():
    search_url = "https://api.allegro.pl" + "/offers/listing"
    access_token = Zadanie_1.get_access_token()
    headers = {"charset": "utf-8", "Accept-Language": "pl-PL", "Content-Type": "application/json",
               "Accept": 'application/vnd.allegro.public.v1+json',
           	   "Authorization:" "Bearer {}".format(access_token)}
               # w powyższym słowniku został wykasowany ważny wpis pola nagłówka, kojarzy się z misiem po angielsku
               # w razie problemów proszę patrzeć do dokumentacji Allegro REST API lub pytać


    parameters = {'phrase': 'cisco'}
    with requests.Session() as session:
    	session.headers.update(headers)
		##
    	response = session.get(search_url, parameters=parameters)
    	data = response.json()

    return data['items']['promoted']
    # by elegancko wcisnąć do requesta nagłówek, można otworzyć coś czego studenci boją się najbardziej
    # i wypada na koniec semestru - patrz do dokumentacji biblioteki requests