from pytube import YouTube

youtube_url = "https://www.youtube.com/watch?v=aywZrzNaKjs"

yt=YouTube(youtube_url)

try:
    if(yt):
        print("Title: ", yt.title)
        print("Title: ", yt.views)
        print("Title: ", yt.author)
        print("Title: ", yt.description)

except:
    print("there was issue connecting")