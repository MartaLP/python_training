import requests


class Artist:

    endpoint = 'http://www.songsterr.com/a/ra/songs.json?pattern={}'

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_titles(json_data):
        """
        Uses the input json to search songs titles that
        will be returned as a list
        """
        titles = []
        for el in json_data:
            titles.append(el['title'])
        return titles

    def search_titles(self):
        """
        Returns the songs titles as a list
        or None if request status code <> 200.
        """
        url = self.endpoint.format(self.name)
        response = requests.get(url)
        if not response.status_code == 200 or response.json() == []:
            return None
        else:
            return Artist.get_titles(response.json())

