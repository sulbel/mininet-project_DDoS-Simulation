from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
#from mininet.log import setLogLevel



# data center topology with a single core switch,
    # 2 aggregate switch, 4 edge switch, and n*4 hosts
class myDataCenterTopo(Topo):
    def __init__(self, n):       # n is the number of hosts at each edge switch

        Topo.__init__( self )

        host_number = 1
        edge_number = 1

        # add core switch
        core_switch = self.addSwitch('sC1')

        # add aggregate switches
        for i in xrange(2):
            agg_switch = self.addSwitch('sA%s' % (i+1))
            # link between agg switch and core switch
            self.addLink(core_switch, agg_switch, bw=50, delay='5ms') # bw 50Mbps delay 5ms

            # add edge switches
            for j in xrange(2):
                edge_switch = self.addSwitch('sE%s' % edge_number)
                edge_number = edge_number + 1
                # link between edge and agg switch
                self.addLink(agg_switch, edge_switch, bw=30, delay="10ms") # bw 30Mbps delay 10ms

                # add hosts
                for k in xrange(n):
                    host = self.addHost('h%s' % host_number, cpu=0.125/n)
                    host_number = host_number + 1
                    # link between edge switch and host
                    self.addLink(edge_switch, host, bw=10, delay="15ms", loss=0, max_queue_size=1000) # bw 10Mbps delay 15ms

# start a DDoS attack
    # always targets h1 with IP of 10.0.0.1
    # sends large UDP datagrams to h1, saturating its links
def myAttack(net):
    hosts = net.hosts
    popens = {}
    for host in hosts:
        if host.name == 'h1':   # dont want to execute DDoS code at the target
            continue
        else:                   # make all other hosts DDoS h1
            # print 'host', host.name, 'with IP', host.IP(), 'starting DDoS..\n'
            print 'starting DDoS attack with', host.name
            popens[host.name] = net.get(host.name).popen('python UDPClient.py')       # popen used so that performance may be measured during attack

    return popens


# initializes data center mininet topology..
    # then starts a simple UDP server on target host (h1)..
    # before calling function myAttack, which floods h1 with all other hosts
def simpleTest():
    topo = myDataCenterTopo(n=32)
    net = Mininet(topo=topo, link=TCLink)
    print 'starting mininet..'
    net.start()

    print 'trying to start UDP client and server...\n'
    targetHost = net.get('h1')
    print 'targ host has IP:', targetHost.IP()

    # p1 = targetHost.popen('python UDPServer.py')
    # pAttackers = myAttack(net)

    #print 'starting pingall..'
    #net.pingAll()


    CLI(net)
    # p1.terminate()
    net.stop()

def main():
    #setLogLevel('info')
    simpleTest()

if __name__ == '__main__':
    main()
