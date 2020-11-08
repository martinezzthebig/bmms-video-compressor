import sys
import os
import subprocess

ROOT_DIRECTORY = ""
VIDEO_FILE_EXTENSIONS = [".mkv", ".mov", ".mp4"]

def runCommandAndGetResult(command):
  process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
  process.wait()
  return process.returncode != 0

def installFFmpegOnWindows():
  doesNotHaveChocolatey = runCommandAndGetResult("choco --version")
  if doesNotHaveChocolatey:
    subprocess.call([
      "C:\\WINDOWS\\system32\\WindowsPowerShell\\v1.0\\powershell.exe", 
      ". \"./choco_install\";"
    ])
  os.system("choco install ffmpeg")

def installFFmpegOnMacOS():
  doesNotHaveHomeBrew = runCommandAndGetResult("brew help")
  if doesNotHaveHomeBrew:
    os.system("curl -fsSL -o install.sh https://raw.githubusercontent.com/Homebrew/install/master/install.sh")
    os.system("/bin/bash install.sh")
    os.system("rm install.sh")
    os.system("rm uninstall.sh")
  os.system("brew install ffmpeg")

def installFFmpegOnLinux():
  os.system("sudo apt install ffmpeg")

if len(sys.argv) < 2 or len(sys.argv) > 2:
  ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

if len(sys.argv) == 2:
  ROOT_DIRECTORY = sys.argv[1]

doesNotHaveFFMpeg = runCommandAndGetResult("ffmpeg -version")
if doesNotHaveFFMpeg:
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
    mediaIn = "\"" + subdirs + slash + file + "\""
    mediaOut = "\"" + subdirs + slash + "Compressed" + slash + file + "\""
    #print("ffmpeg -i " + mediaIn + " -vcodec libx264 -crf 24 " + mediaOut)
    os.system("ffmpeg -i " + mediaIn + " -vcodec libx264 -crf 24 " + mediaOut)