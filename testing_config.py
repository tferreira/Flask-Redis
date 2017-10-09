from flask_testing import TestCase
from application.app import app


class BaseTestConfig(TestCase):
    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app

    def setUp(self):
        self.app = self.create_app().test_client()

        # self.app.post(
        #     "/api/create-something",
        #     data=json.dumps(self.default_data),
        #     content_type='application/json',
        #     headers={'Authorization': self.token}
        # )

    def tearDown(self):
        pass
