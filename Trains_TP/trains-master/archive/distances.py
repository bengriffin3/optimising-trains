import json
import requests
import api
import urllib.parse

import googlemaps


def distance(source, destination, city):
    gmaps = googlemaps.Client(key=api.key)
    origins = [f'{source} Metro Station', city]
    destinations = [f'{destination} Metro Station', city]

    matrix = gmaps.distance_matrix(origins, destinations,
                                   mode="transit")
    return matrix['rows'][0]['elements'][0]['duration']['value']
