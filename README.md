# API, które będzie umożliwiało operacje na eventach ( operacje, które zachodzą w całym systemie).  

Uruchomienie:
wpisujemy w konsoli w projekcie:  
python manage.py runserver  


# 1.
Wyświetlenie listy eventów:  
http://127.0.0.1:8000/events/


Dodawanie nowych jest obsługiwane za pomocą Postmana w którego wpisujemy przykładowy JSON:  
{  
    "name": "New event",  
    "source": "users",  
    "description": "This is a new event."  
}  

oraz pzrzed tym dodajemy w Headers KEY: Content-Type, VALUE: application/json.  

 
# 2.
# Pobierz wszystkie eventy  
query {  
  events {  
    edges {  
        node {  
            name  
            uuid  
            source  
            createdAt  
            updatedAt  
            description  
            }  
        }  
    }
}

Link:  
http://127.0.0.1:8000/graphql?query={events{edges{node{name, uuid, source, createdAt, updatedAt, description}}}}  


# Dodaj nowy event
Aby zrobić to w Postmanie:  
1. Wyślij żądanie GET do dowolnego endpointu, aby otrzymać token CSRF. Znajdziesz go w ciasteczkach jako "csrftoken".  
2. Skopiuj wartość csrftoken z ciasteczka.  
3. W żądaniu POST dodaj nagłówek o nazwie "X-CSRFToken" i wartości wcześniej skopiowanego tokena.  

mutation {
  createEvent(input: {name: "Testowy drugi event", source: "Testowe zrodlo", description: "Opis drugiego testowego eventu"}) {
    event {
      name
      uuid
      source
      createdAt
      updatedAt
      description
    }
  }
}


# Usuń event w przypisanym uuid
(w Postman)

mutation {
  deleteEvent(eventUuid: "ece69731-3d2e-4604-a833-4ebb0aafb55b") {
    success
  }
}


# Modyfikacja wybranego eventu po wpisanym uuid
mutation {
  updateEvent(eventUuid: "65bdd93d-8aad-455c-8323-354b9afba112", input: { name: "Nowa nazwa", source: "Nowe zrodlo", description: "Opis eventu" }) {
    event {
      id
      name
      source
      description
    }
  }
}


# Pobierz wszystkie eventy, w których name jest równe "Ania created"
query {  
  events(name: "Ania created") {  
    edges {  
        node {  
            name  
            uuid  
            source  
            createdAt  
            updatedAt  
            description  
            }  
        }  
    }
} 

Link:  
http://127.0.0.1:8000/graphql?query={events(name: "Ania created"){edges{node{name, uuid, source, createdAt, updatedAt, description}}}}  


# Pobierz wszystkie eventy, w których name zawiera słowo "User"  
query {  
  events(name_Icontains: "User") {  
    edges {  
        node {  
            name  
            uuid  
            source  
            createdAt  
            updatedAt  
            description  
            }  
        }  
    }
} 

Link:  
http://127.0.0.1:8000/graphql?query={events(name_Icontains: "User"){edges{node{name, uuid, source, createdAt, updatedAt, description}}}}  


# Pobierz eventy, w których source zaczyna się literą "a"
query {  
  events(source_Istartswith: "a") {  
    edges {  
        node {  
            name  
            uuid  
            source  
            createdAt  
            updatedAt  
            description  
            }  
        }  
    }
} 


Link:  
http://127.0.0.1:8000/graphql?query={events(source_Istartswith: "a"){edges{node{name, uuid, source, createdAt, updatedAt, description}}}}  


# Pobierz eventy, w których name jest równy "User created" i description zaczyna się literą "D"
query {  
  events(name: "User created", description_Istartswith: "D") {  
    edges {  
        node {  
            name  
            uuid  
            source  
            createdAt  
            updatedAt  
            description  
            }  
        }  
    }
} 


Link:  
http://127.0.0.1:8000/graphql?query={events(name: "User created", description_Istartswith: "D"){edges{node{name, uuid, source, createdAt, updatedAt, description}}}}  


# Posortuj eventy rosnąco po "created_at"
Link:  
http://127.0.0.1:8000/graphql?query={events(orderBy: "created_at"){edges{node{name, uuid, source, createdAt, updatedAt, description}}}}


# Posortuj eventy malejąco po "created_at"
Link:  
http://127.0.0.1:8000/graphql?query={events(orderBy: "-created_at"){edges{node{name, uuid, source, createdAt, updatedAt, description}}}}


# Posortuj eventy rosnąco po "updated_at"
Link:  
http://127.0.0.1:8000/graphql?query={events(orderBy: "updated_at"){edges{node{name, uuid, source, createdAt, updatedAt, description}}}}


# Posortuj eventy malejąco po "updated_at"
Link:  
http://127.0.0.1:8000/graphql?query={events(orderBy: "-updated_at"){edges{node{name, uuid, source, createdAt, updatedAt, description}}}}


# Pobieranie konkretnego eventu gdzie argumentem jest “event_uuid”
Link:  
http://127.0.0.1:8000/graphql?query={eventByUuid(uuid: "67ae47bd-d4f3-40aa-b7ba-990759a27a6d"){name, source, description}}


# Obsługa błędu w przypadku, gdy nie znajdzie eventu po danym uuid
Link:  
http://127.0.0.1:8000/graphql?query={eventByUuid(uuid: "66ae47bd-d4f3-40aa-b7ba-990759a27a6d"){name, source, description}}



