import sys
import os
import subprocess

ROOT_DIRECTORY = ""
VIDEO_FILE_EXTENSIONS = [".mkv", ".mov", ".mp4"]

def installFFmpegOnWindows():
  subprocess.call([
    "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", 
    ". \"./choco_install\";"
  ])
  os.system("choco install ffmpeg")

def installFFmpegOnMacOS():
  os.system("/bin/bash -c '$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)'")
  os.system("brew install ffmpeg")

def installFFmpegOnLinux():
  os.system("sudo apt install ffmpeg")

if len(sys.argv) < 2 or len(sys.argv) > 2:
  ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) == 2:
  ROOT_DIRECTORY = sys.argv[1]

ffmpegVersionCommandString = "ffmpeg --version"
if sys.platform == "linux" or sys.platform == "linux2":
  ffmpegVersionCommandString = "ffmpeg -version"

does_not_have_ffmpeg = os.system(ffmpegVersionCommandString)
if does_not_have_ffmpeg:
  if sys.platform == "win32": installFFmpegOnWindows()
  elif sys.platform == "darwin": installFFmpegOnMacOS()
  elif sys.platform == "linux" or sys.platform == "linux2": installFFmpegOnLinux()

slash = "/"
if sys.platform == "win32":
  slash = "\\"

for subdirs, dirs, files in os.walk(ROOT_DIRECTORY):
  if "Compressed" in subdirs or ".git" in subdirs:
    continue
  for file in files:
    extension = os.path.splitext(file)[-1].lower()
    if extension not in VIDEO_FILE_EXTENSIONS:
      continue
    if not os.path.exists(subdirs + slash + "Compressed"):
      os.makedirs(subdirs + slash + "Compressed")
    media_in = subdirs + slash + file
    media_out = subdirs + slash + "Compressed" + slash + file
    #print("ffmpeg -i " + media_in + " -vcodec libx264 -crf 24 " + media_out)
    os.system("ffmpeg -i " + media_in + " -vcodec libx264 -crf 24 " + media_out)