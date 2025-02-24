from googleapiclient.discovery import build


class Video:
    def __init__(self, video_id: str):
        self.video_id = video_id
        try:
            self.youtube = build('youtube', 'v3', developerKey=self.video_id)
            self.video_response = self.youtube.videos().list(part='snippet,statistics,contentDetails,topicDetails',
                                                         id=self.video_id).execute()
            self.video_title = self.video_response['items'][0]['snippet']['title']
            self.view_count = self.video_response['items'][0]['statistics']['viewCount']
            self.like_count = self.video_response['items'][0]['statistics']['likeCount']
            self.comment_count = self.video_response['items'][0]['statistics']['commentCount']
        except ValueError:
            self.video_title = None
            self.like_count = None

    def __str__(self):
        return f"{self.video_title}"


class PLVideo(Video):
    def __init__(self, video_id: str, playlist_id):
        super().__init__(video_id)
        self.playlist_id = playlist_id

    def __str__(self):
        return f"{self.video_title}"