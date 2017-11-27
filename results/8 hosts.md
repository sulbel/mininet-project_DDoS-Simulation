# BASE CASE

Core -> Agg link: bw=50, delay='5ms'
Agg -> Edge link: bw=30, delay="10ms"
Edge -> Host link: bw=10, delay="15ms", loss=0, max_queue_size=1000

Host CPU limit: cpu=0.125/n

No hosts perform attack, `iperf` yields:
![result of iperf](https://i.imgur.com/SgJD7Fa.png)

`pingall` results:
![result of pingall](https://i.imgur.com/ay9qWil.png)


# Start DDoS

### Each Attacker Sends 20 UDP Datagrams with payload "junk "

![results](https://i.imgur.com/7Wm6XdA.png)


### Each Attacker Sends 200 UDP Datagrams with payload "junk " * 600

![results](https://i.imgur.com/J78V4ky.png)










### Each Attacker Sends 2 UDP Datagrams with payload "junk "

![results](https://i.imgur.com/SGLyo3B.png)




### Each Attacker Sends 20 UDP Datagrams with payload "junk "

![results](https://i.imgur.com/7Wm6XdA.png)


### Each Attacker Sends 20 UDP Datagrams with payload "junk " * 600

![results](https://i.imgur.com/imL7lPg.png)
