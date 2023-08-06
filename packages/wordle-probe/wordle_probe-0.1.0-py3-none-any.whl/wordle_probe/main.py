"""
Main entrypoint for wordle_probe.
"""

import argparse
import socket

from qwilprobe.service.api import (
    DATATYPE_STRING,
    KEY_COLINFO_NAME,
    KEY_COLINFO_TYPE,
    RPC_GET_PROBE_DATA,
    RPC_GET_PROBE_IS_READY,
    qwilprobe_register_handler,
    qwilprobe_set_probe_info,
    qwilprobe_start,
)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def _data_handler():
    global sock
    sock.sendto(bytes("0", "utf-8"), ("localhost", 13337))
    received = str(sock.recv(1024), "utf-8")

    return {"wordle clue": f"{received}"}


def _is_ready_handler():
    return True


def _start_probe():
    qwilprobe_set_probe_info(
        "wordle-probe",
        [
            {
                KEY_COLINFO_NAME: "wordle clue",
                KEY_COLINFO_TYPE: DATATYPE_STRING,
            }
        ],
    )
    qwilprobe_register_handler(RPC_GET_PROBE_DATA, _data_handler)
    qwilprobe_register_handler(RPC_GET_PROBE_IS_READY, _is_ready_handler)
    qwilprobe_start()


def main():
    parser = argparse.ArgumentParser(
                        prog="Wordle Probe",
                        description="An example probe service for a wordle server")

    parser.add_argument("-V",
                        "--version",
                        action="store_true",
                        help="print package version")

    args = parser.parse_args()

    if args.version:
        print("wordle_probe " +
              wordle_probe.__version__)
    else:
        _start_probe()
