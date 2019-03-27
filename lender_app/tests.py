from django.test import TestCase

# Create your tests here.
class TestClass():

    def test_book_list_view(self):
        rv = app.test_client().get('')
        assert rv.status_code == 200
        assert b'<h2>Book list</h2>' in rv.data

    def test_book_detail_view():
        rv = app.test_client().get('')
        assert rv.status_code == 200
        assert b'<h2>Book Detail</h2>' in rv.data