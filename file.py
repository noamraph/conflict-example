import os
import sys
import json
import pathlib
import urllib

def main():
    print("This file does nothing useful.")
    print(f"Python version: {sys.version.split()[0]}")
    print(f"Current working directory: {pathlib.Path.cwd()}")

if __name__ == "__main__":
    main()
