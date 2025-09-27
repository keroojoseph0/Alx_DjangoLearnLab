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


## Advanced Query Capabilities for Book API

As part of the `advanced_api_project`, the Book API now supports **filtering**, **searching**, and **ordering** to enhance usability and provide flexible data access.

---

### 🔎 Filtering
Users can filter the book list by **title**, **author**, and **publication_year**.

**Examples:**
- Get books published in 2023:  
- Get books by a specific author (ID or FK value):  
- Get books with a specific title:  

---

### 🔍 Searching
Search functionality is enabled on **title** and **author name** fields.

**Examples:**
- Search books by keyword in title:  
- Search books by author name:  

---

### ↕️ Ordering
Users can order results by **title** or **publication_year**.  
Prefix with `-` for descending order.

**Examples:**
- Order by title (ascending):  

---

### ✅ Combined Usage
Filtering, searching, and ordering can be combined in one request.

**Example:**
👉 Gets books by author with ID `1`, containing the keyword "python" in title or author name, ordered by newest publication year first.

---

### 📌 Notes
- Filtering is powered by `DjangoFilterBackend`.  
- Searching is powered by `SearchFilter`.  
- Ordering is powered by `OrderingFilter`.  
- Default ordering is set to **title** (ascending).
