import youtube_dl

want = True

while(want):
    url = input("What're you trying to download: ")

    ytdl_options = {
        'format': 'bestaudio/best',
        'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ytdl_options) as ydl:
        ydl.download([url])

    yesno = input("Do you want to download another song? (y/n): ")
    if (yesno.lower() == 'n' or yesno.lower() == 'no'):
        want = False
