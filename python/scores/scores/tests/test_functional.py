from unittest2 import TestCase
import webtest
from scores import views as scores_view

class FunctionalTest(TestCase):

    def setUp(self):
      self.app = webtest.TestApp("config:tests.ini", relative_to='.')
      scores_view.SCORES = {}

    def test_root_returns_hello(self):
      resp = self.app.get('/', status=200)
      self.assertEquals(resp.json, {'Hello': 'World'})

    def test_save_score_return_success(self):
      resp = self.app.post_json('/scores', {'score': 20}, status=201)
      self.assertIn('location', resp.headers)

    def test_api_rejects_unknown_scores(self):
      resp = self.app.post('/scores', status=400)

    def test_api_can_store_new_score(self):
      resp = self.app.post_json('/scores', {'score': 20}, status=201)
      score_id = resp.headers['location'].split('/')[-1]

      scores = self.app.get('/scores', status=200).json['scores']
      self.assertIn(score_id, scores, "cannot find %s in scores" % score_id)

    def test_save_score_return_valid_url(self):
      resp = self.app.post_json('/scores', {'score': 20}, status=201)
      return_url = resp.headers['location']
      self.assertTrue(return_url.startswith("http://"))

    def test_list_score_is_return(self):
      resp = self.app.get('/scores',status=200)
      self.assertEquals(len(resp.json['scores']), 0)
