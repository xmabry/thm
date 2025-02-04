https://www.howtogeek.com/405806/windows-task-manager-the-complete-guide/
     

[Remina](https://remmina.org/) is a remote desktop client for Linux. 

For network configuration you can use commands like:
ipconfig
ping
tracert
nslookup
netstat

Use of 
tasklist /FI "imagename eq notepad.exe"
taskkill /PID 1234


## Stored Passwords
Windows uses a SAM file database to store credentials on the system. Generally can be found in the C:/Windows/System32/config folder

## Windows Logs
Going to Event Viewer, there is the opportunity for investigating application logs, security logs, and audit logs. Here's some important log codes

| Event ID | Description |
|----------|-------------|
| 4624     | A user account successfully logged in |
| 4625     | A user account failed to login |
| 4634     | A user account successfully logged off |
| 4720     | A user account was created |
| 4724     | An attempt was made to reset an account’s password |
| 4722     | A user account was enabled |
| 4725     | A user account was disabled |
| 4726     | A user account was deleted |
