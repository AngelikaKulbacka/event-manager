# API, które będzie umożliwiało operacje na eventach ( operacje, które zachodzą w całym systemie).  


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
    name  
    uuid  
    source  
    createdAt  
    updatedAt  
    description  
  }  
}  

Link:  
http://127.0.0.1:8000/graphql?query={events{name, uuid, source, createdAt, updatedAt, description}}


(Zostały dodane dwa rodzaje filtrowania)

# Pobierz wszystkie eventy, w których name zawiera słowo "User"  
query {  
  event(nameContains: "User") {  
    id  
    name  
    source  
    createdAt  
    updatedAt  
    description  
  }  
}  

Link:  
http://127.0.0.1:8000/graphql?query=query{events(nameContains: "User"){id name source createdAt updatedAt description}}


# Pobierz eventy o podanym source
Link:  
http://127.0.0.1:8000/graphql?query=query{events(sourceContains: "admins"){id name source createdAt updatedAt description}}

query {  
  event(sourceContains: "admins") {  
    id  
    name  
    source  
    createdAt  
    updatedAt  
    description  
  }  
}  


# Dodaj nowy event
mutation {  
  createEvent(input: {name: "User created", source: "users", description: "Dodano użytkownika"}) {  
    event {  
      name  
      source  
      description  
    }  
  }  
}  


# Zapytanie z filtrowaniem po polu name, które zwraca wszystkie eventy, których nazwa zaczyna się od litery "U"
query {  
  events(name_Istartswith: "U") {  
    name  
    source  
    created_at  
    updated_at  
    description  
  }  
}  

