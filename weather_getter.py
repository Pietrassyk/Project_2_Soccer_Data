class WeatherGetter:
    def __init__(self):
        # API key from Dark Sky
        #   https://darksky.net/dev/docs#time-machine-request
        self.api_key = '9e82e12479d0f36289a78ea12a5cf8af'

    def is_rain(self, day, location):

        # LOCATION
        # Currently hard-coded location to Berlin using:
        #   https://www.latlong.net/
        lat = 52.520008
        long = 13.404954

        # DATE
        # try to find the date from the string and use
        date_patt = re.compile(r'(\d{1,2})/(\d{1,2})/(\d{4})')
        match = date_patt.search(day)
        if (match):
            m, d, y = match.group(1), match.group(2), match.group(3)
            t = datetime.datetime(int(y), int(m), int(d))
        else:
            return ('Invalid Date: M/D/YYYY')

        # EXCLUDEminimize the return JSON from the API by using the exclude list because the API lets us
        exclude = 'currently,hourly'
        query = f'https://api.darksky.net/forecast/{self.api_key}/{lat},{long},{t.strftime("%s")}?exclude={exclude}'

        try:
            r = requests.get(query)
        except Exception as e:
            print(e)

        # PARSE FOR RAIN:  The Expected keys = dict_keys(['latitude', 'longitude', 'timezone', 'daily', 'flags', 'offset'])
        # We want to see if the string 'rain' exists in the ['data']['daily']['summary'], or 'data']['daily']['icon']
        summary, icon = r.json()['daily']['data'][0]['summary'], r.json()['daily']['data'][0]['icon']
        if ('rain' in summary.lower()) or ('rain' in icon.lower()):
            print(summary, icon)
            return True
        else:
            print(summary, icon)
            return False


w = WeatherGetter()
w.is_rain('7/2/12', 'here')