import json

from fastapi import APIRouter, Path, Query, HTTPException, status
from schemas.books import BookBase, Book


router = APIRouter(prefix='/books', tags=['books'])

@router.get('/')
def get_all_books() -> list[Book]:
    """
    Obtiene todos los libros desde la base de datos
    """
    
    with open('database/db.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    return data['books']


@router.get('/search')
def get_books_by_query(page: int = Query(default=1, ge=1), per_page: int = Query(default=2, ge=1), title: str = Query(default=''), category: str = Query(default='')):
    """
    Obtener libros por consulta:

    - titulo
    - pagina
    - por pagina
    """

    with open('database/db.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    books = data['books']

    filtered_books = []

    for book in books:
        if title.lower() in book['title'].lower() and category.lower() in book['category'].lower() :
            filtered_books.append(book)

    limit = page * per_page
    offset = limit - per_page 

    return filtered_books[offset:limit]


@router.get('/{id}')
def get_book_by_id(id: int = Path()):
    """
    Obtener un libro por id
    """

    with open('database/db.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    books = data['books']

    for book in books:
        if book['id'] == id:
            return book
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail={'message': 'Book not found'}
    )


@router.post('/')
def create_book(book: BookBase):
    """
    Crear un libro:

    - title
    - category
    - year
    """

    with open('database/db.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    books = data['books']

    # generate new book
    new_book = {
        'id': len(books) + 1,
        'title': book.title,
        'category': book.category,
        'year': book.year
    }

    # insertamos el nuevo libro
    books.append(new_book)

    # actualizamos toda la propiedad books
    data['books'] = books

    with open('database/db.json', 'w', encoding='utf-8') as file:
        data = json.dump(data, file, indent=4)

    return {'message': 'Book created'}


@router.put('/{id}')
def update_book_by_id(book: BookBase, id: int = Path()):
    """
    Actualizar libro porm id

    - id: viene por parametro
    - title: viene en el body de la peticion
    - category: viene en el body de la peticion
    - year: viene en el body de la peticion
    """

    with open('database/db.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    books = data['books']

    for index in range(len(books)):
        curr_book = books[index]

        if curr_book['id'] == id:
            curr_book['title'] = book.title
            curr_book['category'] = book.category
            curr_book['year'] = book.year
            
            # actualizamos el libro por posicion
            books[index] = curr_book

            break
        
        # si llega a la ultima posicion y el libro no existe ejecuta este codigo
        if index == len(books) - 1:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={'message': 'Book not found'})

    data['books'] = books

    with open('database/db.json', 'w', encoding='utf-8') as file:
        data = json.dump(data, file, indent=4)

    return {'message': 'Book updated'}


@router.delete('/{id}')
def delete_book_by_id(id: int = Path()):
    """
    Borrar libro por id
    """

    with open('database/db.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    books = data['books']

    for index in range(len(books)):
        curr_book = books[index]

        if curr_book['id'] == id:
            del books[index]

            data['books'] = books

            with open('database/db.json', 'w', encoding='utf-8') as file:
                data = json.dump(data, file, indent=4)

            return {'message': 'Book deleted'}
        
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, 
        detail={'message': 'Book not found'}
    )

