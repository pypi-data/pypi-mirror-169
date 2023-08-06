"""
Main entrypoint for very_simple_wordle_server.
"""

import argparse
import json
import socketserver
import threading

import very_simple_wordle_server


class WordleHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request[0]
        msg = str(data, "UTF-8")
        if msg[0] == "1":
            self.handle_guess()
        elif msg[0] == "0":
            self.handle_check()
        else:
            self.handle_bad_format()

    def handle_guess(self):
        data = self.request[0]
        socket = self.request[1]
        guess = str(data[1:6], "UTF-8").strip()
        clue = []

        for item in zip(guess, self.server.wordle_word):
            if item[0] == item[1]:
                clue.append((item[0], "green"))
            elif item[0] in self.server.wordle_word:
                clue.append((item[0], "yellow"))
            else:
                clue.append((item[0], "red"))

        socket.sendto(bytes(json.dumps(clue), "UTF-8"), self.client_address)
        self.server.set_last_clue(json.dumps(clue))

    def handle_check(self):
        response = bytes(json.dumps({}), "UTF-8")
        clue = self.server.get_last_clue()
        if clue:
            response = bytes(clue, "UTF-8")
        socket = self.request[1]
        socket.sendto(response, self.client_address)

    def handle_bad_format(self):
        response = bytes("Bad format!", "UTF-8")
        socket = self.request[1]
        socket.sendto(response, self.client_address)


class WordleServer(socketserver.UDPServer):

    def __init__(self, wordle_word, *args, **kwargs):
        self.wordle_word = wordle_word
        self.last_clue = None
        self.clue_lock = threading.Lock()
        super().__init__(*args, **kwargs)

    def set_last_clue(self, clue):
        with self.clue_lock:
            self.last_clue = clue

    def get_last_clue(self):
        with self.clue_lock:
            clue = self.last_clue
        return clue


def main():
    parser = argparse.ArgumentParser(
                        prog="Very Simple Wordle Server",
                        description="A very simple UDP-based Wordle server")

    parser.add_argument("-V",
                        "--version",
                        action="store_true",
                        help="print package version")

    parser.add_argument("-a",
                        "--address",
                        default="localhost",
                        help="address to listen on")

    parser.add_argument("-p",
                        "--port",
                        default=13337,
                        help="port to listen on")

    parser.add_argument("-w",
                        "--wordle-word",
                        default="zebra",
                        help="the secret word to guess")

    args = parser.parse_args()

    if args.version:
        print("very_simple_wordle_server " +
              very_simple_wordle_server.__version__)
    else:
        with WordleServer(args.wordle_word,
                          (args.address, args.port),
                          WordleHandler) as server:
            server.serve_forever()
