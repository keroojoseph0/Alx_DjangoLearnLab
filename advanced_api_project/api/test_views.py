from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create user for authentication
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client = APIClient()

        # Create authors
        self.author1 = Author.objects.create(name="J.R.R. Tolkien")
        self.author2 = Author.objects.create(name="Mark Lutz")

        # Create books
        self.book1 = Book.objects.create(title="The Hobbit", author=self.author1, publication_year=1937)
        self.book2 = Book.objects.create(title="Learning Python", author=self.author2, publication_year=2021)

        # Endpoints
        self.list_url = reverse("book-list")   # Assuming your ListView is registered as 'book-list'
        self.detail_url = lambda pk: reverse("book-detail", kwargs={"pk": pk})

    # ---------------------------
    # CRUD TESTS
    # ---------------------------

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_create_book_requires_authentication(self):
        data = {"title": "New Book", "author": self.author1.id, "publication_year": 2023}
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Not logged in

        # Now authenticate
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_update_book(self):
        self.client.login(username="testuser", password="testpass123")
        url = self.detail_url(self.book1.id)
        data = {"title": "The Hobbit - Updated", "author": self.author1.id, "publication_year": 1937}
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "The Hobbit - Updated")

    def test_delete_book(self):
        self.client.login(username="testuser", password="testpass123")
        url = self.detail_url(self.book2.id)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # ---------------------------
    # FILTERING, SEARCHING, ORDERING
    # ---------------------------

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"publication_year": 1937})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_search_books_by_title(self):
        response = self.client.get(self.list_url, {"search": "Python"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "Learning Python")

    def test_search_books_by_author_name(self):
        response = self.client.get(self.list_url, {"search": "Tolkien"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["title"], "The Hobbit")

    def test_order_books_by_publication_year_desc(self):
        response = self.client.get(self.list_url, {"ordering": "-publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Learning Python")  # Newest first
