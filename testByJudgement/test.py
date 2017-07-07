import unittest
from flask import current_app, url_for,jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import json
class BasicTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_app_exist(self):
        self.assertFalse(current_app is None)


    def test_c_get_news(self):
        response = self.client.post(self):
          url_for('api.get_news',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_recommend_news(self):
        response = self.client.post(self):
          url_for('api.recommend_news',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_show_news(self):
        response = self.client.get(self):
          url_for('api.show_news',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_add_news(self):
        response = self.client.post(self):
          url_for('api.add_news',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_update_news(self):
        response = self.client.XXXX(self):
          url_for('api.update_news',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_news_body(self):
        response = self.client.get(self):
          url_for('api.get_news_body',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_update_news_body(self):
        response = self.client.XXXX(self):
          url_for('api.update_news_body',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_delete_news(self):
        response = self.client.XXXX(self):
          url_for('api.delete_news',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_pic(self):
        response = self.client.post(self):
          url_for('api.get_pic',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_recommend_pics(self):
        response = self.client.post(self):
          url_for('api.recommend_pics',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_show_pic(self):
        response = self.client.get(self):
          url_for('api.show_pic',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_add_pics(self):
        response = self.client.post(self):
          url_for('api.add_pics',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_update_pics(self):
        response = self.client.XXXX(self):
          url_for('api.update_pics',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_delete_pics(self):
        response = self.client.XXXX(self):
          url_for('api.delete_pics',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_delete_one_pic(self):
        response = self.client.XXXX(self):
          url_for('api.delete_one_pic',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_interaction(self):
        response = self.client.post(self):
          url_for('api.get_interaction',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_recommend_interactions(self):
        response = self.client.post(self):
          url_for('api.recommend_interactions',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_get_tea(self):
        response = self.client.get(self):
          url_for('api.get_tea',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_show_interaction(self):
        response = self.client.get(self):
          url_for('api.show_interaction',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_add_interaction(self):
        response = self.client.post(self):
          url_for('api.add_interaction',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_update_interaction(self):
        response = self.client.get(self):
          url_for('api.update_interaction',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_interaction_body(self):
        response = self.client.get(self):
          url_for('api.get_interaction_body',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_update_interaction_body(self):
        response = self.client.XXXX(self):
          url_for('api.update_interaction_body',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_delete_interaction(self):
        response = self.client.get(self):
          url_for('api.delete_interaction',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_set_tea(self):
        response = self.client.post(self):
          url_for('api.set_tea',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_get_token(self):
        response = self.client.get(self):
          url_for('api.get_token',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_profile(self):
        response = self.client.post(self):
          url_for('api.get_profile',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_edit_profile(self):
        response = self.client.get(self):
          url_for('api.edit_profile',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_works(self):
        response = self.client.get(self):
          url_for('api.get_works',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_collections(self):
        response = self.client.get(self):
          url_for('api.get_collections',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_suggeston(self):
        response = self.client.post(self):
          url_for('api.suggeston',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_collect(self):
        response = self.client.post(self):
          url_for('api.collect',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_collect_delete(self):
        response = self.client.post(self):
          url_for('api.collect_delete',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_get_comments(self):
        response = self.client.get(self):
          url_for('api.get_comments',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_create_comments(self):
        response = self.client.post(self):
          url_for('api.create_comments',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_get_comment_likes(self):
        response = self.client.XXXX(self):
          url_for('api.get_comment_likes',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_delete_comment(self):
        response = self.client.get(self):
          url_for('api.delete_comment',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_main_page(self):
        response = self.client.get(self):
          url_for('api.main_page',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_search(self):
        response = self.client.post(self):
          url_for('api.search',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_get_hottag(self):
        response = self.client.get(self):
          url_for('api.get_hottag',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_list(self):
        response = self.client.get(self):
          url_for('api.list',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_publish(self):
        response = self.client.post(self):
          url_for('api.publish',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_unpublish(self):
        response = self.client.post(self):
          url_for('api.unpublish',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_a_register(self):
        response = self.client.post(self):
          url_for('api.register',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_b_login(self):
        response = self.client.post(self):
          url_for('api.login',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_change_to_author(self):
        response = self.client.get(self):
          url_for('api.change_to_author',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_change_to_common_user(self):
        response = self.client.get(self):
          url_for('api.change_to_common_user',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_article(self):
        response = self.client.post(self):
          url_for('api.get_article',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_recommend_articles(self):
        response = self.client.post(self):
          url_for('api.recommend_articles',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_show_article(self):
        response = self.client.get(self):
          url_for('api.show_article',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_add_article(self):
        response = self.client.post(self):
          url_for('api.add_article',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_update_article(self):
        response = self.client.XXXX(self):
          url_for('api.update_article',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_get_article_body(self):
        response = self.client.get(self):
          url_for('api.get_article_body',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_update_article_body(self):
        response = self.client.XXXX(self):
          url_for('api.update_article_body',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_delete_article(self):
        response = self.client.get(self):
          url_for('api.delete_article',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_light(self):
        response = self.client.post(self):
          url_for('api.light',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_like_picture(self):
        response = self.client.post(self):
          url_for('api.like_picture',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_like_comment(self):
        response = self.client.post(self):
          url_for('api.like_comment',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)

    def test_c_get_everydaypic(self):
        response = self.client.get(self):
          url_for('api.get_everydaypic',_external=True),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
    def test_c_add_everydaypic(self):
        response = self.client.post(self):
          url_for('api.add_everydaypic',_external=True),
          data = json.dump({ #Need complete}),
          content_type = 'application/json')
        self.assertTrue(response.status_code == 200)
