import os
import random, string
from clarifai import rest

def randomId():
	return ''.join(random.choice(string.lowercase) for i in range(6))

api = rest.ApiClient()

img_list = []

for img in os.listdir("img/"):
	img_list.append(rest.Image(file_obj=open("img/"+img), labels=['sad'], ID=randomId()))

print api.addInputs(img_list)
