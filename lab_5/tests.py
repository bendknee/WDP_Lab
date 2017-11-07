from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, add_todo
from .models import Todo
from .forms import Todo_Form

# Create your tests here.
class Lab5UnitTest(TestCase):

    def test_lab_5_url_is_exist(self):
        response = Client().get('/lab-5/')
        self.assertEqual(response.status_code, 200)

    def test_lab5_using_index_func(self):
        found = resolve('/lab-5/')
        self.assertEqual(found.func, index)

    def test_model_can_create_new_todo(self):
        # Creating a new activity
        new_activity = Todo.objects.create(title='mengerjakan lab ppw', description='mengerjakan lab_5 ppw')

        # Retrieving all available activity
        counting_all_available_todo = Todo.objects.all().count()
        self.assertEqual(counting_all_available_todo, 1)

    def test_form_todo_input_has_placeholder_and_css_classes(self):
        form = Todo_Form()
        self.assertIn('class="todo-form-input', form.as_p())
        self.assertIn('id="id_title"', form.as_p())
        self.assertIn('class="todo-form-textarea', form.as_p())
        self.assertIn('id="id_description', form.as_p())

    def test_form_validation_for_blank_items(self):
        form = Todo_Form(data={'title': '', 'description': ''})
        self.assertFalse(form.is_valid())
        self.assertEqual(
            form.errors['description'],
            ["This field is required."]
        )
    def test_lab5_post_success_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/lab-5/add_todo', {'title': test, 'description': test})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/lab-5/')
        html_response = response.content.decode('utf8')
        self.assertIn(test, html_response)

    def test_lab5_post_error_and_render_the_result(self):
        test = 'Anonymous'
        response_post = Client().post('/lab-5/add_todo', {'title': '', 'description': ''})
        self.assertEqual(response_post.status_code, 302)

        response= Client().get('/lab-5/')
        html_response = response.content.decode('utf8')
        self.assertNotIn(test, html_response)
