# using flask_restful 
from flask import Flask, jsonify, request, Response, json
from flask_restful import Resource, Api, reqparse
from app import initiate_analysis_process
# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class ProcessAPI(Resource): 
    
    # corresponds to the GET request. 
    # this function is called whenever there 
    # is a GET request for this resource 
    def get(self):
        print(request.data)
        return {'message': request.form.get("type")}
  
    # Corresponds to POST request 
    def post(self):
        video_link = request.form.get("video_link")
        data = initiate_analysis_process(video_link)
        return {'task': "succesful", 'data': data}, 201
# adding the defined resources along with their corresponding urls 
api.add_resource(ProcessAPI, '/process') 

if __name__ == "__main__":
    app.run(debug = True)
