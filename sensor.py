class FS2012(object):

  def Gas_Part(self):
    DEVICE_BUS = 1
    bus = smbus.SMBus(DEVICE_BUS)
    data = bus.read_i2c_block_data(0x07, 0, 2)
    SLPM = ((data[0] << 8) + data[1])/1000
    return SLPM
