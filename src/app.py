from flask import Flask, request
from models.plate_reader import PlateReader
import logging
import requests
from plate_client import PlateClient
import PIL
import io

def read_bytes(bytes):
    im = io.BytesIO(bytes)
    try:
        result = plate_reader.read_text(im)
    except PIL.UnidentifiedImageError as err:
        print(err)
    return {'plate_number': result}

app = Flask(__name__)
plate_reader = PlateReader.load_from_file('./model_weights/plate_reader_model.pth')
plate_client = PlateClient(host_ip='127.0.0.1', host_port='8080')


@app.route('/')
def hello():
    return '<h1><center>Welcome to the plate recognizer!</center></h1>'

@app.route('/NumberReader', methods=["POST"])
def read_number():
    body = request.get_data()
    return read_bytes(body)

@app.route('/NumberByImageId')
def read_remote_image():
    image_id = request.args.get('id')
    try:
        result = plate_client.read_id_number(image_id)
    except Exception as err:
        print(err)
    return result

@app.route('/NumbersByImageIds')
def read_several_nums():
    ids = request.args.getlist('id')
    try:
        results = plate_client.read_several_nums(ids)
    except Exception as err:
        print(err)
    
    return {img_id:res for img_id, res in zip(ids, results)}


if __name__ == '__main__':
    logging.basicConfig(
        format='[%(levelname)s] [%(asctime)s] %(message)s',
        level=logging.INFO,
    )
    app.config['JSON_AS_ASCII'] = False
    app.run(host='0.0.0.0', port=8080, debug=True)
