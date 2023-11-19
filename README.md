# UBloX-6_codes
These are some of the reverse-engineered serial command codes for the UBlox-6 GPS modules (e.g NEO-6M). 

## Background

UBlox provides the spec for these codes (https://content.u-blox.com/sites/default/files/products/documents/u-blox6_ReceiverDescrProtSpec_%28GPS.G6-SW-10018%29_Public.pdf), however, the CRC is difficult to generate, and most of the fields are unclear. 

This repository contains serial command codes captured from the official UBlox configuration software communicating with the GPS. Each text file has the command in the hexadecimal format. To send the command, simply send the hexadecimal bytes via serial to the GPS module. 

## What about the GPS poll codes?

The UBX protocol provides a way to poll the current status of the GPS to check that the GPS was configured correctly. This is a bit tricky, since according to the datasheet, the communication is mixed between string (ASCII) and hexadecimal binary formats. Since this is a two-way communication, it will require much more extensive reverse-engineering. However, I am planning to do it eventually. 
