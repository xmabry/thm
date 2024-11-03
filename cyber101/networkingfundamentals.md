# Networking Fundamentals

## OSI Model
Physical Layer
Data Link Layer
Network Layer
Transport Layer
Session Layer
Presentation Layer
Application Layer

## OSI Model and RFC1122 Model

| OSI Layer             | RFC1122 Layer | Examples                                                                                     |
|-----------------------|---------------|----------------------------------------------------------------------------------------------|
| Physical Layer        | Link Layer    | WiFi radio bands (2.4 GHz, 5 GHz, 6 GHz)                                                     |
| Data Link Layer       | Link Layer    | Ethernet (802.3), WiFi (802.11). Ethernet and WiFi addresses are six bytes, called MAC addresses. They are usually expressed in hexadecimal format with a colon separating each two bytes. The three leftmost bytes identify the vendor. |
| Network Layer         | Internet Layer| Internet Protocol (IP), Internet Control Message Protocol (ICMP), Virtual Private Network (VPN) protocols such as IPSec and SSL/TLS VPN |
| Transport Layer       | Transport Layer| Transmission Control Protocol (TCP), User Datagram Protocol (UDP)                            |
| Session Layer         | Application Layer| Network File System (NFS), Remote Procedure Call (RPC)                                       |
| Presentation Layer    | Application Layer| Data encoding, compression, and encryption. An example of encoding is character encoding, such as ASCII or Unicode. |
| Application Layer     | Application Layer| HTTP, FTP, DNS, POP3, SMTP, IMAP                                                             |

## DNS

A Record - Address record map host to IPv4
AAAA Record - Address record map host to IPv6
The CNAME (Canonical Name) record maps a domain name to another domain name. 
The MX (Mail Exchange) record specifies the mail server responsible for handling emails for a domain.

## WHOIS
whois {website domain}

## HTTP
Using telnet to connect to a server you want to use the following formate when you're looking for the webserver ports that could be listening on the server
```sh
telnet 10.10.88.81 80
Trying 10.10.88.81...
Connected to 10.10.88.81.
Escape character is '^]'.
GET /flag.html HTTP/1.1
Host: anything

HTTP/1.1 200 OK
```

## FTP
logging in to a server using the anonymous user doesn't require a password but you have the opportunity to 


## SMTP
this is another connect over telnet protocol but on port 25



## TCPDUMP
| Command          | Explanation                                                      |
|------------------|------------------------------------------------------------------|
| tcpdump -i INTERFACE | Captures packets on a specific network interface              |
| tcpdump -w FILE      | Writes captured packets to a file                             |
| tcpdump -r FILE      | Reads captured packets from a file                            |
| tcpdump -c COUNT     | Captures a specific number of packets                         |
| tcpdump -n           | Don’t resolve IP addresses                                    |
| tcpdump -nn          | Don’t resolve IP addresses and don’t resolve protocol numbers |
| tcpdump -v           | Verbose display; verbosity can be increased with -vv and -vvv |
| tcpdump host IP or tcpdump host HOSTNAME | Filters according to the IP or HOSTNAME |
| tcpdump src host IP |
| tcpdump dst host IP |
| tcpdump -r traffic.pcap icmp -n  | adding wc word count allows you to 
| tcpdump -r traffic.pcap "tcp[tcpflags] == tcp-rst" | 
| tcpdump -r traffic.pcap greater 15000 -n -c 55 |