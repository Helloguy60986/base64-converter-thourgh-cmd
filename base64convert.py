#!/usr/bin/env python3
import base64
import argparse

def string_to_base64(text):
    return base64.b64encode(text.encode('utf-8')).decode('utf-8')

def main():
    parser = argparse.ArgumentParser(description="Convert a string to Base64")
    parser.add_argument("text", type=str)
    args = parser.parse_args()
    print(string_to_base64(args.text))

if __name__ == "__main__":
    main()
