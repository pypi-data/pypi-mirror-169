# RCXXXX TinyMesh RF Module Library
# Tekon Electronics
#
# V 1.0.0 -First release

import RPi.GPIO as GPIO
import serial
import time
import threading

# Commands to execute different actions on RF module 
COMMAND_READ_MEM = b'Y'         # Read configuration memory
COMMAND_WRITE_MEM = b'M'        # Write configuration memory
COMMAND_EXIT_CONFIG = b'X'      # Exit configuration mode
COMMAND_SET_SLEEP = b'z'        # Enter in sleep mode
COMMAND_BATTERY = b'V'          # Get battery voltage
COMMAND_TEMPERATURE	= b'U'      # Get temperature
COMMAND_RSSI = b'S'             # Get RSSI
COMMAND_RESET = b'@'            # Reset configuration memory
COMMAND_PACKET_SNIFFER = b'6'   # Simple packet sniffer
COMMAND_SET_END_NODE = b'N'     # Set end device mode
COMMAND_SET_ROUTER = b'R'       # Set router mode
COMMAND_SET_GATEWAY	= b'G'      # Set gateway mode
COMMAND_TEST_MODE_1 = b'1'      # Test mode 1 (TX carrier ON)
COMMAND_TEST_MODE_2 = b'2'      # Test mode 2 (TX modulated signal)
COMMAND_TEST_MODE_3 = b'3'      # Test mode 3 (RX mode)
COMMAND_SET_AES_KEY_1 = b'K'    # Set AES key (command)
COMMAND_SET_AES_KEY_2 = b'7'    # Set AES key (argument)

# Functions return values
rcxxxx_return_values = {
    "EXIT_OK": 0,
    "EXIT_NOK": -1,
    "EXIT_COMM_ERROR": -1,
    "EXIT_NOT_READY": 1,
    "EXIT_FRAME_OK": 0,
    "EXIT_FRAME_DISCARD": 1,
    "EXIT_FRAME_NOT_RECEIVED": 2,
    "EXIT_FRAME_SENT": 0,
}

EXIT_OK = rcxxxx_return_values["EXIT_OK"]
EXIT_NOK = rcxxxx_return_values["EXIT_NOK"]
EXIT_COMM_ERROR = rcxxxx_return_values["EXIT_COMM_ERROR"]
EXIT_NOT_READY = rcxxxx_return_values["EXIT_NOT_READY"]
EXIT_FRAME_OK = rcxxxx_return_values["EXIT_FRAME_OK"]
EXIT_FRAME_DISCARD = rcxxxx_return_values["EXIT_FRAME_DISCARD"]
EXIT_FRAME_NOT_RECEIVED = rcxxxx_return_values["EXIT_FRAME_NOT_RECEIVED"]
EXIT_FRAME_SENT = rcxxxx_return_values["EXIT_FRAME_SENT"]

# States to control RF module state machine
STATE_NORMAL = 0
STATE_CONFIG = 1
STATE_SLEEP_PIN = 2
STATE_SLEEP_COMMAND = 3
STATE_SLEEP_USART = 4
STATE_TIMEOUT = 5
STATE_SNIFFER = 6
STATE_CHANGING = 7

# Timout constans
CONFIG_TIMEOUT = 350
SERIAL_TIMEOUT = 20
READ_MEM_TIMEOUT = 30
CONFIG_TO_NORMAL_TIMEOUT = 70
SLEEP_EXIT_TIMEOUT = 3
SLEEP_ENTER_TIMEOUT = 3
WAIT_PROMPT_TIMEOUT = 10
MEMORY_CONFIG_TIMEOUT = 60
WAIT_CMD_PROMPT_TIMEOUT = 500
SNIFFER_TIMEOUT = 5

# Tinymesh frames indexes
FRAME_TM_START_CHAR_INDEX = 0
FRAME_TM_SYS_ID0_INDEX = 1
FRAME_TM_SYS_ID1_INDEX = 2
FRAME_TM_SYS_ID2_INDEX = 3
FRAME_TM_SYS_ID3_INDEX = 4
FRAME_TM_ORI_ID0_INDEX = 5
FRAME_TM_ORI_ID1_INDEX = 6
FRAME_TM_ORI_ID2_INDEX = 7
FRAME_TM_ORI_ID3_INDEX = 8
FRAME_TM_ORI_RSSI_INDEX = 9
FRAME_TM_ORI_NET_LEVEL_INDEX = 10
FRAME_TM_HOP_CNT_INDEX = 11
FRAME_TM_MSG_CNT0_INDEX = 12
FRAME_TM_MSG_CNT1_INDEX = 13
FRAME_TM_LAT_CNT0_INDEX = 14
FRAME_TM_LAT_CNT1_INDEX = 15
FRAME_TM_PCK_TYPE_INDEX = 16
FRAME_TM_MESSAGE_DETAIL = 17
FRAME_TM_PAYLOAD_INDEX = 18
FRAME_TM_SNIF_RSSI = 0
FRAME_TM_SNIF_PCKT_LEN = 1
FRAME_TM_SNIF_DEST_ID0 = 2
FRAME_TM_SNIF_DEST_ID1 = 3
FRAME_TM_SNIF_DEST_ID2 = 4
FRAME_TM_SNIF_DEST_ID3 = 5
FRAME_TM_SNIF_SRC_ID0 = 6
FRAME_TM_SNIF_SRC_ID1 = 7
FRAME_TM_SNIF_SRC_ID2 = 8
FRAME_TM_SNIF_SRC_ID3 = 9
FRAME_TM_SNIF_JUMP_LV = 10
FRAME_TM_SNIF_PCKT_TYPE = 11

# RCXXXX Baudrate supported list
# rcxxxx_baudrate_list = (2400, 4800, 9600, 14400, 19200, 28800, 38400, 56700, 76800, 115200, 230400)
rcxxxx_baudrate_list = (230400, 115200, 76800, 56700, 38400, 28800, 19200, 14400, 9600, 4800, 2400)

# Address mapping
rcxxxx_configuration_memory = {
    "ADDRESS_RF_CHANNEL": 0,
    "ADDRESS_RF_POWER": 1,
    "ADDRESS_RF_DATA_RATE": 2,
    "ADDRESS_PROTOCOL_MODE": 3,
    "ADDRESS_RSSI_ACCEPTANCE_LEVEL": 4,
    "ADDRESS_RSSI_CLEAR_ACCEP_LEVEL": 5,
    "ADDRESS_HIAM_TIME": 6,
    "ADDRESS_IMA_TIME": 7,
    "ADDRESS_CONNECT_CHECK_TIME": 8,
    "ADDRESS_MAX_JUMP_LEVEL": 9,
    "ADDRESS_MAX_JUMP_COUNT": 10,
    "ADDRESS_MAX_PACKET_LATENCY": 11,
    "ADDRESS_RF_TRANSMIT_RETRY_LIM": 12,
    "ADDRESS_SERIAL_PORT_TIME_OUT": 13,
    "ADDRESS_DEVICE_TYPE": 14,
    "ADDRESS_EXCELLENT_RSSI_LEVEL": 15,
    "ADDRESS_GPIO_0_CONF": 16,
    "ADDRESS_GPIO_1_CONF": 17,
    "ADDRESS_GPIO_2_CONF": 18,
    "ADDRESS_GPIO_3_CONF": 19,
    "ADDRESS_GPIO_4_CONF": 20,
    "ADDRESS_GPIO_5_CONF": 21,
    "ADDRESS_GPIO_6_CONF": 22,
    "ADDRESS_GPIO_7_CONF": 23,
    "ADDRESS_GPIO_0_TRIG": 24,
    "ADDRESS_GPIO_1_TRIG": 25,
    "ADDRESS_GPIO_2_TRIG": 26,
    "ADDRESS_GPIO_3_TRIG": 27,
    "ADDRESS_GPIO_4_TRIG": 28,
    "ADDRESS_GPIO_5_TRIG": 29,
    "ADDRESS_GPIO_6_TRIG": 30,
    "ADDRESS_GPIO_7_TRIG": 31,
    "ADDRESS_INPUT_DEBOUNCE": 32,
    "ADDRESS_GPIO_0_AN_H_TRIG_HB": 33,
    "ADDRESS_GPIO_0_AN_H_TRIG_LVAL": 34,
    "ADDRESS_GPIO_0_AN_L_TRIG_HB": 35,
    "ADDRESS_GPIO_0_AN_L_TRIG_LVAL": 36,
    "ADDRESS_GPIO_0_AN_SAMPLE_INTER": 37,
    "ADDRESS_GPIO_1_AN_H_TRIG_HB": 38,
    "ADDRESS_GPIO_1_AN_H_TRIG_LVAL": 39,
    "ADDRESS_GPIO_1_AN_L_TRIG_HB": 40,
    "ADDRESS_GPIO_1_AN_L_TRIG_LVAL": 41,
    "ADDRESS_GPIO_1_AN_SAMPLE_INTER": 42,
    "ADDRESS_CTS_HOLD_TIME": 43,
    "ADDRESS_LOCATOR_ENABLE": 44,
    "ADDRESS_UNIQUE_ID_0": 45,
    "ADDRESS_UNIQUE_ID_1": 46,
    "ADDRESS_UNIQUE_ID_2": 47,
    "ADDRESS_UNIQUE_ID_3": 48,
    "ADDRESS_SYSTEM_ID_0": 49,
    "ADDRESS_SYSTEM_ID_1": 50,
    "ADDRESS_SYSTEM_ID_2": 51,
    "ADDRESS_SYSTEM_ID_3": 52,
    "ADDRESS_UART_BAUD_RATE": 53,
    "ADDRESS_UART_BITS": 54,
    "ADDRESS_UART_PARITY": 55,
    "ADDRESS_UART_STOP_BITS": 56,
    "ADDRESS_UART_FLOW_CONTROL": 58,
    "ADDRESS_SERIAL_BUF_FULL_MARGIN": 59,
    "ADDRESS_PART_NUM": 60,                 # to 70
    "ADDRESS_HW_REV": 72,                   # to 75
    "ADDRESS_FW_REV": 77,                   # to 80
    "ADDRESS_SECURITY_LEVEL": 81,
    "ADDRESS_MAX_PCK_LAT_TIME_BASE": 84,
    "ADDRESS_IMA_TIME_BASE": 85,
    "ADDRESS_END_DEVICE_WAIT_COMMAND": 86,
    "ADDRESS_END_DEVICE_WAKE_ENABLE": 87,
    "ADDRESS_CONFIG_MODE_ENTRY_CONTROL": 88,
    "ADDRESS_INDICATORS_ON": 89,
    "ADDRESS_RECEIVE_NEIGHBOUR_MSG": 90,
    "ADDRESS_COMMAND_ACKNOWLEDGE": 91,
    "ADDRESS_SLEEP_OR_RTS": 93,
    "ADDRESS_IMA_ON_CONNECT": 94,
    "ADDRESS_PWM_DEFAULT": 95,
    "ADDRESS_PWM_PULSE_COUNTER": 96,
    "ADDRESS_PWM_PULSE_COUNTER_DEBO": 97,
    "ADDRESS_CONNECT_CHANGE_MARGIN": 98,
    "ADDRESS_CLUST_NODE_LIMIT": 99,
    "ADDRESS_CLUST_NODE_RSSI": 100,
    "ADDRESS_DETECT_NET_BUSY": 101,
    "ADDRESS_RF_JAMMING_DETECT": 102,
    "ADDRESS_RF_JAMMMING_PORT": 103,
    "ADDRESS_FEEDBACK_PORT": 104,
    "ADDRESS_FEEDBACK_ENABLE": 105,
    "ADDRESS_IMA_DATA_CONTENT": 106,
    "ADDRESS_IMA_ADD_CONTENT": 107,
    "ADDRESS_TRIG_HOOLD": 108,
    "ADDRESS_END_DEVICE_AWAKE": 109,
    "ADDRESS_CONFIG_LOCK_OVERRIDE": 110,
    "ADDRESS_GROUP_TABLE": 113,             # to 120
    "ADDRESS_NEW_COMMAND_TIMEOUT": 121,
    "ADDRESS_COMMAND_RETRY": 122,
}

# Message detail types
MESSAGE_DIGITAL_INPUT_CHANGE = 0x01
MESSAGE_ANALOG_0_INPUT_TRIG = 0x02
MESSAGE_ANALOG_1_INPUT_TRIG	= 0x03
MESSAGE_RF_JAMMING_DETECTED	= 0x06
MESSAGE_DEVICE_RESET = 0x08
MESSAGE_STATUS_IMA = 0x09
MESSAGE_CHN_BUSY_SAME_SYS_ID = 0x0A
MESSAGE_CHN_FREE = 0x0B
MESSAGE_CHN_JAMMED = 0x0C
MESSAGE_OTHER_TM_SAME_CHN = 0x0D
MESSAGE_CMD_RCV_EXC_ACK = 0x10
MESSAGE_CMD_NRCV_NEXC_NACK = 0x11
MESSAGE_STATUS_MSG_NID = 0x12
MESSAGE_STATUS_MSG_NEXT_RCV = 0x13
MESSAGE_GET_PATH = 0x20
MESSAGE_GET_CONFIG_MEMORY = 0x21
MESSAGE_GET_CALIB_MEMORY = 0x22

# Packet types
packet_types_dict = {
    # Receive
    "PACKET_EVENT": 0x02,
    "PACKET_SERIAL": 0x10,
    "PACKET_BEACON": 0x0B,
    # Send
    "PACKET_SEND_CMD": 0x03,
    "PACKET_SEND_SERIAL": 0x11,
}

# TinyMesh commands (packet mode)
com_packet_mode_dict = {
    "CMD_PACKET_SET_OUTPUTS": 0x01,
    "CMD_PACKET_SET_PWM": 0x02,
    "CMD_PACKET_SET_CONFIG": 0x03,
    "CMD_PACKET_SET_GTW_CONFIG": 0x05,
    "CMD_PACKET_GET_NID": 0x10,
    "CMD_PACKET_GET_STATUS": 0x11,
    "CMD_PACKET_GET_DID_STATUS": 0x12,
    "CMD_PACKET_GET_CONF_MEM": 0x13,
    "CMD_PACKET_GET_CALIB_MEM": 0x14,
    "CMD_PACKET_FORCE_ROUTER_RST": 0x15,
    "CMD_PACKET_GET_PCK_PATH": 0x16,
}

# Other useful constants
BUFFER_SIZE = 64
N_CARS_TO_RECEIVE_WRITE_CMD = 1
N_CARS_TO_RECEIVE_WRITE_MEM = 1
N_CARS_TO_RECEIVE_READ_MEM = 2
N_CARS_TO_RECEIVE_READ_VALUE = 2
N_CARS_OF_MODULE_INFO = 21
N_CARS_TO_RECEIVE_AES_KEY = 1
N_CARS_AES_KEY = 16
N_CARS_TO_RECEIVE_BEACON_PACKET = 12


class TinyMeshSerialInterface:

    def __init__(self, bd):
        #Pins configuration to work with RCXXXX_TM library
        self.RF_RESET_PIN = 4
        self.RF_RTS_PIN = 17
        self.RF_CTS_PIN = 22
        self.RF_CONFIG_PIN = 18   
        self.RF_AWAKE_PIN = 23

        #Serial port configuration to work with RCXXXX_TM library
        self.rf_serial = serial.Serial("/dev/ttyS0", baudrate=bd, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE, bytesize=serial.EIGHTBITS, timeout=0)

        #Flag definition to work with RCXXXX_TM library
        self.rf_as_gateway = True

    def Close(self):
        self.rf_serial.close()

class TinyMeshModule:

    def __init__(self, baudrate):
        
        # Global variables
        self.cnt = 0
        self.state = STATE_NORMAL                # Variable to control RF module state machine
        self.in_buffer = [None] * BUFFER_SIZE    # Buffer to receive data from RF module
        self.out_buffer = [None] * BUFFER_SIZE   # Buffer to send data to RF module
        self.frame_buffer = [None] * BUFFER_SIZE # Frame process buffer
        self.in_buffer_wr_idx = 0                # Intput buffer write control
        self.in_buffer_rd_idx = 0                # Intput buffer read control
        self.in_buffer_rd_len = 0                # Number of bytes occupied in the input buffer
        self.out_buffer_wr_idx = 0               # Output buffer write control
        self.out_buffer_rd_idx = 0               # Output buffer read control
        self.out_buffer_wr_len = 0               # Number of bytes occupied in the output buffer
        self.timeout_value = 0                   # Limit value to consider timeout occurrence 
        self.timeout_flag = False                # Flag to signalize timeout occurrence 
        self.timeout_counter = 0                 # Timeout counter (counts in milliseconds)                                          
        self.frame_received = 0                  # Variable to count frames that have been received and not yet processed
        self.fw_version = ""                     # RF module firmware version
        self.hw_version = ""                     # RF module hardware version
        self.part_number = ""                    # RF module part number

        self.tinymesh_pkt_rcv = {                # Dictionary to handle packet mode reception frames
            "n_of_chars": 0,
            "origin_id": 0,
            "origin_rssi": 0,
            "origin_net_level": 0,
            "hop_counter": 0,
            "message_counter": 0,
            "latency_counter": 0,
            "packet": 0,
            "message": 0,
            "buffer": [None] * BUFFER_SIZE
        }

        self.tinymesh_beacon_pkt = {             # Dictionary to handle sniffed packets
            "rssi": 0,
            "packet_length": 0,
            "destination_id": 0,
            "source_id": 0,
            "origin_jump_level": 0,
            "packet_type": 0
        }
        
        self.tinymesh_pkt_send = {               # Dictionary to handle packet mode transmission frames
            "dest_id": [None] * 4,
            "packet_type": 0,
            "cmd_packet": 0,
            "out_buffer": [None] * BUFFER_SIZE,
            "n_chars": 0
        }

        self.serial = TinyMeshSerialInterface(baudrate)
        
        self.t = threading.Thread(target=self.handler)
        self.t.start()

        self.init_hw()


    def handler(self):
        t = threading.currentThread()
        while getattr(t, "do_run", True):
            time.sleep(0.001)
            self.cnt +=1
            if self.cnt == 1000:
                # print (self.state)
                self.cnt = 0
            try:
                data_left = self.serial.rf_serial.inWaiting()
            except:
                # ignore...  Let the loop retry.
                pass
            if data_left > 0:
                a = ''
                a = self.serial.rf_serial.read(1)
                self.receive_data(a)

            self.count_timeout()
            # print("timer = {}".format(self.timeout_counter))


    def stop_handler(self):
        self.t.do_run = False
        

    # Initialization of HW to operate RF module
    def init_hw(self):
        
        # GPIOs configuration
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.serial.RF_CONFIG_PIN, GPIO.OUT)
        GPIO.setup(self.serial.RF_RESET_PIN, GPIO.OUT)
        GPIO.setup(self.serial.RF_RTS_PIN, GPIO.OUT)
        GPIO.setup(self.serial.RF_CTS_PIN, GPIO.IN)
        GPIO.setup(self.serial.RF_AWAKE_PIN, GPIO.IN)

        # Set config pin initial state to 1
        GPIO.output(self.serial.RF_CONFIG_PIN, GPIO.HIGH)
        
        # Send reset signal
        GPIO.output(self.serial.RF_RESET_PIN, GPIO.LOW)
        time.sleep(0.1)
        GPIO.output(self.serial.RF_RESET_PIN, GPIO.HIGH)

        # Init state machine
        self.state = STATE_NORMAL

        # Init buffers
        self.clear_in_buffer()
        self.clear_out_buffer()
        
        # Init HW and FW versions and part number
        self.hw_version = ""
        self.fw_version = ""
        self.part_number = ""


    # Enter in sleep mode
    def enter_sleep_mode(self, sleep_mode):

        ret = EXIT_NOK

        # Enter in sleep mode acting RTS/SLEEP pin
        if sleep_mode == STATE_SLEEP_PIN:
            # Sleep enable
            GPIO.output(self.serial.RF_RTS_PIN, GPIO.LOW)
            self.state = STATE_SLEEP_PIN
            ret = EXIT_OK
        # Enter in sleep mode through config mode command
        elif sleep_mode == STATE_SLEEP_COMMAND:
            if self.enter_config_mode() == EXIT_OK:
                # To accept this command the config line must be and stay in LOW state
                GPIO.output(self.serial.RF_CONFIG_PIN, GPIO.LOW)
                # Put command in output buffer
                self.write_out_buffer(COMMAND_SET_SLEEP)
                # Send output buffer content
                self.send_out_buffer()
                self.timeout_counter = 0
                # Set time to declare timeout event
                self.timeout_value = SLEEP_ENTER_TIMEOUT
                # Wait until timeout
                while self.timeout_flag != True:
                    pass
                self.timeout_flag = False
                self.state = STATE_SLEEP_COMMAND
                ret = EXIT_OK
            else:
                ret = EXIT_NOK
        # Enter in sleep mode through USART (state update only)            
        elif sleep_mode == STATE_SLEEP_USART:
            self.state = STATE_SLEEP_USART
            ret = EXIT_OK
        
        return ret


    # Hold Device in Reset
    def hold_reset(self, hold_reset_time=1):
        GPIO.output(self.serial.RF_RESET_PIN, GPIO.LOW)

        time.sleep(hold_reset_time)

        GPIO.output(self.serial.RF_RESET_PIN, GPIO.HIGH)
    
    
    # Exit sleep mode
    def exit_sleep_mode(self, sleep_mode):

        ret = EXIT_NOK
        # Delay to guarantee at least 10ms of SLEEP time
        time.sleep(0.01)

        # Exit sleep mode by acting RTS/SLEEP pin
        if sleep_mode == STATE_SLEEP_PIN:
            # Sleep disable
            GPIO.output(self.serial.RF_RTS_PIN, GPIO.HIGH)
            self.timeout_counter = 0
            # Set time to declare timeout event
            self.timeout_value = SLEEP_EXIT_TIMEOUT
            # Wait until timeout
            while self.timeout_flag != True:
                pass
            self.timeout_flag = False
            self.state = STATE_NORMAL
            ret = EXIT_OK
        # Exit sleep mode by setting CONFIG in high            
        elif sleep_mode == STATE_SLEEP_COMMAND:
            # Sleep disable
            GPIO.output(self.serial.RF_CONFIG_PIN, GPIO.HIGH)
            self.timeout_counter = 0
            # Set time to declare timeout event
            self.timeout_value = SLEEP_EXIT_TIMEOUT
            # Wait until timeout
            while self.timeout_flag != True:
                pass
            self.timeout_flag = False
            self.state = STATE_NORMAL
            ret = EXIT_OK        
        # Exit sleep mode through serial port by sending character 0xFF        
        elif sleep_mode == STATE_SLEEP_USART:
            self.serial.rf_serial.write(0xFF)    
            self.state = STATE_NORMAL
            ret = EXIT_OK        
            
        return ret    


    # Return next byte from input buffer
    def read_in_buffer(self):
        next_char = 0xFF

        # See if there is a new byte to read. If yes, read it to next_char variable
        if self.in_buffer_rd_idx != self.in_buffer_wr_idx:
            next_char = self.in_buffer[self.in_buffer_rd_idx]
            self.in_buffer_rd_idx += 1
            # Circular buffer implementation
            if self.in_buffer_rd_idx == BUFFER_SIZE:
                self.in_buffer_rd_idx = 0
            # Decrementation of the number of bytes occupied in the input buffer    
            self.in_buffer_rd_len -= 1
        return next_char


    # Clear all bytes from output buffer
    def clear_out_buffer(self):
        self.out_buffer_wr_idx= 0
        self.out_buffer_rd_idx = 0
        self.out_buffer_rd_len = 0


    # Clear all bytes from input buffer
    def clear_in_buffer(self):
        self.in_buffer_wr_idx= 0
        self.in_buffer_rd_idx = 0
        self.in_buffer_rd_len = 0
        self.frame_received = 0


    # Enter in configuration mode
    def enter_config_mode(self):
        ret = EXIT_NOK

        if self.state == STATE_CONFIG:
            ret = EXIT_OK
        else:
            # If RF module is in sleep mode, wake it up
            if (self.state == STATE_SLEEP_PIN) or (self.state == STATE_SLEEP_COMMAND) or (self.state == STATE_SLEEP_USART):
                self.exit_sleep_mode(self.state)
                
            # Mark the state of the module...trying to change
            self.state = STATE_CHANGING
            # Enter in configuration mode by pulling CONFIG pin down
            GPIO.output(self.serial.RF_CONFIG_PIN, GPIO.LOW)

            # Wait until RF module handle the CTS line
            while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
                pass
            
            # Clear timeout flag
            self.timeout_flag = False 
            # Reset timeout counter
            self.timeout_counter = 0
            # Set time to declare timeout event
            self.timeout_value = CONFIG_TIMEOUT

            # Verify if RF module replies with character '>'. Otherwise, should exit by timeout and return error code
            while True:
                if self.in_buffer_rd_len != 0:
                    char = self.read_in_buffer()
                    if char == bytes(b'>'):
                        ret = EXIT_OK
                        self.state = STATE_CONFIG
                        self.timeout_counter = 0
                        self.timeout_value = 0
                        self.timeout_flag = False
                        GPIO.output(self.serial.RF_CONFIG_PIN, GPIO.HIGH)
                        break
                elif self.timeout_flag == True:
                    ret = EXIT_NOK
                    self.state = STATE_TIMEOUT
                    self.timeout_flag = False
                    GPIO.output(self.serial.RF_CONFIG_PIN, GPIO.HIGH)
                    break
        
        self.clear_in_buffer()
        return ret             


    # Read data from serial port to in_buffer
    # 'data' parameter is the character read from serial port
    def receive_data(self, data):

        self.in_buffer[self.in_buffer_wr_idx] = data
        self.in_buffer_wr_idx += 1
        
        # Circular buffer implementation
        if self.in_buffer_wr_idx == BUFFER_SIZE:
            self.in_buffer_wr_idx = 0
        # Update input buffer control variables
        if self.in_buffer_wr_idx == self.in_buffer_rd_idx:
            if self.in_buffer_wr_idx == 0:
                self.in_buffer_wr_idx = BUFFER_SIZE - 1
            else:
                self.in_buffer_wr_idx -= 1
        else:
            self.in_buffer_rd_len += 1

        if self.state == STATE_NORMAL:
            # In Packet Mode, the first data index indicates the number of bytes to receive
            if self.in_buffer_rd_len == self.in_buffer[self.in_buffer_rd_idx]:
                self.timeout_counter = 0
                self.timeout_value = 0
                self.frame_received += 1
            else:
                # Serial port timeout - end of frame
                self.timeout_value = SERIAL_TIMEOUT
                self.timeout_counter = 0
        elif self.state == STATE_SNIFFER:
            # Serial port timeout - end of frame
            self.timeout_value = SNIFFER_TIMEOUT
            self.timeout_counter = 0


    # Write a byte of data to the RF module output buffer
    def write_out_buffer(self, data):
        
        self.out_buffer[self.out_buffer_wr_idx] = data
        self.out_buffer_wr_idx += 1

        # Circular buffer implementation
        if self.out_buffer_wr_idx == BUFFER_SIZE:
            self.out_buffer_wr_idx = 0
        
        # Update input buffer control variables
        if self.out_buffer_wr_idx == self.out_buffer_rd_idx:
            if self.out_buffer_wr_idx == 0:
                self.out_buffer_wr_idx = BUFFER_SIZE - 1
            else:
                self.out_buffer_wr_idx -= 1    
        else:
            self.out_buffer_wr_len += 1


    # Send the output buffer contents to the RF module
    def send_out_buffer(self ):

        while self.out_buffer_rd_idx != self.out_buffer_wr_idx:
            byte_to_send = self.out_buffer[self.out_buffer_rd_idx]
            self.serial.rf_serial.write(byte_to_send)
            # print(hex(int.from_bytes(byte_to_send, 'big')))
            self.out_buffer_rd_idx += 1

            # Circular buffer implementation
            if self.out_buffer_rd_idx == BUFFER_SIZE:
                self.out_buffer_rd_idx = 0
            
            self.out_buffer_wr_len -= 1           


    # Read the memory content from one specific address (RF module has to be in Configuration Mode)
    def read_memory_value(self, address):

        ret = EXIT_COMM_ERROR

        # Add read command and memory address to output buffer
        self.write_out_buffer(COMMAND_READ_MEM)
        self.write_out_buffer(int.to_bytes(address, 1, 'big'))
        
        # Wait for CTS signal
        while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
            pass

        # Send data to RF module    
        self.send_out_buffer()

        # Set time to declare timeout event
        self.timeout_counter = 0
        self.timeout_value = READ_MEM_TIMEOUT

        while True:
            if self.in_buffer_rd_len == N_CARS_TO_RECEIVE_READ_MEM:
                self.timeout_counter = 0
                self.timeout_value = 0
                ret = self.read_in_buffer()
                # Format return value (string for address = 60 to 80, integer for all other addresses)
                if rcxxxx_configuration_memory["ADDRESS_PART_NUM"] <= address < rcxxxx_configuration_memory["ADDRESS_SECURITY_LEVEL"]:
                    ret = ret.decode('utf-8')
                else:
                    ret = int.from_bytes(ret,'big')
                break
            elif self.timeout_flag == True:
                self.timeout_flag = False
                ret = EXIT_COMM_ERROR
                self.state = STATE_TIMEOUT
                break
        self.clear_in_buffer()
        return ret


    # Write memory value to a specific address (RF module has to be in Configuration Mode)
    def write_memory_value(self, address, value):

        ret = EXIT_NOK
        
        # Set write command to output buffer
        self.write_out_buffer(COMMAND_WRITE_MEM)
        # Wait fot the correct state of the CTS line
        while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
            pass
        # Set time to declare timeout event
        self.timeout_value = WAIT_PROMPT_TIMEOUT
        # Send output buffer content
        self.send_out_buffer()
        # Check if prompt character was received. If not, exit by timeout
        while True:
            if self.in_buffer_rd_len == N_CARS_TO_RECEIVE_WRITE_MEM:
                if self.read_in_buffer() == bytes(b'>'):
                    self.timeout_counter = 0
                    self.timeout_value = 0
                    ret = EXIT_OK
                    time.sleep(0.003)
                    break
            elif self.timeout_flag == True:
                self.timeout_flag = False
                self.state = STATE_TIMEOUT
                ret = EXIT_NOK
                break


        # If write memory command was successfully sent, write a specific value to a specific address
        if self.state != STATE_TIMEOUT:
            # Set the address and data to write
            self.write_out_buffer(int.to_bytes(address, 1, 'big'))
            self.write_out_buffer(int.to_bytes(value, 1, 'big'))
            self.write_out_buffer(int.to_bytes(0xFF, 1, 'big'))
            
            # Wait fot the correct state of the CTS line
            while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
                pass
            # Set time to declare timeout event
            self.timeout_value = MEMORY_CONFIG_TIMEOUT      
            # Send command to RF module
            self.send_out_buffer()   
            # Check if prompt character was received. If not, exit by timeout
            while True:
                if self.in_buffer_rd_len == N_CARS_TO_RECEIVE_WRITE_MEM:
                    if self.read_in_buffer() == bytes(b'>'):
                        self.timeout_counter = 0
                        self.timeout_value = 0
                        ret = EXIT_OK
                        break
                elif self.timeout_flag == True:
                    self.timeout_flag = False
                    self.state = STATE_TIMEOUT
                    ret = EXIT_NOK
                    break            
        
        self.clear_in_buffer()
        return ret


    # Exit from configuration mode
    def exit_config_mode(self):

        ret = EXIT_NOK

        if self.state == STATE_CONFIG:
            # Add config command to output buffer
            self.write_out_buffer(COMMAND_EXIT_CONFIG)
            
            # Wait for RF module ready
            while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
                pass        
            
            # Send command
            self.send_out_buffer()
            
            # Set time to declare timeout event
            self.timeout_counter = 0
            self.timeout_value = CONFIG_TO_NORMAL_TIMEOUT
            # Wait until timeout
            while self.timeout_flag != True:
                pass

            self.timeout_flag = False
            self.timeout_value = 0
            self.timeout_counter = 0

            # Wait until the RF module release the CTS PIN
            #while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.HIGH:
            #    pass
            
            # Set state to Normal. In this case we don't have any feedback from the RF module
            self.state = STATE_NORMAL
            ret = EXIT_OK
        
        elif self.state == STATE_NORMAL:
            ret = EXIT_OK

        return ret


    # Read RF module part number, HW and FW version (RF module has to be in Configuration Mode)
    def read_part_number_and_fw_hw_vs(self):
        ret = EXIT_NOK
        rf_module_info = ""
        
        for i in range(N_CARS_OF_MODULE_INFO):
            rf_module_info += self.read_memory_value(rcxxxx_configuration_memory["ADDRESS_PART_NUM"] + i)
        
        [self.part_number, self.hw_version, self.fw_version] = rf_module_info.split(",")

        if self.part_number[:2] == 'RC':
            ret = EXIT_OK
            
        return ret


    # Count and declare timeout event (must be called every millisecond)
    def count_timeout(self):

        if self.timeout_value != 0:
            if self.timeout_counter == self.timeout_value:
                    self.timeout_flag = True
                    self.timeout_counter = 0
                    self.timeout_value = 0
                
                    # If the timeout occurs in normal mode operation, the timeout is caused
                    # by a serial port timeout event. It's time to process the received frame
                    if (self.state == STATE_NORMAL) or (self.state == STATE_SNIFFER):
                        self.frame_received += 1
            else:
                self.timeout_counter += 1


    # Get value from device, based on input parameter (RSSI, battery voltage, temperature)
    def get_value_from_device(self, cmd):

        ret = EXIT_COMM_ERROR
        # Add command to output buffer
        self.write_out_buffer(cmd)
        # Wait for CTS signal
        while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
            pass
        # Send command
        self.send_out_buffer()
        self.timeout_counter = 0
        # Set time to declare timeout event
        self.timeout_value = READ_MEM_TIMEOUT

        while True:
            if self.in_buffer_rd_len == N_CARS_TO_RECEIVE_READ_VALUE:
                self.timeout_counter = 0
                self.timeout_value = 0
                ret = self.read_in_buffer()
                break
            elif self.timeout_flag == True:
                self.timeout_flag = False
                ret = EXIT_COMM_ERROR
                self.state = STATE_TIMEOUT
                break
        self.clear_in_buffer()
        return ret    


    # Read RF module battery voltage (return value in millivolts)
    def read_battery_voltage(self):
        ret = EXIT_COMM_ERROR

        if self.state == STATE_CONFIG:
            ret = self.get_value_from_device(COMMAND_BATTERY)
            # Convert received value to integer and multiply by 30 millivolts to obtain the final result
            ret = (int.from_bytes(ret,'big')) * 30
        else:
            if self.enter_config_mode() == EXIT_OK:
                ret = self.get_value_from_device(COMMAND_BATTERY)
                # Convert received value to integer and multiply by 30 millivolts to obtain the final result
                ret = (int.from_bytes(ret,'big')) * 30
                self.exit_config_mode()
        return ret


    # Read RF module internal temperature (return value in ºC)
    def read_temperature(self):
        ret = EXIT_COMM_ERROR

        if self.state == STATE_CONFIG:
            ret = self.get_value_from_device(COMMAND_TEMPERATURE)
            # Convert received value to integer and subtracts 128 to obtain the final result in ºC
            ret = (int.from_bytes(ret,'big')) - 128
        else:
            if self.enter_config_mode() == EXIT_OK:
                ret = self.get_value_from_device(COMMAND_TEMPERATURE)
                # Convert received value to integer and subtracts 128 to obtain the final result in ºC
                ret = (int.from_bytes(ret,'big')) - 128
                self.exit_config_mode()
        return ret 


    # Read RF module RSSI (return value in dBm)
    def read_rssi(self):
        ret = EXIT_COMM_ERROR

        if self.state == STATE_CONFIG:
            ret = self.get_value_from_device(COMMAND_RSSI)
            # Convert received value to integer and divides by -2 to obtain the final result in dBm
            ret = (int.from_bytes(ret,'big')) / -2
        else:
            if self.enter_config_mode() == EXIT_OK:
                ret = self.get_value_from_device(COMMAND_RSSI)
                # Convert received value to integer and divides by -2 to obtain the final result in dBm
                ret = (int.from_bytes(ret,'big')) / -2
                self.exit_config_mode()
        return ret


    # Send command to RF module
    def send_command(self, cmd):

        ret = EXIT_NOK
        
        # Wait for CTS signal
        while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
            pass

        # Add command to output buffer
        self.write_out_buffer(cmd)
        # Set time to declare timeout event
        self.timeout_value = WAIT_CMD_PROMPT_TIMEOUT

        if cmd == COMMAND_RESET:
            # Add bytes 'TM' to output buffer to restore configuration memory to factory default values
            self.write_out_buffer(b'T')
            self.write_out_buffer(b'M')
        # Send command to RF module
        self.send_out_buffer()    

        if cmd != COMMAND_PACKET_SNIFFER:
            # See if RF module replies with prompt character, otherwise exit by timeout
            while True:
                if self.in_buffer_rd_len == N_CARS_TO_RECEIVE_WRITE_CMD:
                    if self.read_in_buffer() == bytes(b'>'):
                        self.timeout_counter = 0
                        self.timeout_value = 0
                        # Delay 50ms (time to save new data at flash)
                        time.sleep(0.05)
                        ret = EXIT_OK
                        break
                elif self.timeout_flag == True:
                    self.timeout_flag = False
                    self.state = STATE_TIMEOUT
                    ret = EXIT_NOK
                    break
        else:
            self.timeout_counter = 0
            self.timeout_value = 0
            ret = EXIT_OK

        self.clear_in_buffer()
        return ret    


    # Set device as end node
    def set_as_end_node(self):
        ret = EXIT_NOK

        if self.state == STATE_CONFIG:
            ret = self.send_command(COMMAND_SET_END_NODE)
        else:
            if self.enter_config_mode() == EXIT_OK:
                ret = self.send_command(COMMAND_SET_END_NODE)
                self.exit_config_mode()
        return ret        


    # Set device as gateway
    def set_as_gateway(self):
        ret = EXIT_NOK

        if self.state == STATE_CONFIG:
            ret = self.send_command(COMMAND_SET_GATEWAY)
        else:
            if self.enter_config_mode() == EXIT_OK:
                ret = self.send_command(COMMAND_SET_GATEWAY)
                self.exit_config_mode()
        return ret        


    # Set device as router
    def set_as_router(self):
        ret = EXIT_NOK

        if self.state == STATE_CONFIG:
            ret = self.send_command(COMMAND_SET_ROUTER)
        else:
            if self.enter_config_mode() == EXIT_OK:
                ret = self.send_command(COMMAND_SET_ROUTER)
                self.exit_config_mode()
        return ret


    # Restore default settings
    def reset_default_settings(self):
        ret = EXIT_NOK

        if self.state == STATE_CONFIG:
            ret = self.send_command(COMMAND_RESET)
        else:
            if self.enter_config_mode() == EXIT_OK:
                ret = self.send_command(COMMAND_RESET)
                self.exit_config_mode()
        return ret
                

    # Set device as packet sniffer
    def set_as_packet_sniffer(self):

        ret = EXIT_NOK

        if self.state == STATE_CONFIG:
            ret = self.send_command(COMMAND_PACKET_SNIFFER)
        else:
            if self.enter_config_mode() == EXIT_OK:
                ret = self.send_command(COMMAND_PACKET_SNIFFER)
        if ret == EXIT_OK:
            self.state = STATE_SNIFFER
        return ret


    # Exit from packet sniffer mode
    def exit_packet_sniffer(self):
        ret = EXIT_NOK

        if self.state == STATE_SNIFFER:
            self.send_command(COMMAND_PACKET_SNIFFER)
            self.enter_config_mode()
            ret = self.exit_config_mode()
        self.clear_in_buffer()
        return ret                    


    # Put RF module at a test mode (defined by input parameter). RF module has to be in configuration mode
    def set_test_mode(self, test_mode):
        ret = EXIT_NOK

        if (self.state == STATE_CONFIG ) or (self.state == STATE_SNIFFER):
            # Put character on output buffer
            self.write_out_buffer(test_mode)
            # Wait for CTS signal
            while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
                pass
            # Send command to RF module
            self.send_out_buffer()
            ret = EXIT_OK

        self.clear_in_buffer()
        return ret


    # Write a 16 byte key to RF module for AES encription. RF module has to be in configuration mode
    # 'key' should be a list of 16 elements (bytes)
    def set_aes_key(self, key):

        ret = EXIT_NOK
        
        # Set AES key, but only if RF module is in configuration mode
        if self.state == STATE_CONFIG:
            # Add command to output buffer
            self.write_out_buffer(COMMAND_SET_AES_KEY_1)
            self.write_out_buffer(COMMAND_SET_AES_KEY_2)
            # Wait for CTS signal
            while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
                pass        
            # Set time to declare timeout event
            self.timeout_value = WAIT_CMD_PROMPT_TIMEOUT
            # Send command to RF module
            self.send_out_buffer()
            
            while True:
                if self.in_buffer_rd_len == N_CARS_TO_RECEIVE_AES_KEY:
                    if self.read_in_buffer() == bytes(b'>'):
                        self.timeout_counter = 0
                        self.timeout_value = 0
                        ret = EXIT_OK
                        time.sleep(0.006)
                        self.clear_in_buffer()
                        break
                elif self.timeout_flag == True:
                    self.timeout_flag = False
                    self.state = STATE_TIMEOUT
                    ret = EXIT_NOK
                    break

            # Proceed with AES write only if command was sent correctly
            if self.state != STATE_TIMEOUT:
                self.clear_out_buffer()
                
                if len(key) == N_CARS_AES_KEY:
                    # Set AES key bytes
                    for byte in key:
                        self.write_out_buffer(int.to_bytes(byte, 1, 'big'))
                    # Wait for CTS signal
                    while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
                        pass        
                    # Set time to declare timeout event
                    self.timeout_value = WAIT_CMD_PROMPT_TIMEOUT
                    # Send command to RF module
                    self.send_out_buffer()

                    while True:
                        if self.in_buffer_rd_len == N_CARS_TO_RECEIVE_AES_KEY:
                            if self.read_in_buffer() == bytes(b'>'):
                                self.timeout_counter = 0
                                self.timeout_value = 0
                                ret = EXIT_OK
                                break
                        elif self.timeout_flag == True:
                            self.timeout_flag = False
                            self.state = STATE_TIMEOUT
                            ret = EXIT_NOK
                            break                    
                else:
                    ret = EXIT_NOK        
            self.clear_in_buffer()

        return ret


    # Fills up the output buffer with 'n_bytes' from list 'buffer'
    def fill_out_buffer(self, buffer, n_bytes):
        
        i = 0
        for i in range(n_bytes):
            # Fill the buffer
            self.out_buffer[self.out_buffer_wr_idx] = int.to_bytes(buffer[i], 1, 'big')
            self.out_buffer_wr_idx += 1
            # Prevent index overflow and implement circular buffer
            if self.out_buffer_wr_idx == BUFFER_SIZE:
                self.out_buffer_wr_idx = 0
            if self.out_buffer_wr_idx == self.out_buffer_rd_idx:
                if self.out_buffer_wr_idx == 0:
                    self.out_buffer_wr_idx = BUFFER_SIZE - 1
                else:
                    self.out_buffer_wr_idx -= 1
            else:
                self.out_buffer_wr_len += 1


    # Process the received frame according to TinyMesh protocol
    def process_frame(self):
        
        ret = EXIT_FRAME_NOT_RECEIVED

        self.frame_received -= 1            
        self.timeout_flag = False
        n_chars = self.in_buffer_rd_len
        self.frame_buffer[0] = self.read_in_buffer()

        if self.serial.rf_as_gateway == True:
            if type(self.frame_buffer[0]) is int:
                data = self.frame_buffer[0]
            else:
                data = int.from_bytes(self.frame_buffer[0], 'big')

            if n_chars == data:
                # Copy buffer to process it
                for i in range(1, n_chars):
                    self.frame_buffer[i] = self.read_in_buffer()

                self.tinymesh_pkt_rcv["origin_id"] = int.from_bytes(self.frame_buffer[FRAME_TM_ORI_ID3_INDEX], 'big')
                self.tinymesh_pkt_rcv["origin_id"] <<= 8
                self.tinymesh_pkt_rcv["origin_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_ORI_ID2_INDEX], 'big')    
                self.tinymesh_pkt_rcv["origin_id"] <<= 8
                self.tinymesh_pkt_rcv["origin_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_ORI_ID1_INDEX], 'big')
                self.tinymesh_pkt_rcv["origin_id"] <<= 8
                self.tinymesh_pkt_rcv["origin_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_ORI_ID0_INDEX], 'big')
                self.tinymesh_pkt_rcv["origin_rssi"] = int.from_bytes(self.frame_buffer[FRAME_TM_ORI_RSSI_INDEX], 'big')
                self.tinymesh_pkt_rcv["origin_net_level"] = int.from_bytes(self.frame_buffer[FRAME_TM_ORI_NET_LEVEL_INDEX], 'big')
                self.tinymesh_pkt_rcv["hop_counter"] = int.from_bytes(self.frame_buffer[FRAME_TM_HOP_CNT_INDEX], 'big')
                self.tinymesh_pkt_rcv["message_counter"] = int.from_bytes(self.frame_buffer[FRAME_TM_MSG_CNT0_INDEX], 'big')
                self.tinymesh_pkt_rcv["message_counter"] <<= 8
                self.tinymesh_pkt_rcv["message_counter"] |= int.from_bytes(self.frame_buffer[FRAME_TM_MSG_CNT1_INDEX], 'big')
                self.tinymesh_pkt_rcv["latency_counter"] = int.from_bytes(self.frame_buffer[FRAME_TM_LAT_CNT0_INDEX], 'big')
                self.tinymesh_pkt_rcv["latency_counter"] <<= 8
                self.tinymesh_pkt_rcv["latency_counter"] |= int.from_bytes(self.frame_buffer[FRAME_TM_LAT_CNT1_INDEX], 'big')            
                self.tinymesh_pkt_rcv["packet"] = int.from_bytes(self.frame_buffer[FRAME_TM_PCK_TYPE_INDEX], 'big')

                # General event packet format
                if self.tinymesh_pkt_rcv["packet"] == packet_types_dict["PACKET_EVENT"]:
                    self.tinymesh_pkt_rcv["message"] = int.from_bytes(self.frame_buffer[FRAME_TM_MESSAGE_DETAIL], 'big')
                # Serial packet format    
                elif self.tinymesh_pkt_rcv["packet"] == packet_types_dict["PACKET_SERIAL"]:
                    self.tinymesh_pkt_rcv["n_of_chars"] = 0
                    for i in range(FRAME_TM_PAYLOAD_INDEX, n_chars):
                        self.tinymesh_pkt_rcv["buffer"][self.tinymesh_pkt_rcv["n_of_chars"]] = int.from_bytes(self.frame_buffer[i], 'big')
                        self.tinymesh_pkt_rcv["n_of_chars"] += 1     
                ret = EXIT_FRAME_OK
            else:
                self.clear_in_buffer()
                ret = EXIT_FRAME_DISCARD        
        else:
            # Copy buffer to process it
            for i in range(1, n_chars):
                self.frame_buffer[i] = self.read_in_buffer()
            
            self.tinymesh_pkt_rcv["n_of_chars"] = 0
            
            for i in range(n_chars):
                self.tinymesh_pkt_rcv["buffer"][self.tinymesh_pkt_rcv["n_of_chars"]] = int.from_bytes(self.frame_buffer[i], 'big')
                self.tinymesh_pkt_rcv["n_of_chars"] += 1

            ret = EXIT_FRAME_OK    
        
        return ret


    # Process the received frame according to TinyMesh protocol in sniffer mode
    def process_sniffer_frame(self):
        
        ret = EXIT_FRAME_NOT_RECEIVED

        # Decrement frame received counter
        self.frame_received -= 1
        self.timeout_flag = False
        n_chars = self.in_buffer_rd_len
        self.frame_buffer[0] = self.read_in_buffer()

        if n_chars == N_CARS_TO_RECEIVE_BEACON_PACKET:
            # Copy buffer to process it
            for i in range(1, n_chars):
                self.frame_buffer[i] = self.read_in_buffer()

            # Validate the beacon packet
            if int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_PCKT_TYPE], 'big') == packet_types_dict["PACKET_BEACON"]:

                self.tinymesh_beacon_pkt["rssi"] = int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_RSSI], 'big')
                self.tinymesh_beacon_pkt["rssi"] /= -2
                self.tinymesh_beacon_pkt["packet_length"] = int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_PCKT_LEN], 'big')
                self.tinymesh_beacon_pkt["destination_id"] = int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_DEST_ID3], 'big')
                self.tinymesh_beacon_pkt["destination_id"] <<= 8
                self.tinymesh_beacon_pkt["destination_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_DEST_ID2], 'big')
                self.tinymesh_beacon_pkt["destination_id"] <<= 8
                self.tinymesh_beacon_pkt["destination_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_DEST_ID1], 'big')
                self.tinymesh_beacon_pkt["destination_id"] <<= 8
                self.tinymesh_beacon_pkt["destination_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_DEST_ID0], 'big')                        
                self.tinymesh_beacon_pkt["source_id"] = int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_SRC_ID3], 'big')
                self.tinymesh_beacon_pkt["source_id"] <<= 8
                self.tinymesh_beacon_pkt["source_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_SRC_ID2], 'big')
                self.tinymesh_beacon_pkt["source_id"] <<= 8
                self.tinymesh_beacon_pkt["source_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_SRC_ID1], 'big')
                self.tinymesh_beacon_pkt["source_id"] <<= 8
                self.tinymesh_beacon_pkt["source_id"] |= int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_SRC_ID0], 'big')
                self.tinymesh_beacon_pkt["origin_jump_level"]  = int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_JUMP_LV], 'big')
                self.tinymesh_beacon_pkt["packet_type"] = int.from_bytes(self.frame_buffer[FRAME_TM_SNIF_PCKT_TYPE], 'big')

                ret = EXIT_FRAME_OK
            else:
                ret = EXIT_FRAME_DISCARD    
        else:
            self.clear_in_buffer()
            ret = EXIT_FRAME_DISCARD

        return ret


    # Compose the packet and send it to the the network
    def send_packet_from_gtw(self):

        ret = EXIT_NOT_READY

        if self.state == STATE_NORMAL:

            # print(self.tinymesh_pkt_send)

            if self.tinymesh_pkt_send["packet_type"] == packet_types_dict["PACKET_SEND_SERIAL"]:
                # 1 start char + 4 dest ID + 1 cmd number + 1 packet type 
                bytes_to_send = 7
            else:
                # 1 start char + 4 dest ID + 1 cmd number + 1 packet type + 1 cmd argument
                bytes_to_send = 8
                self.tinymesh_pkt_send["n_chars"] = 2
            
            # Total number of bytes to send
            bytes_to_send += self.tinymesh_pkt_send["n_chars"]

            # print(f'Bytes to Send: {bytes_to_send}')

            self.write_out_buffer(int.to_bytes(bytes_to_send, 1, 'big'))                     # Start character
            self.fill_out_buffer(self.tinymesh_pkt_send["dest_id"], 4)                            # Destination address
            self.write_out_buffer(int.to_bytes(bytes_to_send, 1, 'big'))                     # Command number (don't care)
            self.write_out_buffer(int.to_bytes(self.tinymesh_pkt_send["packet_type"], 1, 'big'))  # Packet type

            if self.tinymesh_pkt_send["packet_type"] == packet_types_dict["PACKET_SEND_CMD"]:
                self.write_out_buffer(int.to_bytes(self.tinymesh_pkt_send["cmd_packet"], 1, 'big'))
                self.fill_out_buffer(self.tinymesh_pkt_send["out_buffer"], 2)
            else:
                self.fill_out_buffer(self.tinymesh_pkt_send["out_buffer"], self.tinymesh_pkt_send["n_chars"])

            # Wait for module to be ready to receive data from serial port
            while GPIO.input(self.serial.RF_CTS_PIN) != GPIO.LOW:
                pass

            self.send_out_buffer()
            ret = EXIT_FRAME_SENT

        return ret


    def baudrate_codification(self, bd):
        if bd == 2400:
            return 1
        elif bd == 4800:
            return 2
        elif bd == 9600:
            return 3
        elif bd == 14400:
            return 4
        elif bd == 19200:
            return 5
        elif bd == 28800:
            return 6
        elif bd == 38400:
            return 7
        elif bd == 56700:
            return 8
        elif bd == 76800:
            return 9
        elif bd == 115200:
            return 10
        elif bd == 230400:
            return 11
        else:
            return 5    # Default Value
