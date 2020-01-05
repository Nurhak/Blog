from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post


class ApiTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='testUser',
            password='12345'
        )

        test_user.save()

        test_post = Post.objects.create(
            author=test_user,
            title='auto_title',
            body='test_body...',
            summary='test_summary...'
        )

        test_post.save()

    def test_content(self):

        post = Post.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        summary = f'{post.summary}'
        self.assertEqual(author, 'testUser')
        self.assertEqual(title, 'auto_title')
        self.assertEqual(body, 'test_body...')
        self.assertEqual(summary, 'test_summary...')
