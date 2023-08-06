import time
import spidev

# Op Codes
READ_DATA = 0x03
HIGH_SPEED_READ = 0x0b
SECTOR_ERASE = 0x20
BLOCK_ERASE = 0x52
CHIP_ERASE = 0xC7
BYTE_PROG = 0x02
AAI_PROG = 0xAF
READ_STATUS_REG = 0x05
WRITE_STATUS_ENABLE = 0x50
WRITE_STATUS_REG = 0x01
WRITE_ENABLE = 0x06
WRITE_DISABLE = 0x04
READ_ID = 0x90
VENDOR_ID = 0xBF
CHIP_ID = 0x49

#
# SPI Configurations
#
# SPI bus 0 of CM4
bus = 0
# Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 0
# Enable SPI
spi = spidev.SpiDev()
# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)
# Set SPI speed and mode
spi.max_speed_hz = 1000000
spi.mode = 0

#
# Functions
#
# Decompose memory address in a list os 3 values of 8 bits each
def set_address(addr):
    aux = addr.to_bytes(3,'big')
    return [aux[i] for i in range(0,3)]

# Read SST25VF vendor ID and chip ID
# Return 0 if both IDs are correct
# Return 1 if one or both IDs is/are wrong
def read_id():
    msg = [READ_ID] + set_address(0) + [0]
    reply = spi.xfer2(msg)
    if reply[4] == VENDOR_ID:
        msg = [READ_ID] + set_address(1) + [0]
        reply = spi.xfer2(msg)
        if reply[4] == CHIP_ID:
            return 0
        else:
            return 1    
    else:
        return 1

# Remove block protection to allow writes to memory
# Return 0 if protection is well removed
# Return 1 if protection isn't well removed
def init():
    spi.writebytes([WRITE_STATUS_ENABLE])
    spi.writebytes([WRITE_STATUS_REG,0])    # Write 0 to set BP0, BP1 and BPL as 0

    # Verify if write protection was well removed
    reply = spi.xfer2([READ_STATUS_REG, 0])
    if (reply[1] & 0x8C) == 0:
        return 0
    else:
        return 1    

# Wait until busy bit goes to 0 
def wait_until_done():
    while True:
        reply = spi.xfer2([READ_STATUS_REG, 0])
        if (reply[1] & 0x01) == 0:
            break

# Write byte to a specific address
def write_byte(addr, data):
    spi.xfer2([WRITE_ENABLE])
    msg = [BYTE_PROG] + set_address(addr) + [data]
    spi.xfer2(msg)
    wait_until_done()

# Write array of bytes starting in a specific address
def write_array(addr, data):
    for i in range (0, len(data)):
        write_byte(addr+i, data[i])
    spi.xfer2([WRITE_DISABLE])    

# Read array of n_bytes starting in a specific address
# Returns a list with the loaded values
def read_array(addr, n_bytes):
    msg = [READ_DATA] + set_address(addr)
    for i in range (0, n_bytes):
        msg.append(0)  
    data = spi.xfer2(msg)
    return data[4:]   

# Erase a sector specified by its address (sector_addr)
def sector_erase(sector_addr):
    spi.xfer2([WRITE_ENABLE])
    msg = [SECTOR_ERASE] + set_address(sector_addr)
    spi.xfer2(msg)
    wait_until_done()
    spi.xfer2([WRITE_DISABLE])

# Erase all memory content
def total_erase():
    spi.xfer2([WRITE_ENABLE])
    spi.xfer2([CHIP_ERASE])
    wait_until_done()
    spi.xfer2([WRITE_DISABLE])
