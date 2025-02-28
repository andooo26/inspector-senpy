set "video_path=test.mp4"

:loop
start /wait "" "C:\Program Files\VideoLAN\VLC\vlc.exe" --loop --play-and-exit --fullscreen "%video_path%"
goto loop
