# Low-power-approximate-multipliers
Verilog and Python Codes of two schemes of low power truncation based approximate multipliers

This repository consists of verilog and python codes of two schemes of 16,32 and 64 bit truncation based approximate multiplier. The file scheme_1_bits.py is the comparisoon between scheme 1 of 
4,8,16,32,64 and 128 bitsapproximate multipliers. Both the approximate multipliers are based on the fact that all the bits are not required for approximate multiplication and 
it consideres only the bits followed by the bit position of leading 1 from MSB of both the numbers into account. The total number of bits considered for multiplication in a number is
called latency parameter. Scheme 1 has a fixed value of latency parameter for all the numbers considered for multiplication. Scheme 2 has a variable value of latency parameter 
and it changes according to the two numbers which are to be multiplied. 

All the given verilog codes are synthesizable (the original module, not testbench) and have been synthesized on Cadence Virtuoso with slow_vdd_1.0 library (45nm) to find out the 
area, power and timing of the two schemes of approximate multipliers and it was found out that the scheme 2 multipliers fared better than scheme 1 with high latency parameter in
the terms of area and power. These type of truncation based multipliers are usually better than other approximate multipliers if numbers with a large magnitude are to be 
considered.

The error parameters, that is mean relative error and acceptance probability (1% relative error) were calculated using python codes.
