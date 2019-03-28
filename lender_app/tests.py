from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User
# Create your tests here.
class TestModuleClass():

    def setUp(self):
        user = User.objects.create_user('dan', 'le')
        Book.objects.create(title='book one', detail='detail one', user=user)
        Book.objects.create(title='book two', detail='detail two', user=user)
        Book.objects.create(title='book three', detail='detail three', user=user)
    
    def test_book_titles(self):
        one = Book.objects.get(title='book one')
        two = Book.objects.get(title='book two')
        self.assertEqual(one.title, 'book one')
        self.assertEqual(two.title, 'book two')
    def test_book_details(self):
        one = Book.objects.get(detail='book one')
        two = Book.objects.get(detail='book two')
        self.assertEqual(one.detail, 'book one')
        self.assertEqual(two.detail, 'book two')

class TestViews():

    def setUp(self):
        self.request = RequestFactory()

        self.user = User.objects.create_user('foo','bar')
        
        Book.objects.create(title='book one', detail='detail one', user=self.user)
        Book.objects.create(title='book two', detail='detail two', user=self.user)
        Book.objects.create(title='book three', detail='detail three', user=self.user)

    def test_book_list_view(self):
        from .views import book_list_view
        request = self.request.get('')
        request.user = self.user
        response = book_list_view(request)
        self.assertIn(b'book two', response.content)

    def test_book_detail_view():
        from .views import book_detail_view
        request = self.request.get('')
        request.user = self.user
        response = book_detail_view(request, f'{ Book.objects.get(title="title one").id }')
        self.assertEqual(response.status_code, 200)