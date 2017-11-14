from django.test import TestCase
from django.test import Client
from django.urls import resolve
from .views import index, paginate_page
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.db.models.manager import Manager
from unittest.mock import patch

from .models import Friend
from .api_csui_helper.csui_helper import CSUIhelper


class Lab6UnitTest(TestCase):
    def test_lab_7_url_is_exist(self):
        response = Client().get('/lab-7/')
        self.assertEqual(response.status_code, 200)

    def test_lab7_using_index_func(self):
        found = resolve('/lab-7/')
        self.assertEqual(found.func, index)

    def test_root_url_now_is_using_index_page_from_lab_7(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 301)
        self.assertRedirects(response, '/lab-7/', 301, 200)

    def test_friend_list_url_is_exist(self):
        response = Client().get('/lab-7/friend-list/')
        self.assertEqual(response.status_code, 200)

    def test_get_friend_list_data_url_is_exist(self):
        response = Client().get('/lab-7/get-friend-list/')
        self.assertEqual(response.status_code, 200)

    def test_auth_param_dict(self):
        csui_helper = CSUIhelper()
        auth_param = csui_helper.instance.get_auth_param_dict()
        self.assertEqual(auth_param['client_id'], csui_helper.instance.get_auth_param_dict()['client_id'])

    def test_add_friend(self):
        response_post = Client().post('/lab-7/add-friend/', {'name': "Ben ben", 'npm': "1606917550"})
        self.assertEqual(response_post.status_code, 200)

    def test_invalid_sso_tap_in(self):
        username = "dummy"
        password = "lab1103"
        csui_helper = CSUIhelper()
        with self.assertRaises(Exception) as context:
            csui_helper.instance.get_access_token(username, password)
        self.assertIn("dummy", str(context.exception))

    def test_validate_npm(self):
        response = self.client.post('/lab-7/validate-npm/')
        html_response = response.content.decode('utf8')
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(html_response, {'is_taken': False})

    def test_delete_friend(self):
        friend = Friend.objects.create(friend_name="Benny benyenybyenbye", npm="1606917550")
        response = Client().post('/lab-7/friend-list/delete-friend/' + str(friend.id) + '/')
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(friend, Friend.objects.all())

    def test_invalid_page_pagination_number(self):
        data = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15",
                "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29",
                "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44"]
        test1 = paginate_page("a String", data)
        test2 = paginate_page(-1, data)
        with patch.object(Manager, 'get_or_create') as wrong:
            wrong.side_effect = PageNotAnInteger("page number is not an integer")
            res = paginate_page("a String", data)
            self.assertEqual(res['page_range'], test1['page_range'])
        with patch.object(Manager, 'get_or_create') as wrong:
            wrong.side_effect = EmptyPage("page number is less than 1")
            res = paginate_page(-1, data)
            self.assertEqual(res['page_range'], test2['page_range'])
