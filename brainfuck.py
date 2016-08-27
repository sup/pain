#!/usr/bin/python

import sys

# ================
#  Main Eval Loop
# ================
def evaluate(code):
    # Build a program from the source code
    program = list(code)

    # Initialize memory, byte pointer, and program counter
    memory = [0 for byte in range(30000)]
    byte_ptr = 0
    pc = 0

    # Evaluate the program
    while pc < len(program):
        # Grab the instruction at program counter
        instruction = program[pc]

        # Program Memory Instructions
        if instruction == ">": byte_ptr += 1
        elif instruction == "<": byte_ptr = max(0, byte_ptr - 1)

        # Data Memory Instructions
        elif instruction == "+": memory[byte_ptr] = (memory[byte_ptr] + 1) % 256
        elif instruction == "-": memory[byte_ptr] = (memory[byte_ptr] - 1) % 256
        elif instruction == ".": sys.stdout.write(chr(memory[byte_ptr]))
        elif instruction == ",": memory[byte_ptr] = ord(raw_input())

        # Control Flow Instructions
        elif instruction == "[": pc = jump_forward(pc, program, memory[byte_ptr])
        elif instruction == "]": pc = jump_backward(pc, program, memory[byte_ptr])

        # Invalid Expression
        else: raise Exception("Invalid Expression")

        # Increment program counter
        pc += 1

# ===============
#    Helpers
# ===============
def jump_forward(pc, program, byte):
    if byte == 0:
        while program[pc] != "]":
            pc += 1
    return pc

def jump_backward(pc, program, byte):
    if byte != 0:
        while program[pc] != "[":
            pc -= 1
    return pc

# Hello world!
evaluate("--[>--->->->++>-<<<<<-------]>--.>---------.>--..+++.>----.>+++++++++.<<.+++.------.<-.>>+.")
