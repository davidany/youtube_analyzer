from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi

youtube_url = "https://www.youtube.com/watch?v=aywZrzNaKjs"


video_id=YouTube(youtube_url).video_id

yt=YouTube(youtube_url)

try:
    if(yt):
        print("Title: ", yt.title)
        print("Title: ", yt.views)
        print("Title: ", yt.author)
        print("Title: ", yt.description)

except:
    print("there was issue connecting")

transcript=YouTubeTranscriptApi.get_transcript(video_id)
text_transcript = ""

for segment in transcript:
    text_transcript += segment['text'] + " "

print(text_transcript)