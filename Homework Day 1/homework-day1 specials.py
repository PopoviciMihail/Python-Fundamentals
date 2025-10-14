"""
Exercise 1:
We are given an “S” string, representing a series of two dice rolls.

Each roll is represented in X-Y format, where X and Y are numbers from the 1..6 range. The rolls are separated by a comma.

Some examples of a valid “S” are:
"6-3"
"1-2,1-2"
"1-1,3-5,5-5,2-2,2-4"

In dice games, rolling two dice with the same value is called a double.

The possible doubles are: 1-1 ⚀⚀, 2-2 ⚁⚁, 3-3 ⚂⚂, 4-4 ⚃⚃, 5-5 ⚄⚄ and 6-6 ⚅⚅.

Devise a function that given an S string, returns the length of the longest streak of doubles within S.

Examples:
doubles("6-3") // should return 0
doubles("1-2,2-2") // should return 1
doubles("1-1,5-5,2-3,3-5,2-4") // should return 2

Test cases:
doubles("3-5,5-3,4-3,6-5") // 0
doubles("4-4,6-6,3-4,6-6") // 2
doubles("6-4,2-2,3-3,6-6,3-4,6-6,5-5") // 3
doubles("3-3,3-3,4-4,6-4,6-6,2-2,1-1,6-6") // 4
doubles("1-2,3-3,2-2,4-5,3-4,5-5,4-4,5-5,6-5,4-4,1-1") // 3
doubles("1-1,2-2,6-6,6-6,3-3") // 5


Example 2:
A precedence rule is given as "P>E", which means that letter "P" is followed directly by the letter "E".
Write a function, given an array of precedence rules, that finds the word represented by the given rules.

Note: Each represented word contains a set of unique characters, i.e. the word does not contain duplicate letters.

Examples:
findWord(["P>E","E>R","R>U"]) // PERU
findWord(["I>N","A>I","P>A","S>P"]) // SPAIN


findWord(["U>N", "G>A", "R>Y", "H>U", "N>G", "A>R"]) // HUNGARY
findWord(["I>F", "W>I", "S>W", "F>T"]) // SWIFT
findWord(["R>T", "A>L", "P>O", "O>R", "G>A", "T>U", "U>G"]) // PORTUGAL
findWord(["W>I", "R>L", "T>Z", "Z>E", "S>W", "E>R", "L>A", "A>N", "N>D", "I>T"]) // SWITZERLAND
"""
