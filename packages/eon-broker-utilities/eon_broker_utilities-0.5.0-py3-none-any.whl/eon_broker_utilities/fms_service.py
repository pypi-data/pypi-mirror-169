import os 
import requests
import eon_logger.logging as log


cls = log.Logger('fms', 'debug')
_logger = cls.create_logger()


class ManageFiles():
    def __init__(self, config):
        self.fms_host = config['FMS_HOST'] or '10.1.0.5'
        self.fms_port = config['FMS_PORT'] or '8007'
        self.fms_url = f"{self.fms_host}:{self.fms_port}"
        self.base_location = os.getcwd()
        
    def download_file(self, file_key, location):
        url = f"http://{self.fms_url}/{file_key}"
        with requests.get(url, stream=True) as response:
            response.raise_for_status()
            ext = response.headers['x-ext'].replace('.','')
            file_location = os.path.join(self.base_location, f"{location}/{file_key}.{ext}")
            with open(file_location, 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024): 
                    file.write(chunk)
            response.close()
        _logger.info(f"File Downloaded Successfully {file_key}.{ext}")
        return f"File Donwloaded Successfully {file_key}.{ext}"

    def upload_file(self, file_key, ext, location, group, created_by):
        url = f"http://{self.fms_url}/{file_key}"
        file_location = os.path.join(self.base_location, f"{location}/{file_key}.{ext}")
        headers = {'content-type': 'application/octet-stream',
                    'x-ext': ext, 'x-group': group, 'x-createdBy': created_by}
        file_request = requests.Session()
        with open(file_location, 'rb') as file:
            with file_request.post(url, file, headers=headers, stream=True) as req:
                req.raise_for_status()
        file_request.close()
        _logger.warning(f"File Uploaded Successfully {file_key}.{ext}")
        return f"File Uploaded Successfully {file_key}.{ext}"
        

    def delete_file(self, file_key, ext, location): 
        os.remove(os.path.join(self.base_location, f"{location}/{file_key}.{ext}"))
        _logger.info(f"File Deleted Successfully {file_key}.{ext}")
        return f"File Deleted Successfully {file_key}.{ext}"

import configparser
config = configparser.ConfigParser()
config.read("broker_config.ini")
config.sections()


fms_host = "10.1.0.5"
fms_port = "8007"
config_file = os.getenv("CONFIG_FILE") or 'broker_config.ini'
fms_dict = {
    "FMS_HOST": fms_host,
    "FMS_PORT": fms_port
}



cls = FilesManager(fms_dict)
print("Downloading file...")
cls.download_file("small-case", '/')
