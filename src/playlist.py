from googleapiclient.discovery import build


class PlayList:
    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        self.youtube = build('youtube', 'v3', developerKey=self.video_id)
        self.playlist_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                            id=self.playlist_id).execute()
        self.playlist_title = self.playlist_response['items'][0]['snippet']['title']
        self.url = f"https://music.youtube.com/playlist?list={self.playlist_id}"

    def total_duration(self):
        self.playlist_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                            id=','.join(self.playlist_id)
                                                            ).execute()
        return self.playlist_response
