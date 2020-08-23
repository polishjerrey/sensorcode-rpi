import spidev
import sensor

class MCP3004(object):
    def __init__(self, bus, addr, vref):
        super(MCP3004, self).__init__()

        self._vref = vref
        self._spi = spidev.SpiDev()
        self._spi.open(bus, addr)

    def read(self, channel):
        r = self._spi.xfer2([1, (8+channel) << 4, 0])
        out = ((r[1]&3) << 8) + r[2]
        return out

    def voltage(self, channel):
        return self._vref * self.read(channel) / 1024.0