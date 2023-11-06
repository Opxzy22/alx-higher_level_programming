fetch('https://swapi-api.alx-tools.com/api/films/?format=json')
.then(response => response.json())
.then(data => { 
    moviestitle = data.results.map(movies => movies.title);
    title =moviestitle.join(",");
        $("ul#list_movies").append(title)
})