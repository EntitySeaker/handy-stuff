#Imports
import sys
from pytube import YouTube
from pytube.cli import on_progress

def main():
  URLS = sys.argv[1:]

  def on_complete(x, y):
    print()

  for i in URLS:
    video = YouTube(i, on_progress_callback=on_progress, on_complete_callback=on_complete, use_oauth=False, allow_oauth_cache=False)

    print("Printing video information...")
    print(f"Video title: {video.title}")
    stream = video.streams.get_highest_resolution()
    print(f"Downloading video: {i}")
    stream.download()
  print("Done!")

if __name__ == "__main__":
  main()
