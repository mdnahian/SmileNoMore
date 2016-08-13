from clarifai import rest
api = rest.ApiClient()
print api.getInputs(page=1, per_page=25)
