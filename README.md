# Converter YouTube Live-Chat JSON file to Text file

<a href="https://github.com/sstybel/chat-converter/releases/latest"><img alt="Static Badge" src="https://img.shields.io/badge/download-red?style=for-the-badge&label=stable&color=%23FF0000&link=https%3A%2F%2Fgithub.com%2Fsstybel%2Fchat-converter%2Freleases%2Flatest"></a> ![GitHub Release](https://img.shields.io/github/v/release/sstybel/chat-converter?sort=date&display_name=release&style=for-the-badge&logo=github&label=release&link=https%3A%2F%2Fgithub.com%2Fsstybel%2Fchat-converter) ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/sstybel/chat-converter/total?style=for-the-badge&logo=github&link=https%3A%2F%2Fgithub.com%2Fsstybel%2Fchat-converter)

This program converts live chat from YouTube downloaded using the **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** application.

To download live chat from YouTube using the **[yt-dlp](https://github.com/yt-dlp/yt-dlp)** application, call it with the parameters `--write-sub --sub-lang live_chat`. The live chat will be saved in JSONL (_JSON Lines_) format to a file with the .json extension.

Sample execution of the **`yt-dlp.exe`** application downloading a YouTube recording with the best available video and audio quality and live chat:

> `yt-dlp.exe -f "bv*[ext=mp4]+ba[ext=m4a]/b[ext=mp4] / bv*+ba/b" --extractor-args "youtube:player-client=default,-tv_simply" --write-sub --sub-lang live_chat https://link_to_the_youtube_video/`


In this repository, I've included sample PowerShell code (`yt-down.ps1`) that downloads a YouTube recording along with a live chat saved in JSON (.json) format and converts it to a text file (.txt).

**Usage:** **`chat-converter.exe`** [--json JSON] [--output OUTPUT] [--print] [--add-line-number] [--help | -h]`

**Options:**

* `--json JSON` - Input JSON Chat file or `auto` to select first JSON file in current directory
* `--output OUTPUT` - Output text Chat file or `auto` to create output file with same name as input file and add .txt extension
* `--print` - Print Chat messages to console
* `--add-line-number` - Add line numbers to each message in output file and console output
* `--help`, `-h` - Show this help message and exit

## Download

<a href="https://github.com/sstybel/chat-converter/releases/latest"><img alt="Static Badge" src="https://img.shields.io/badge/download-red?style=for-the-badge&label=stable&color=%23FF0000&link=https%3A%2F%2Fgithub.com%2Fsstybel%2Fchat-converter%2Freleases%2Flatest"></a> ![GitHub Release](https://img.shields.io/github/v/release/sstybel/chat-converter?sort=date&display_name=release&style=for-the-badge&logo=github&label=release&link=https%3A%2F%2Fgithub.com%2Fsstybel%2Fchat-converter) ![GitHub Downloads (all assets, all releases)](https://img.shields.io/github/downloads/sstybel/chat-converter/total?style=for-the-badge&logo=github&link=https%3A%2F%2Fgithub.com%2Fsstybel%2Fchat-converter)

##  GitHub

![GitHub stats](https://github-readme-stats-sigma-five.vercel.app/api?username=sstybel&show_icons=true&theme=react&hide_title=true&include_all_commits=true)

&nbsp;

---

## Copyright &copy; 2025 - 2026 by Sebastian Stybel, [www.BONO.Edu.PL](https://www.bono.edu.pl/)
