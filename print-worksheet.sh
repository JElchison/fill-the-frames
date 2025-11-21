#!/bin/bash

python3 ./fill-the-frames.py | paps --font="Monospace 10" | lp -d "Home" -o sides=two-sided-long-edge