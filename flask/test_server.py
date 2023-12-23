import unittest
from server import app  # Asegúrate de que esta importación sea correcta
import json

class FlaskServerTestCase(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_feedback_valid(self):
        # Enviar datos válidos
        response = self.client.post('/submit_feedback', data=json.dumps({
            "pagina": "Analisis",
            "calificacion": 5,
            "feedback": "Excelente página"
        }), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertIn("Feedback recibido", response.get_data(as_text=True))

    def test_feedback_invalid(self):
        # Enviar datos inválidos (faltan campos)
        response = self.client.post('/submit_feedback', data=json.dumps({
            "calificacion": 5
        }), content_type='application/json')

        self.assertEqual(response.status_code, 400)

if __name__ == '__main__':
    unittest.main()
