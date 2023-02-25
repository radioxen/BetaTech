from helpers.read_data import *


def check_criteria(result : dict):
    if result["ID (hex)"] == "7E3":
        return get_id_ox7e3(result)
    elif result["ID (hex)"] == "7E4":
        return get_id_ox7e4(result)
    if result["ID (hex)"] in ("1","2"):
        return get_IMU_pitch_data(result)
    if result["ID (hex)"] in ("1","2"):
        return get_id_ox7e3(result)
    if result["ID (hex)"] in ("3","4"):
        return get_id_ox7e3(result)
    if result["ID (hex)"] in ("5","6"):
        return get_id_ox7e3(result)

