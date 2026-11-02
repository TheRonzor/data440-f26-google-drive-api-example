import os
import requests
import pandas as pd

# ABC stands for "Abstract Base Class"
from abc import ABC, abstractmethod

from dotenv import load_dotenv
load_dotenv('.env')

# An abstract class is a blueprint
# for all classes that are derived from it
class CatalogAPI(ABC):
    @abstractmethod
    def get_items(self) -> pd.DataFrame:
        '''Return the catalog as a pandas DataFrame'''

class DummyAPI(CatalogAPI):
    def get_items(self) -> pd.DataFrame:
        return pd.read_csv('sample_catalog.csv')

class RealAPI(CatalogAPI):
    def __init__(self):
        self._file_id = os.getenv('GOOGLE_DRIVE_FILE_ID')
        self._api_key = os.getenv('GOOGLE_DRIVE_API_KEY')
        self._resource_key = os.getenv('GOOGLE_DRIVE_RESOURCE_KEY')
        return

    def get_items(self) -> pd.DataFrame:
        url = (
            f'https://www.googleapis.com/drive/v3/files/{self._file_id}'
            '?alt=media'
        )
        headers = {'X-Goog-Api-Key': self._api_key}
        if self._resource_key:
            # Some links include a resourcekey value
            headers['X-Goog-Drive-Resource-Keys'] = (
                f'{self._file_id}/{self._resource_key}'
            )
        with requests.get(
            url, headers=headers, timeout=20, stream=True
        ) as response:
            response.raise_for_status()
            # Decode HTTP compression before pandas reads the CSV
            response.raw.decode_content = True
            return pd.read_csv(response.raw)

class Catalog:
    def __init__(self):
        api_key = os.getenv('GOOGLE_DRIVE_API_KEY')
        file_id = os.getenv('GOOGLE_DRIVE_FILE_ID')

        if api_key and file_id:
            self._api = RealAPI()
            print('Using RealAPI')
        else:
            self._api = DummyAPI()
            print('Using DummyAPI')
        return
    
    def get_items(self) -> pd.DataFrame:
        return self._api.get_items()