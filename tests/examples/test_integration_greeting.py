# test_integration_greeting.py
import unittest
import threading
import time
from backend import app
from frontend import send_greeting_request

class IntegrationTest(unittest.TestCase):    
    
    @classmethod
    def setUpClass(cls):
        global server
                
        # Start the Flask app in a separate thread for testing        
        cls.server_thread = threading.Thread(target=app.run, kwargs={'port': 5111})
        cls.server_thread.daemon = True
        cls.server_thread.start()
        
        # Allow time for the server to start
        time.sleep(3)
        
    @classmethod
    def tearDownClass(cls):
        cls.server_thread.join(1)

    def test_greeting_integration(self):
        # Call the frontend function, which sends a request to the running backend        
        result = send_greeting_request()

        # Verify the result from the frontend function
        self.assertEqual(result, {'message': 'Hello, Guest!'})