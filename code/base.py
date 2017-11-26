
 

# core switch
core_switch = self.addSwitch('c1')
host_number = 1
edge_number = 1
    # aggregate switches
    for i in xrange(2):
        agg_switch = self.addSwitch('a%s' % (i+1))
        # link between agg switch and core switch
        self.addLink(core_switch, agg_switch) # bw 50 delay 5ms

        # edge switches
        for j in xrange(2):
            edge_switch = self.addSwitch('e%s' % edge_number)
            edge_number += 1
            # link between edge and agg switch
            self.addLink(agg_switch, edge_switch) # bw 30 delay 10ms

            # hosts
            for k in xrange(n):
                host = self.addHost('h%s' % host_number, )
                host_number += host_number
                # link between edge switch and host
                self.addLink(edge_switch, host) # bw 10 delay 15ms
