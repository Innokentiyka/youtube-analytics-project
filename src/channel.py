
class Channel:
    def __init__(self, channel_id):
        self.channel_id = channel_id
        self.api_key = 'nYWC2jEhe6ymWQkZPzVzBMkaxWnosnka'

    def get_channel_info(self):
        import requests
        url = f'https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id={self.channel_id}&key={self.api_key}'
        response = requests.get(url)
        data = response.json()
        return data

    def print_info(self):

        channel_info = self.get_channel_info()
        print (channel_info)