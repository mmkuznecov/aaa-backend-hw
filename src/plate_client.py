import requests

class PlateClient:
    def __init__(self, host_ip, host_port, storage_url='http://51.250.83.169:7878/images'):
        self.host_url = f'http://{host_ip}:{host_port}'
        self.storage_url = storage_url

    def number_reader(self, img):
        result = requests.post(
            f'{self.host_url}/NumberReader',
            headers={'Content-Type': 'application/x-www-form-urlencoded'},
            data=img)
        
        return result.json()
    
    def read_id_number(self, img_id):

        try:
            resp = requests.get(f'{self.storage_url}/{img_id}')
            resp.raise_for_status()

        # handling different exceptions here
        except requests.exceptions.HTTPError as errh:
            print("Http Error:", errh)
        except requests.exceptions.ConnectionError as errc:
            print("Error Connecting:", errc)
        except requests.exceptions.Timeout as errt:
            print("Timeout Error:", errt)

        return self.number_reader(resp.content)
        

    def read_several_nums(self, imgs_ids):
        return [self.read_id_number(img_id)['plate_number'] for img_id in imgs_ids]