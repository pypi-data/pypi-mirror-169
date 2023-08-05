from sentiment_amazon_analyzer.import_data import DataImporter
from mock import patch

class TestDataImporter():

    @patch('sentiment_amazon_analyzer.import_data.DataImporter._load_data')
    def test_load_data_is_called_once(self, mock_ld):
        mock_ld.return_value ={
            "0": {
                'overall': 3.0, 
                'verified': False, 
                'reviewTime': '08 4, 2014', 
                'reviewerID': 'A24E3SXTC62LJI', 
                'asin': 
                '7508492919', 
                'style': {
                    'Color:': ' Bling'
                }, 
                'reviewerName': 'Claudia Valdivia', 
                'reviewText': 'Looks even better in person.', 
                'summary': "Can't stop won't stop looking at it", 
                'unixReviewTime': 1407110400
            }
        } 
        data_importer = DataImporter('path')
        df = data_importer.import_data()
        data_importer._load_data.assert_called_once()


    @patch('sentiment_amazon_analyzer.import_data.DataImporter._load_data')
    def test_path_is_defined(self, mock_ld):
        mock_ld.return_value ={
            "0": {
                'overall': 3.0, 
                'verified': False, 
                'reviewTime': '08 4, 2014', 
                'reviewerID': 'A24E3SXTC62LJI', 
                'asin': 
                '7508492919', 
                'style': {
                    'Color:': ' Bling'
                }, 
                'reviewerName': 'Claudia Valdivia', 
                'reviewText': 'Looks even better in person.', 
                'summary': "Can't stop won't stop looking at it", 
                'unixReviewTime': 1407110400
            }
        } 
        data_importer = DataImporter('path')
        df = data_importer.import_data()
        assert data_importer._path is not None


    @patch('sentiment_amazon_analyzer.import_data.DataImporter._load_data')
    def test_num_of_df_rows_is_1(self, mock_ld):
        mock_ld.return_value ={
            "0": {
                'overall': 3.0, 
                'verified': False, 
                'reviewTime': '08 4, 2014', 
                'reviewerID': 'A24E3SXTC62LJI', 
                'asin': 
                '7508492919', 
                'style': {
                    'Color:': ' Bling'
                }, 
                'reviewerName': 'Claudia Valdivia', 
                'reviewText': 'Looks even better in person.', 
                'summary': "Can't stop won't stop looking at it", 
                'unixReviewTime': 1407110400
            }
        } 
        data_importer = DataImporter('path')
        df = data_importer.import_data()
        assert len(df.index) == 1
