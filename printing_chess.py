#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 10:20:58 2023

@author: Fscott
"""

def print_board(board):
    print("    ", end= "")
    for i in range(65,73):
        print(chr(i), end = " ")
    print()
    print("  _ _ _ _ _ _ _ _ _")
    for i in range(len(board)):
        print(i+1, "|", end = " ")
        for j in range(len(board[i])):
            print(board[i][j], end = " ")
        print()