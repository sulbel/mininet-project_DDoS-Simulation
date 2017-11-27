# Notes for using mininet

* If error 'RTNETLINK answers: File exists'
  * `sudo mn -c` to clear environment
* To get all hosts/switches
  * net.hosts / net.switches

## Testing Connections

* *PINGING*
  * `h3 ping -c 4 h1` will ping host 1 with 4 packets, originating from host 3
  * `pingall` will ping every host with all other hosts

* *Bandwidth*
  * `iperf` tests the TCP bw between furthest hosts
  * Results: _***Results: ['9.20 Mbits/sec', '13.1 Mbits/sec']_
