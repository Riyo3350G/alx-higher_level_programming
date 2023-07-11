#!/usr/bin/python3
"""add_item module"""
import sys
from os import path


save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

lst = []
if path.isfile("add_item.json"):
    lst = load_from_json_file("add_item.json")
save_to_json_file(lst + sys.argv[1:], "add_item.json")
