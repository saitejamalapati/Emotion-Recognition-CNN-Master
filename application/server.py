# using flask_restful 
from flask import Flask, jsonify, request, Response, json
from flask_restful import Resource, Api, reqparse
from app import initiate_analysis_process
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = ''
ALLOWED_EXTENSIONS = {'mp4'}
# creating the flask app 
app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
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
        try:
            if 'video' not in request.files:
                return {'status': "failure", 'message': 'Video file is missing'}, 400
            uploadedVideo = request.files["video"]
            if uploadedVideo and allowed_file(uploadedVideo.filename):
                try:
                    securedFilename = secure_filename(uploadedVideo.filename)
                    uploadedVideo.save(securedFilename)
                    data = initiate_analysis_process(securedFilename)
                    return {'status': "succesful", 'data': data, "message": "SAved Video and processed it successfully"}, 200
                except:
                    return {'status': "failure", 'message': "Failure with saving video and processing it"}, 500
            else:
                return {'status': "failure", 'message': 'Video not present'}, 500
        except:
            return {'status': "failure", 'message': 'Video save process exception'}, 500
# adding the defined resources along with their corresponding urls 
api.add_resource(ProcessAPI, '/process') 

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == "__main__":
    app.run(debug = True)
