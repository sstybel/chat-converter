<#
   Download YouTube videos and live chat using yt-dlp and converter json format live chat to text format

   Copyright (c) 2025 by Sebastian Stybel, www.BONO.Edu.PL
#>

param([String]$url) 

.\yt-dlp.exe -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b" --extractor-args "youtube:player-client=default,-tv_simply" --write-sub --sub-lang live_chat $url

.\chat-converter.exe --json auto --output auto --print
