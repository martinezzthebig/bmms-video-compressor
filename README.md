# Prerequisites

This software is a Python script which requires basic CLI commands knowledge. This includes navigation in the file system and invocation of a script.

You need to have Python v2.7+ installed on your system.

# Dependencies

- `ffmpeg` - Windows/Linux/MacOS - needed for the video compression
- `Chocolatey` - Windows - package manager needed for installing `ffmpeg`
- `Homebrew` - MacOS - package manager needed for installing `ffmpeg`

All dependencies will be installed automatically by the script. However if user agreement is needed you will have to do that yourself.

# Usage

1. Open a shell terminal (PowerShell terminal on Windows)
2. Navigate to the directory where the script is contained
3. Call the script with (`<target_directory_path>` being the relative or absolute path of the directory containing the video files that you want to compress)
```
python project_script.py <target_directory_path>
```

NOTE: If the script has no arguments it will compress every video file in the directory it is in, as well as its subdirectories.

# Known issues

## Windows
*None yet.*

## MacOS
*None yet.*

## Linux

If you get the following error:
```
E: Could not get lock /var/lib/dpkg/lock-frontend - open (11: Resource temporarily unavailable) 
E: Unable to acquire the dpkg frontend lock (/var/lib/dpkg/lock-frontend), is another process using it?
```
It is best if you run linux in recovery mode and choose clean and check dpkg there.

WARNING: The steps below cannot guarantee a healthy state of your system afterwards. 
         But, in the end you can still fix the system in recovery mode as i've mentioned.

1. Open up a terminal
2. Execute `ps aux | grep -i apt` to check the running processes contanining "apt" (the update process is one of these)
3. If you see a process with name ending with "daily update", BINGO
4. In the second column of that process's row you will see the process ID (e.g. `1321`)
5. Execute `sudo kill <process-id>` (e.g. `sudo kill 1321`)

If the problems still persists:

1. Run these commands one by one:
```
sudo lsof /var/lib/dpkg/lock
sudo lsof /var/lib/apt/lists/lock
sudo lsof /var/cache/apt/archives/lock
```
2. Kill every process you encounter in there with `sudo kill -9 <process-id>` (do not forget the "-9" parameter)
3. Run these commands
```
sudo rm /var/lib/apt/lists/lock
sudo rm /var/cache/apt/archives/lock
sudo rm /var/lib/dpkg/lock
```
4. Reconfigure the packages with `sudo dpkg --configure -a`
5. Run `sudo apt full-upgrade`