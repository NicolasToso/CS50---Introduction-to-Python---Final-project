from proyect import map_request, format_address, check_address
import re
import googlemaps
from pytest import raises


def test_map_request():
    maps = googlemaps.Client(key=API_KEY)
    assert map_request("afgdsgdfgsdfgdfgd", "ferreteria") != list()

def test_format_address():
    assert format_address("1111111111111111111111") == ([], [])

def test_check_address():
    with raises (TypeError):
        check_address(["empty"])
  


    
