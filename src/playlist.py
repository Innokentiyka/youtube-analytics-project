import datetime
from googleapiclient.discovery import build


class PlayList:
    def __init__(self, playlist_id: str):
        self.playlist_id = playlist_id
        self.youtube = build('youtube', 'v3', developerKey=self.playlist_id)
        self.playlist_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                            id=self.playlist_id).execute()
        self.playlist_title = self.playlist_response['items'][0]['snippet']['title']
        self.url = f"https://music.youtube.com/playlist?list={self.playlist_id}"

    @property #ПЕРВЫЙ СПОСОБ
    def total_duration(self):
        total_seconds = sum(video.duration.total_seconds() for video in self.playlist_id)
        return datetime.timedelta(seconds=total_seconds)

    #def total_duration(self): ВТОРОЙ СПОСОБО
        #self.playlist_response = self.youtube.videos().list(part='contentDetails,statistics',
                                                           # id=','.join(self.playlist_id)
                                                            #).execute()
        #return self.playlist_response

    def show_best_video(self):
        best_video = max(self.playlist_id, key=lambda video: video['views'])
        return best_video['url']