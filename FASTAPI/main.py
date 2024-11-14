from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "FastAPI Curso Platzi"
app.version = "0.0.1"

movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción"
    }
]


@app.get("/", tags=['Home'])
async def root():
    return HTMLResponse('<h1>Welcome to FastAPI</h1>')

@app.get('/movies', tags=['Movies'])
async def get_movies():
    return movies

@app.get('/movies/{id}', tags=['Movies'])
async def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item
    return {'message': 'Movie not found'}


@app.get('/movies/', tags=['Movies'])
async def get_movies_by_category(category: str):
    result = []
    for item in movies:
        if item['category'] == category:
            result.append(item)
    
    if len(result) == 0:
        return {'message': 'No movies found'}
    return result

@app.post('/movies', tags=['Movies'])
async def create_movie(title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({'id': len(movies) + 1, 
                   'title': title, 
                   'overview': overview, 
                   'year': year, 'rating': rating, 
                   'category': category})
    return movies

@app.put('/movies/{id}', tags=['Movies'])
async def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies:
        if item['id'] == id:
            item['title'] = title
            item['overview'] = overview
            item['year'] = year
            item['rating'] = rating
            item['category'] = category
            return item
    return {'message': 'Movie not found'}


@app.delete('/movies/{id}', tags=['Movies'])
async def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return {'message': 'Movie deleted'}
    return {'message': 'Movie not found'}