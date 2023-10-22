#!/usr/bin/python3
"""This module will be working on db storage"""


def close(self):
    """call Remove function on the private session attribute"""
    self.__session.remove()
