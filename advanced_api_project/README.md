# Book API Views

## Endpoints
- GET /api/books/ → List all books (open to everyone)
- GET /api/books/<id>/ → Retrieve single book (open to everyone)
- POST /api/books/create/ → Create book (authenticated only)
- PUT /api/books/<id>/update/ → Update book (owner only)
- DELETE /api/books/<id>/delete/ → Delete book (owner only)

## Permissions
- Read (List, Detail) → Anyone
- Create, Update, Delete → Authenticated users
- Update/Delete restricted to the book’s owner
