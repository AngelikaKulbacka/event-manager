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
