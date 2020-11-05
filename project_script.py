import sys
import os
import subprocess
import popen2

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

does_not_have_ffmpeg = os.system("ffmpeg --version")
if does_not_have_ffmpeg:
  if sys.platform == "win32": installFFmpegOnWindows()
  elif sys.platform == "darwin": installFFmpegOnMacOS()
  elif sys.platform == "linux" or sys.platform == "linux2": installFFmpegOnLinux()