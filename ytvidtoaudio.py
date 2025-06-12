import yt_dlp

url = "https://www.youtube.com/watch?v=9bZkp7q19f0"

options = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with yt_dlp.YoutubeDL(options) as ydl:
    ydl.download([url])
