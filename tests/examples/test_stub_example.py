# An interface for returning data from a client
class ExternalAPIClientInterface:
    def get_data(self):
        """ Returns data to the client. """
        pass

# A concrete implementation of the ExternalAPIClientInterface which returns canned responses
class ExternalAPIClientStub(ExternalAPIClientInterface):
    def get_data(self):
        # Actual implementation makes API call
        # For testing, we'll use a stub
        return "Stubbed API response"

# Test code using the stub
def test_external_api_interaction():
    external_api_stub = ExternalAPIClientStub()
       
    # Now, when the test code calls get_data, it gets the stubbed response
    assert external_api_stub.get_data() == "Stubbed API response"