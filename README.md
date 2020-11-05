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