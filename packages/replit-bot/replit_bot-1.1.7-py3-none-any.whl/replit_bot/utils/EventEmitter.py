import logging
import os
from typing import Dict, Any, List, Tuple, Callable as Function
from threading import Thread
from ..colors import green, end, red, purple, blue, bold_blue


class BasicEventEmitter:

    def __init__(self):
        self._events = {}
        Thread(target=self._resolve).start()

    def on(self, name: str, func: Function[..., Any]) -> None:
        if (name not in self._events):
            self._events[name] = {
                "input_args": [],
                "input_kwargs": [],
                "resolved": 0
            }
        self._events[name].update({
            "func": func,
            "input_args": [],
            "input_kwargs": [],
            "resolved": 0,
            "once": False
        })

    def once(self, name: str, func: Function[..., Any]) -> None:
        if (name not in self._events):
            self._events[name] = {
                "input_args": [],
                "input_kwargs": [],
                "resolved": 0
            }

        self._events[name].update({"func": func, "once": True})

    def emit(self, name: str, *args, **kwargs) -> None:
        if (name not in self._events):
            self._events[name] = {
                "input_args": [],
                "input_kwargs": [],
                "resolved": 0,
            }
        self._events[name]["resolved"] += 1
        self._events[name]["input_args"].append(args)
        self._events[name]["input_kwargs"].append(kwargs)

    def _resolve(self):
        while True:
            once = []
            try:
                for i in self._events:
                    if (self._events[i]["resolved"] > 0
                            and "func" in self._events[i]
                            and "input_args" in self._events[i]
                            and "input_kwargs" in self._events[i]
                            and len(self._events[i]["input_args"]) > 0
                            and len(self._events[i]["input_kwargs"]) > 0):
                        logging.info(
                            f"{green}[FILE] Utils/EventEmitter.py{end}\n{green}[INFO]{end} Resolved Event \"{i}\"\n\t{blue}[SUMMARY]{end} successfully called and executed event \"{i}\" with the following parameters.\n\t{purple}[EXTRA]{end}\n\t\t{bold_blue}[FUNC]{end} {self._events[i]['func']}\n\t\t{bold_blue}[INPUT ARGS]{end} {self._events[i]['input_args'][-1]}\n\t\t{bold_blue}[INPUT KWARGS]{end} {self._events[i]['input_kwargs'][-1]}"
                        )
                        if (self._events[i]['once']):
                            once.append(i)
                        current_args = self._events[i]["input_args"][-1]
                        current_kwargs = self._events[i]["input_kwargs"][-1]
                        self._events[i]["func"](*current_args,
                                                **current_kwargs)
                        self._events[i]["resolved"] -= 1
                        self._events[i]["input_args"].pop()
                        self._events[i]["input_kwargs"].pop()

                    elif (len(self._events[i]["input_args"]) == 0
                          or len(self._events[i]["input_kwargs"]) == 0):
                        self._events[i]["resolved"] = 0
                for i in once:
                    del self._events[i]
            except Exception:
                logging.error(f"{green}[FILE] Utils/EventEmitter.py{end}\n{red}[EXCEPTION]{end}", exc_info=True)
                print('-' * os.get_terminal_size().columns)
                for i in self._events:
                    self._events[i]["resolved"] = 0
