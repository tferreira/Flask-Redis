from testing_config import BaseTestConfig


class TestAPI(BaseTestConfig):

    def test_get_index(self):
        result = self.app.get("/api/status")
        self.assertEqual(result.status_code, 200)
