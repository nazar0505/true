class Monitor:
displayResolution = 0
screenSize = 0
rate = 0
def __init__ (self, px,dm,Hz):
    print("Create nem Monitor")
    self.displayResolution = px
    self.screenSize = dm
    self.rate = Hz


def printInfo(self,name):
    print lg(name:-10}")
    print("Display Resolution:", self.displayResolution)
    print("Screen Size:", self.screenSize)
    print("Image refresh rate:", self.rate)
    def _test(self):
        print("test")

lg = Monitor (1500,500,1000)
philips = Monitor (500,345,6789)
lg.printInfo("LG")
philips.printInfo("PHILIPS")
lg._test()