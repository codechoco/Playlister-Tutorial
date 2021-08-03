# tests.py

from unittest import TestCase, main as unittest_main
from app import app
# Add this new import
from bson.objectid import ObjectId
from app import app, video_url_creator
sample_id_list = ['hY7m5jjJ9mM','CQ85sUNBK7w']
# All of these are new mock data that we'll use
sample_playlist_id = ObjectId('5d55cffc4a3d4031f42827a3')
sample_playlist = {
    'title': 'Cat Videos',
    'description': 'Cats acting weird',
    'videos': [
        'https://youtube.com/embed/hY7m5jjJ9mM',
        'https://youtube.com/embed/CQ85sUNBK7w'
    ],
    'video_ids': ['hY7m5jjJ9mM','CQ85sUNBK7w']
}
sample_form_data = {
    'title': sample_playlist['title'],
    'description': sample_playlist['description'],
    'videos': '\n'.join(sample_playlist['video_ids'])
}
class PlaylistsTests(TestCase):
    """Flask tests."""

    def setUp(self):
        """Stuff to do before every test."""

        # Get the Flask test client
        self.client = app.test_client()

        # Show Flask errors that happen during tests
        app.config['TESTING'] = True
    """def test_index(self):
    	result = self.client.get('/')
    	self.assertEqual(result.status, '200 OK')
    def test_new(self):
    	result = self.client.get('/playlists/new')
    	self.assertEqual(result.status, '200 OK')"""
    def test_video_url_creator(self):
    	expected_list = ['https://youtube.com/embed/hY7m5jjJ9mM', 'https://youtube.com/embed/CQ85sUNBK7w']
    	output_list = video_url_creator(sample_id_list)
    	self.assertEqual(expected_list, output_list)
    @mock.patch('pymongo.collection.Collection.find_one')
    def test_show_playlist(self, mock_find):
    	mock_find.return_value = sample_playlist
    	result = self.client.get(f'/playlists/{sample_playlist_id}')
    	self.assertEqual(result.status, '200 OK')
		
if __name__ == '__main__':
    unittest_main()