from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.util import dumpNodeConnections
from mininet.cli import CLI
#from mininet.log import setLogLevel




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
                    self.addLink(edge_switch, host, bw=10, delay="15ms") # bw 10Mbps delay 15ms



def simpleTest():
    topo = myDataCenterTopo(n=2)
    net = Mininet(topo=topo, link=TCLink)
    print 'starting mininet..'
    net.start()

    print 'trying to start UDP client and server...\n'
    targetHost = net.get('h1')
    print 'targ host has IP:', targetHost.IP()
    p1 = targetHost.popen('python UDPServer.py')

    attackingHost = net.get('h8')
    print 'attack host has IP:', attackingHost.IP()
    attackingHost.cmd('python UDPClient.py')


    #print 'host 1 is:', h1
    #print 'with an IP address of:', h1.IP()
    #print 'starting pingall..'
    #net.pingAll()
    #print 'hosts are..'
    #print net.hosts
    #print 'switches are..'
    #print net.switches
    #CLI(net)
    p1.terminate()
    net.stop()

def main():
    #setLogLevel('info')
    simpleTest()

if __name__ == '__main__':
    main()
