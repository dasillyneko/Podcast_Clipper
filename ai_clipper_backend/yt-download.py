from pytubefix import YouTube
from pytubefix.cli import on_progress

url1="https://www.youtube.com/watch?v=6XLixvPEXUg&ab_channel=SoniaShenoy"
url2="https://www.youtube.com/watch?v=MbaZ93RS-uw&ab_channel=SoniaShenoy"

yt=YouTube(url2, on_progress_callback=on_progress)
print(yt.title)

ys=yt.streams.get_highest_resolution()
ys.download()