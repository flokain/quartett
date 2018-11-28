from pandas import DataFrame

from dataReaders import get_google_sheet, gsheet2df
from xmlManipulator import renderAsPdf, substituteSVG


def testGenerator():
    values = {}
    values['card_name'] = "Blaumeise"

    tree = substituteSVG(values)
    renderAsPdf(tree, values['card_name'])


def testExcelReading():
    SPREADSHEET_ID = '1CJKcriAlXe6nPxcFuNbdgMF24N5SN2lu7lQBmlBdtGc'
    RANGE_NAME = 'daten'

    gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
    df = gsheet2df(gsheet)

def generateQuartett():

    SPREADSHEET_ID = '1CJKcriAlXe6nPxcFuNbdgMF24N5SN2lu7lQBmlBdtGc'
    RANGE_NAME = 'daten'

    gsheet = get_google_sheet(SPREADSHEET_ID, RANGE_NAME)
    df = gsheet2df(gsheet)

    dict_data = df.to_dict(orient='records')
    for values in dict_data:
        tree = substituteSVG(values)
        renderAsPdf(tree, values['card_file_name'])

generateQuartett()