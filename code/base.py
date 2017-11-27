from mininet.topo import Topo
from mininet.net import Mininet
from mininet.link import TCLink


#hostList = []


class myDataCenterTopo(Topo):
    def build(self, n=2):       # n is the number of hosts at each edge switch
        host_number = 1
        edge_number = 1
        # core switch
        core_switch = self.addSwitch('sC1')

            # aggregate switches
            for i in xrange(2):
                agg_switch = self.addSwitch('sA%s' % (i+1))
                # link between agg switch and core switch
                self.addLink(core_switch, agg_switch, bw=50, delay="5ms") # bw 50Mbps delay 5ms

                # edge switches
                for j in xrange(2):
                    edge_switch = self.addSwitch('sE%s' % edge_number)
                    edge_number += 1
                    # link between edge and agg switch
                    self.addLink(agg_switch, edge_switch, bw=30, delay="10ms") # bw 30Mbps delay 10ms

                    # hosts
                    for k in xrange(n):
                        host = self.addHost('h%s' % host_number, cpu=0.125/n)
                        hostList.append(host)
                        host_number += host_number
                        # link between edge switch and host
                        self.addLink(edge_switch, host, bw=10, delay="15ms") # bw 10Mbps delay 15ms



def simpleTest():
    topo = myDataCenterTopo(n=2)
    net = Mininet(topo)
    print 'starting mininet..'
    net.start()
    print 'starting pingall..'
    net.pingAll()
    print 'hosts are..'
    print net.hosts
    print 'switches are..'
    print net.switches
    net.stop()

def main():
    simpleTest()

if __name__ == '__main__':
    main()
