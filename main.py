from flask import Flask
from mongoengine import *
from dotenv import load_dotenv
from library import jsonify
from ml_model import create_model
from models import ProjectMetadata

app = Flask(__name__)
connection = connect('exl')

load_dotenv()

@app.route("/create_model", methods=['POST'])
def create_model_view():
    project_metadata_id = create_model()
    return jsonify({
        "message": "Model Created",
        "project_metadata_id": str(project_metadata_id)
        })
    
    
@app.route("/get_project_metadata", methods=['GET'])
def get_project_metadata():
    data = list(ProjectMetadata.objects().as_pymongo())
    return jsonify({
        "data": data
        })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
