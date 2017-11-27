# BASE CASE

Core -> Agg link: bw=50, delay='5ms'
Agg -> Edge link: bw=30, delay="10ms"
Edge -> Host link: bw=10, delay="15ms", loss=0, max_queue_size=1000

Host CPU limit: cpu=0.125/n

No hosts perform attack, `iperf` yields:
![result of iperf](https://i.imgur.com/Qp0J5vb.png)




# Start DDoS



### Each Attacker Sends 20 UDP Datagrams with payload "junk "

![results](https://i.imgur.com/ofcdqWB.png)


### Each Attacker Sends 200 UDP Datagrams with payload "junk " * 600
![results](https://i.imgur.com/624fSla.png)
