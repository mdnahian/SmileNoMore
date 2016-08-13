from clarifai import rest
api = rest.ApiClient()
print api.searchInputs(image=rest.Image(file_obj=open('img/sad.png')))
