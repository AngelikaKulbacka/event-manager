API, które będzie umożliwiało operacje na eventach ( operacje, które zachodzą w całym systemie).


Wyświetlenie listy eventów:
http://127.0.0.1:8000/events/


Dodawanie nowych jest obsługiwane za pomocą Postmana w którego wpisujemy przykładowy JSON:
{
    "name": "New event",
    "source": "users",
    "description": "This is a new event."
}

oraz pzrzed tym dodajemy w Headers KEY: Content-Type, VALUE: application/json.


