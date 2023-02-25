import struct
from helpers.transformers import *


def get_id_ox7e3(result : dict):
    # - ID 0x7e3, which contains the following fields (in this order)

    # - roll axis input as a 2 byte signed integer in `[-32768, 32767]` that cor0responds to a commanded angle in `[-30, 30]` degrees
    # - pitch axis input as a 2 byte signed integer in `[-32768, 32767]` that corresponds to a commanded angle in `[-30, 30]` degrees
    # - yaw axis input as a 2 byte signed integer in `[-32768, 32767]` that corresponds to a commanded angular rate in `[-60, 60]` degrees/s
    # - hover throttle as a 2 byte unsigned integer in `[0, 65535]` that corresponds to a throttle percentage

    return {
        "timestamp" : result["Timestamp"],
        "bus" : result["Bus"],
        "ID" : result["ID (hex)"],
        "roll_axis" : radian_to_degree(dec_from_hex(result["B0"] + result["B1"])),
        "pitch_axis" : radian_to_degree(dec_from_hex(result["B2"] + result["B3"])),
        "yaw_axis" : radian_to_degree(dec_from_hex(result["B4"] + result["B5"])),
        "hover" : dec_from_hex(result["B6"] + result["B7"], signed=False)
    }


def get_id_ox7e4(result : dict):

    # - ID 0x7e4, which contains the following fields (in this order)

    # - propspin switch as a 1 byte unsigned integer in `[0, 255]` that corresponds to a bool
    # - pusher throttle as a 2 byte signed integer in `[-32768, 32767]` that corresponds to +/- percentage, w/ 0 being neutral
    # - some additional data that we can ignore

    return {
        "timestamp" : result["Timestamp"],
        "bus" : result["Bus"],
        "ID" : result["ID (hex)"],
        "propspin_switch" : "{0:08b}".format(int(result["B0"], 16)),
        "pusher" : dec_from_hex(result["B1"] + result["B2"]),
    }



def get_IMU_pitch_data(result : dict):

    # Additionally, we are interested in seeing data from our onboard inertial measurement unit (IMU):

    # - ID 0x1 contains the pitch angle (in radians) as a 4 byte float, followed by some data we can ignore
    # - ID 0x2 contains the pitch rate (in radians/s) as a 4 byte float, followed by some data we can ignore
    return {
        "timestamp" : result["Timestamp"],
        "bus" : result["Bus"],
        "ID" : result["ID (hex)"],
        "pitch_angle" : radian_to_degree(
            struct.unpack('!f',bytes.fromhex(result["B0"]+
                                             result["B1"]+
                                             result["B2"]+
                                             result["B3"]))[0]),
        "pitch_rate" : radian_to_degree(
            struct.unpack('!f',bytes.fromhex(result["B0"]+
                                             result["B1"]+
                                             result["B2"]+
                                             result["B3"]))[0]),}

def get_IMU_roll_data(result : dict):

    # Additionally, we are interested in seeing data from our onboard inertial measurement unit (IMU):

    # - ID 0x3 contains the roll angle (in radians) as a 4 byte float, followed by some data we can ignore
    # - ID 0x4 contains the roll rate (in radians/s) as a 4 byte float, followed by some data we can ignore

    return {
        "timestamp" : result["Timestamp"],
        "bus" : result["Bus"],
        "ID" : result["ID (hex)"],
        "roll_angle" :radian_to_degree(
            struct.unpack('!f',bytes.fromhex(result["B0"]+
                                             result["B1"]+
                                             result["B2"]+
                                             result["B3"]))[0]),
        "roll_rate" : radian_to_degree(
            struct.unpack('!f',bytes.fromhex(result["B0"]+
                                             result["B1"]+
                                             result["B2"]+
                                             result["B3"]))[0]),}

def get_IMU_yaw_data(result : dict):

    # Additionally, we are interested in seeing data from our onboard inertial measurement unit (IMU):

    # - ID 0x5 contains the yaw angle (in radians) as a 4 byte float, followed by some data we can ignore
    # - ID 0x6 contains the yaw rate (in radians/s) as a 4 byte float, followed by some data we can ignore

    return {
        "timestamp" : result["Timestamp"],
        "bus" : result["Bus"],
        "ID" : result["ID (hex)"],
        "yaw_angle" : radian_to_degree(
            struct.unpack('!f',bytes.fromhex(result["B0"]+
                                             result["B1"]+
                                             result["B2"]+
                                             result["B3"]))[0]),
        "yaw_rate" : radian_to_degree(
            struct.unpack('!f',bytes.fromhex(result["B0"]+
                                             result["B1"]+
                                             result["B2"]+
                                             result["B3"]))[0]),
    }