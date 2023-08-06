
from collections.abc import Iterable
import struct
import math

from rcxxxx_tm_lib import com_packet_mode_dict as tinymesh_packet_mode_commands
from rcxxxx_tm_lib import packet_types_dict as tinymesh_packet_types

class TekonDefinitions():
    # Maximum Devices from each Family
    NUM_MAX_DEVICES = 55

    # Tekon Products Identification Dictionary
    products_dict = {
        "DUOS GATEWAY 868MHz": 1,
        "DUOS REPEATER 868MHz": 2,
        "DUOS TEMP 868MHz": 3,
        "GATEWAY 2.4Hz": 4,
        "REPEATER 2.4GHz": 5,
        "DUOS END DEVICE 2.4GHz HP": 6,
        "DUOS END DEVICE 2.4GHz LP": 7,
        "PLUS GATEWAY 4 ANALOG 868MHz": 8,
        "PLUS TWP-4AI 868MHz": 9,
        "PLUS REPEATER 868MHz": 10,
        "DUOS HYGROTEMP 868MHz": 11,
        "DUOS DI+TEMP 868MHz": 12,
        "DUOS CO2 868MHz": 13,
        "DUOS MULTITEMP 868MHz": 14,
        "DUOS AIRQ 868MHz": 15,
        "DUOS TEMP 2.4GHz": 16,
        "DUOS HYGROTEMP 2.4GHz": 17,
        "DUOS DI+TEMP 2.4GHz": 18,
        "DUOS CO2 2.4GHz": 19,
        "DUOS MULTITMEP 2.4GHz": 20,
        "DUOS AIRQ 2.4GHz": 21,
        "DUOS GATEWAY 2.4GHz": 22,
        "DUOS REPEATER 2.4GHz": 23,
        "PLUS TWPH-1UT 868MHz": 24,
        "THU301": 25,
        "PLUS TWP-4AI 915MHZ": 26,
        "PLUS REPEATER 915MHZ": 27,
        "PLUS TWPH-1UT 915MHZ": 28,
        "DUOS TEMP 915MHZ": 29,
        "DUOS HYGROTEMP 915MHZ": 30,
        "DUOS DI+TEMP 915MHZ": 31,
        "DUOS CO2 915MHZ": 32,
        "DUOS MULTITEMP 915MHZ": 33,
        "DUOS AIRQ 915MHZ": 34,
        "DUOS GATEWAY 915MHZ": 35,
        "DUOS REPEATER 915MHZ": 36,
        "PLUS TWP-4AI/4DI/1UT 868MHz": 37,
        "PLUS TWP-4AI/4DI/1UT 915MHz": 38,
        "PLUS TWP-4DI/1UT 868MHz": 39,
        "PLUS TWP-4DI/1UT 915MHz": 40,
        "THP102": 41,
        "THT202": 42,
        "PLUS GATEWAY 4 ANALOG 915MHz": 43,
        "TDU301": 44,
        "PLUS TWP-1UT 868MHz": 45,
        "PLUS TWP-2UT 868MHz": 46,
        "PLUS TWP-1AI 868MHz": 47,
        "PLUS TWP-2AI 868MHz": 48,
        "PLUS TWP-1DI 868MHz": 49,
        "PLUS TWP-2DI 868MHz": 50,
        "PLUS TWP-1UT 915MHz": 51,
        "PLUS TWP-2UT 915MHz": 52,
        "PLUS TWP-1AI 915MHz": 53,
        "PLUS TWP-2AI 915MHz": 54,
        "PLUS TWP-1DI 915MHz": 55,
        "PLUS TWP-2DI 915MHz": 56,
        "WIRELESS SERIAL WSM-101 868MHz": 57,
        "WIRELESS SERIAL WSM-101 915MHz": 58,
        "DUOS inHygroTemp 868MHz": 59,
        "DUOS inCO2 868MHz": 60,
        "DUOS inAirQuality 868MHz": 61,
        "DUOS inTemp 868MHz": 62,
        "DUOS inHygroTemp 915MHz": 63,
        "DUOS inCO2 868MHz": 64,
        "DUOS inAirQuality 915MHz": 65,
        "DUOS inTemp 915MHz": 66,
        "DUOS uTemp 868MHz": 67,
        "DUOS uTemp 915MHz": 68,
        "THM 502-I": 69,
        "THM 602-I": 70,
        "TDU 302": 71,    
    }

    # Tekon Sensors Codes Dictionary
    duos_sensors_dict = {
        "TK9808": 1,
        "TK07": 2,
        "TK939": 3,
        "TK871": 4,
        "MULTI TK9808": 5,
        "TK2806713": 6,
        "PT100 (LASMA)": 7,
        "TK280": 8,
        "TK895": 9,
        "PT100 2W": 10,
        "PT100 3W": 11,
        "PT100 4W": 12,
        "PT500 2W": 13,
        "PT500 3W": 14,
        "PT500 4W": 15,
        "PT1000 2W": 16,
        "PT1000 3W": 17,
        "PT1000 4W": 18,
        "TC J": 19,
        "TC K": 20,
        "TC R": 21,
        "TC S": 22,
        "TC T": 23,
        "TC N": 24,
        "TC C": 25,
        "Linear Ohm": 26,
        "Linear mV": 27,
        "TK8095": 28,
        "TK30": 29,
        "Unknown": 255,
    }

    # TinyMesh RF Power & Datarate Channels Dictionary
    tinymesh_ch_conf = {
        "169MHz": {
            ch: {"RF Power": 5, "RF Baudrate": 5}  for ch in range(1, 14)
        },
        "868MHz": {
            1: { "RF Power": 4, "RF Baudrate": 3 },
            2: { "RF Power": 4, "RF Baudrate": 5 },
            3: { "RF Power": 4, "RF Baudrate": 5 },
            4: { "RF Power": 4, "RF Baudrate": 5 },
            5: { "RF Power": 4, "RF Baudrate": 5 },
            6: { "RF Power": 4, "RF Baudrate": 3 },
            7: { "RF Power": 4, "RF Baudrate": 3 },
            8: { "RF Power": 4, "RF Baudrate": 5 },
            9: { "RF Power": 4, "RF Baudrate": 5 },
            10: { "RF Power": 4, "RF Baudrate": 5 },
            11: { "RF Power": 4, "RF Baudrate": 5 },
            12: { "RF Power": 4, "RF Baudrate": 3 },
            13: { "RF Power": 5, "RF Baudrate": 5 },
            14: { "RF Power": 4, "RF Baudrate": 3 },
            15: { "RF Power": 4, "RF Baudrate": 5 },
            16: { "RF Power": 4, "RF Baudrate": 3 },
        },
        "915MHz": {
            ch: {"RF Power": 5, "RF Baudrate": 5}  for ch in range(1, 51)
        },
    }

class TinymeshTekon:
    # TinyMesh Encription Key
    tekon_aes_key = (0x28, 0x6F, 0x29, 0x20, 0x2B, 0x20, 0x2E, 0x7C, 0x2E, 0x20, 0x3D, 0x20, 0x3A, 0x29, 0x20, 0x23)

    # RCXXXX family part numbers
    rcxxxx_partnumber_dict = {
        "RC2500HP_PARTNUMBER": "RC2500HP-TM",
        "RC1190HP_PARTNUMBER": "RC1190HP-TM",
        "RC1191HP_PARTNUMBER": "RC1191HP-TM",
        "RC1180HP_PARTNUMBER": "RC1180HP-TM",
        "RC1181HP_PARTNUMBER": "RC1181HP-TM",
        "RC1701HP_PARTNUMBER": "RC1701HP-TM",
    }

    """
    Datapacket received from DUOS Remote Devices.
    """
    tekwi_receive_datapacket_plus = {
        "Modbus Index": 0,
        "Device Model": "Unknown",
        "Refresh Time": 0,
        "Power Voltage": 0,
        "FW Version": "0.0.0",
        "HW Version": "0.0",
        "Data": [0, 0, 0, 0, 0],
        "IO Coils": [[0] * 8 , [0] * 8],
        "Config Words": [0, 0, 0, 0],
        "Check Sum": 0,
        "Sizeof Datapacket": 42,
    }

    """
    Datapacket used to send Remote Commands from 
    Gateway to PLUS Remote Devices.
    """
    tekwi_send_datapacket_plus = {
        "Num Bytes": 0,
        "Time Refresh": 0,
        "Data": [0, 0, 0, 0, 0],
        "IO Coils": [0, 0],
        "Config Words": [0, 0, 0, 0],
        "Check Sum": 0,
        "Sizeof Datapacket": 35,
    }

    """
    Datapacket received from DUOS Remote Devices.
    """
    tekwi_receive_datapacket_duos = {
        "Transmitter Model": "Unknown",
        "Probe Model": "Unknown",
        "Refresh Time": 0,
        "Power Voltage": 0,
        "FW Version": "0.0.0",
        "HW Version": "0.0",
        "Data": [0, 0, 0, 0, 0, 0],
        "Check Sum": 0,
        "Sizeof Datapacket": 35,
    }

    """
    Datapacket used to send Remote Commands from 
    Gateway to DUOS Remote Devices.
    """
    tekwi_send_datapacket_duos = {
        "Num Bytes": 0,
        "Time Refresh": 0,
        "Check Sum": 0,
        "Sizeof Datapacket": 5,
    }

def pack_tekwi_plus_datapacket(payload):

    buffer = []
    # Convert payload combination type values to a single list of values
    values = list(flatten(payload.values()))
    values.pop()

    for value in values:
        # print(value)
        if type(value) is float:
            aux = bytearray(4)
            aux = int.from_bytes(bytes(bytearray(struct.pack("f", value))), 'big')
            aux = list(aux.to_bytes(4, 'big'))
            aux = list(flatten(aux))
            for v in aux:
                buffer.append(v)
        elif value > 65535:
            aux = value.to_bytes(4, 'big')
            aux = list(flatten(list(aux)))
            # print(aux)
            for v in aux:
                buffer.append(v)
        elif value > 255:
            aux = value.to_bytes(2, 'little')
            aux = list(flatten(list(aux)))
            for v in aux:
                buffer.append(v)
        else:
            buffer.append(value)

    if payload['Time Refresh'] < 255:
        buffer.insert(2, 0)

    chk = tekwi_chksum_calc(buffer, len(buffer))
    chk = list(flatten(list(chk.to_bytes(2, 'little'))))
    
    buffer = buffer + ([0] * (payload.get("Num Bytes") - len(buffer) - len(chk))) + chk

    return buffer


def pack_tekwi_duos_datapacket(payload):

    buffer = []
    # Convert payload combination type values to a single list of values
    values = list(flatten(payload.values()))
    values.pop()
    # pop porque nem nos interessa o sizeof datapacket nem o checksum
    values.pop()

    for value in values:
        # print(value)
        if type(value) is float:
            aux = bytearray(4)
            aux = int.from_bytes(bytes(bytearray(struct.pack("f", value))), 'big')
            aux = list(aux.to_bytes(4, 'big'))
            aux = list(flatten(aux))
            for v in aux:
                buffer.append(v)
        elif value > 65535:
            aux = value.to_bytes(4, 'big')
            aux = list(flatten(list(aux)))
            # print(aux)
            for v in aux:
                buffer.append(v)
        elif value > 255:
            aux = value.to_bytes(2, 'little')
            aux = list(flatten(list(aux)))
            for v in aux:
                buffer.append(v)
        else:
            buffer.append(value)

    # Se o communication period for menor q 256, temos que adicionar o outro byte
    if len(buffer) == 2:
        buffer.append(0)    
    # print(buffer)
    # Adicionados 2 bytes por causa da condicao de paragem no calculo do checksum        
    chk = tekwi_chksum_calc(buffer, (len(buffer) + 2))
    chk = list(flatten(list(chk.to_bytes(2, 'little'))))
    buffer = buffer + ([0] * (payload.get("Num Bytes") - len(buffer) - len(chk))) + chk

    return buffer


def unpack_tekwi_plus_datapacket(payload, payload_length):

    chk_sum = tekwi_chksum_calc(payload, payload_length)
    TinymeshTekon.tekwi_receive_datapacket_plus["Check Sum"] = (payload[payload_length - 1] << 8) + payload[payload_length - 2]

    if TinymeshTekon.tekwi_receive_datapacket_plus["Check Sum"] == chk_sum:
        node_index = payload[0]

        TinymeshTekon.tekwi_receive_datapacket_plus["Modbus Index"] = payload[0] + 1
        TinymeshTekon.tekwi_receive_datapacket_plus["Device Model"] = payload[1]
        TinymeshTekon.tekwi_receive_datapacket_plus["Refresh Time"] = payload[2] + (payload[3] << 8)
        TinymeshTekon.tekwi_receive_datapacket_plus["Power Voltage"] = float(payload[4]) / 10

        aux = [str(payload[5]), str(payload[6]), str(payload[7])]
        TinymeshTekon.tekwi_receive_datapacket_plus["FW Version"] = '.'.join(aux)

        aux = [str(payload[8]), str(payload[9])]
        TinymeshTekon.tekwi_receive_datapacket_plus["HW Version"] = '.'.join(aux)

        # Data fields
        tek_wi_data = payload[10:30]
        array = [tek_wi_data[i:(i+4):1] for i in range(0, 20) if i % 4 == 0]
        # print(array)

        i = 0
        for v in array:
            v.reverse()
            b = bytes(v)
            aux = struct.unpack('>f', b)
            value = list(aux)
            TinymeshTekon.tekwi_receive_datapacket_plus["Data"][i] = value[0]
            TinymeshTekon.tekwi_receive_datapacket_plus["Data"][i] = round(value[0], 5)
            i += 1

        # IO Coils
        TinymeshTekon.tekwi_receive_datapacket_plus["IO Coils"][0] = int2bitslist(payload[30])
        TinymeshTekon.tekwi_receive_datapacket_plus["IO Coils"][1] = int2bitslist(payload[31])

        # Config Words
        tek_wi_data = payload[32:40]
        array = [tek_wi_data[i:(i+2):1] for i in range(0, 8) if i % 2 == 0]

        i = 0
        for v in array:
            # print(v)
            value = (v[0] << 8) + v[1]
            TinymeshTekon.tekwi_receive_datapacket_plus["Config Words"][i] = value
            i += 1

        # print(f'Transmitter Index: {TinymeshTekon.tekwi_receive_datapacket_plus["Modbus Index"]}')
        # print(f'Device Model: {device_model_decoding(payload[1])} ({TinymeshTekon.tekwi_receive_datapacket_plus["Device Model"]})')
        # print(f'Refresh Time: {TinymeshTekon.tekwi_receive_datapacket_plus["Refresh Time"]} (s)')
        # print(f'Power Supply Voltage: {TinymeshTekon.tekwi_receive_datapacket_plus["Power Voltage"]} (V)')
        # print(f'FW Version: {TinymeshTekon.tekwi_receive_datapacket_plus["FW Version"]}')
        # print(f'HW Version: {TinymeshTekon.tekwi_receive_datapacket_plus["HW Version"]}')
        # print(f'Data: {TinymeshTekon.tekwi_receive_datapacket_plus["Data"]}')
        # print(f'IO Coils: {TinymeshTekon.tekwi_receive_datapacket_plus["IO Coils"]}')
        # print(f'Config Words: {TinymeshTekon.tekwi_receive_datapacket_plus["Config Words"]}')

        return [node_index, TinymeshTekon.tekwi_receive_datapacket_plus]


def unpack_tekwi_duos_datapacket(payload, payload_length, device_index):

    chk_sum = tekwi_chksum_calc(payload, payload_length)
    TinymeshTekon.tekwi_receive_datapacket_duos["Check Sum"] = (payload[payload_length - 1] << 8) + payload[payload_length - 2]

    if TinymeshTekon.tekwi_receive_datapacket_duos["Check Sum"] == chk_sum:
        node_index = device_index & 255

        TinymeshTekon.tekwi_receive_datapacket_duos["Transmitter Model"] = payload[0]
        TinymeshTekon.tekwi_receive_datapacket_duos["Probe Model"] = payload[1]
        TinymeshTekon.tekwi_receive_datapacket_duos["Refresh Time"] = payload[2] + (payload[3] << 8)
        TinymeshTekon.tekwi_receive_datapacket_duos["Power Voltage"] = float(payload[4]) / 10

        aux = [str(payload[5]), str(payload[6]), str(payload[7])]
        TinymeshTekon.tekwi_receive_datapacket_duos["FW Version"] = '.'.join(aux)

        aux = [str(payload[8] >> 4), str(payload[8] & 15)]
        TinymeshTekon.tekwi_receive_datapacket_duos["HW Version"] = '.'.join(aux)

        # Data fields
        tek_wi_data = payload[9:payload_length - 2]
        array = [tek_wi_data[i:(i+4):1] for i in range(0, 24) if i % 4 == 0]

        i = 0
        for v in array:
            if len(v) == 0:
                v = [0, 0, 0, 0]
            else:
                v.reverse()
                b = bytes(v)
                aux = struct.unpack('>f', b)
                value = list(aux)
                TinymeshTekon.tekwi_receive_datapacket_duos["Data"][i] = value[0]
                TinymeshTekon.tekwi_receive_datapacket_duos["Data"][i] = round(value[0], 4)
            i += 1

        # print(f'Transmitter Model: {device_model_decoding(TinymeshTekon.tekwi_receive_datapacket_duos["Transmitter Model"])}')
        # print(f'Sensor Model: {probe_duos_model_decoding(TinymeshTekon.tekwi_receive_datapacket_duos["Probe Model"])} ({TinymeshTekon.tekwi_receive_datapacket_duos["Probe Model"]})')
        # print(f'Refresh Time: {TinymeshTekon.tekwi_receive_datapacket_duos["Refresh Time"]} (s)')
        # print(f'Power Supply Voltage: {TinymeshTekon.tekwi_receive_datapacket_duos["Power Voltage"]} (V)')
        # print(f'FW Version: {TinymeshTekon.tekwi_receive_datapacket_duos["FW Version"]}')
        # print(f'HW Version: {TinymeshTekon.tekwi_receive_datapacket_duos["HW Version"]}')
        # print(f'Data: {TinymeshTekon.tekwi_receive_datapacket_duos["Data"]}')

        return [node_index, TinymeshTekon.tekwi_receive_datapacket_duos]


def send_data_2_end_device(data, command_size, RCXXXX_TM):

    RCXXXX_TM.tinymesh_pkt_send["packet_type"] = tinymesh_packet_types["PACKET_SEND_SERIAL"]
    RCXXXX_TM.tinymesh_pkt_send["cmd_packet"] = tinymesh_packet_mode_commands["CMD_PACKET_GET_PCK_PATH"]

    buffer = []
    aux = RCXXXX_TM.tinymesh_pkt_rcv["origin_id"].to_bytes(4, 'big')
    aux = list(flatten(list(aux)))
    for v in aux:
        buffer.append(v)
    RCXXXX_TM.tinymesh_pkt_send["dest_id"] = list(reversed(buffer))
    # print(f'Dest ID: {RCXXXX_TM.tinymesh_pkt_send["dest_id"]}')

    if command_size == TinymeshTekon.tekwi_send_datapacket_plus["Sizeof Datapacket"]:
        TinymeshTekon.tekwi_send_datapacket_plus["Num Bytes"] = TinymeshTekon.tekwi_send_datapacket_plus["Sizeof Datapacket"]
        TinymeshTekon.tekwi_send_datapacket_plus["Time Refresh"] = data["Refresh Time"]
        TinymeshTekon.tekwi_send_datapacket_plus["Data"][0] = data["Data"][0]
        TinymeshTekon.tekwi_send_datapacket_plus["Data"][1] = data["Data"][1]
        TinymeshTekon.tekwi_send_datapacket_plus["Data"][2] = data["Data"][2]
        TinymeshTekon.tekwi_send_datapacket_plus["Data"][3] = data["Data"][3]
        TinymeshTekon.tekwi_send_datapacket_plus["Data"][4] = data["Data"][4]

        index = 0
        TinymeshTekon.tekwi_send_datapacket_plus["IO Coils"] = [0, 0]

        for bit in data["IO Coils"][0]:
            TinymeshTekon.tekwi_send_datapacket_plus["IO Coils"][0] += bit * (2**index)
            index+=1
        
        index = 0
        for bit in data["IO Coils"][1]:
            TinymeshTekon.tekwi_send_datapacket_plus["IO Coils"][1] += bit * (2**index)
            index+=1

        TinymeshTekon.tekwi_send_datapacket_plus["Config Words"] = data["Config Words"]
        
        RCXXXX_TM.tinymesh_pkt_send["out_buffer"] = pack_tekwi_plus_datapacket(TinymeshTekon.tekwi_send_datapacket_plus)
        RCXXXX_TM.tinymesh_pkt_send["n_chars"] = TinymeshTekon.tekwi_send_datapacket_plus["Num Bytes"]

    elif command_size == TinymeshTekon.tekwi_send_datapacket_duos["Sizeof Datapacket"]:
        TinymeshTekon.tekwi_send_datapacket_duos["Num Bytes"] = TinymeshTekon.tekwi_send_datapacket_duos["Sizeof Datapacket"]
        TinymeshTekon.tekwi_send_datapacket_duos["Time Refresh"] = data["Refresh Time"]

        RCXXXX_TM.tinymesh_pkt_send["out_buffer"] = pack_tekwi_duos_datapacket(TinymeshTekon.tekwi_send_datapacket_duos)
        RCXXXX_TM.tinymesh_pkt_send["n_chars"] = TinymeshTekon.tekwi_send_datapacket_duos["Num Bytes"]

    # print('Buffer: [{}] Buffer size: {}'.format(', '.join(hex(x) for x in RCXXXX_TM.tinymesh_pkt_send["out_buffer"]), RCXXXX_TM.tinymesh_pkt_send["n_chars"]))
    RCXXXX_TM.send_packet_from_gtw()


def tekwi_chksum_calc(payload, payload_length):
    i = 0
    chk_sum = 0

    for value in payload:
        i += 1
        if i > payload_length - 2:
            break
        chk_sum += value

        # print(value)

    # print(f'Send CHK: {(payload[payload_length - 1] << 8) + payload[payload_length - 2]} Calc CHK: {chk_sum}\n')

    return chk_sum


def device_model_decoding(code):

    for k, v in TekonDefinitions.products_dict.items():
        # print(k, v, code)
        if v == code:
            return k

    return "Unknown"


def probe_duos_model_decoding(code):

    for k, v in TekonDefinitions.duos_sensors_dict.items():
        # print(k, v, code)
        if v == code:
            return k

    return "Unknown"


def int2bitslist(value):
    out = [0] * 8

    if value != 0:
        bits = int(max(8, math.log(value, 2)+1))
        out = [1 if value & (1 << (bits-1-n)) else 0 for n in range(bits)]
        out.reverse()

    # print(out)
    return out


def int2byteslist(value):

    # Decompose wireless_net_id int in 4 bytes
    value = [int(value >> i & 0xff) for i in (0, 8, 16, 24)]

    return value


def flatten(lis):
    for item in lis:
        if isinstance(item, Iterable) and not isinstance(item, str):
            for x in flatten(item):
                yield x
        else:
            yield item