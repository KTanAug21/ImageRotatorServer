from flask import Flask,request,json, send_file
from flask_cors import CORS
from image.service import Service as ImageService

app = Flask(__name__)
CORS(app)

"""
USERS
"""
@app.route("/upload", methods=["POST"])
def image_create():
  
  # get the file from request
  file = request.files['file']

  if file.filename == '':
    return json_response({'error':'No file'},422)

  # save file locally
  meta_data = ImageService().save_file_to_local( file )

  # respond
  return send_file(meta_data['rotated'], mimetype='image/png'),200


def json_response(payload, status=200):
  return (json.dumps(payload), status, {'content-type': 'application/json'})

if __name__ == "__main__":
    app.run(debug=True)