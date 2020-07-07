# Emotion-Recognition-CNN-Master
Pre-req: 
    Python
    Pip
    execute <pip install -r requirements.txt>

Running the application: 
    cd application
    python app.py 
    This will open a default windows based app with webcam, to recognize emotional gesture and detect pulse.
 
Files named flask_app.py and flask_cam.py are created for video feed from web. Video feed is currently succeeding, but need to connect the model to the video stream.
 

Folder Structure and Module details:
    The classes are modular and can be plugged with any language. 
    Folder: application --> app.py   -> file with native windows gui to start the model
    flask_app.py --> web based video feed. (file still under construction)
    Folder: lib
    cam.py --> contains camera class, which can be used to open a webcam
    emotions.py --> emotion class, to label emotions
    processing.py --> Contains class to Identify pulse