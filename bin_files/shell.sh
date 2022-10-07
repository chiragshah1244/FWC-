#!/bin/bash
sudo python3 /Users/chiragshah/TinyFPGA-Programmer-Application/tinyfpga-programmer-gui.py --port /dev/cu.usbmodem1101 --appfpga top.bin --m4app $1 --mode m4-fpga --reset

