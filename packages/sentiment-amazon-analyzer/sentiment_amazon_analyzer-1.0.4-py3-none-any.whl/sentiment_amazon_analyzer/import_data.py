import pandas as pd
import gzip
import json

class DataImporter():
    """
        Imports data into dataframe
    """
    def __init__(self, path):
        self._path = path

    def import_data(self):
        df = self._load_data()
        return pd.DataFrame.from_dict(df, orient='index')

    def _load_data(self):
        i = 0
        df = {}
        
        for d in self._parse():
            df[i] = d
            i += 1
        return df

    def _parse(self):
        g = gzip.open(self._path, 'rb')
        # for every line
        for l in g:
            # convert json into python object
            yield json.loads(l)