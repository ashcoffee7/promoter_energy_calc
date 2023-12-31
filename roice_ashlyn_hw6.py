# -*- coding: utf-8 -*-
"""roice_ashlyn_hw6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Hvk1h8glgNR8PtwpMndYzmVkdbNYV0U8

**Question 2B**
"""

'''
Given a link to an uploaded .txt file of an energy matrix, converts the file into an array usable in energy calculations.
- parameters: (str) a .txt file consisting of an energy matrix
- returns: an array of the converted energy matrix
'''

def create_arr(matrix):
  # initializes matrix to return
  matrix_arr = []
  # opens file in read mode
  with open(matrix, 'r') as f:
    # iterates through every row
    for row in f:
      # only continues if first character of row is an integer or negative sign
      if(row[0].isnumeric() or row[0] == '-'):
        # strips the row of any extra punctuation or \n, and then splits it by spaces to get each float
        new_row = row.strip().split(' ')
        # appends the new_row to the matrix_arr
        matrix_arr.append(new_row)
  # returns the created matrix
  return matrix_arr

'''
Given 1 sequence and a file for the matrix, calculates the binding energy of a given promoter.
- parameters: (str) seq1, (arr) energy matrix
- returns: the binding energy of a given promoter
'''
def calc_eng_one_seq(seq1, matrix):
  # defines a dict with the placement of energy values for each base within each row of the energy matrix. for future reference
  base_dict = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
  # creates the energy matrix array
  arrMatrix = create_arr(matrix)
  # gets the list of keys from diffIdxs to know which indexes to search for base pairs
  # initializes variable for energy
  sum = 0
  # loops through every key in the differences dictionary
  for i in range(len(seq1)):
    # gets curr base
    currB = seq1[i]
    # gets the index of current base from bases dictionary
    bIdx = base_dict.get(currB)
    # gets the needed row of the energy matrix based on the key
    currArr = arrMatrix[i]
    # gets the energy value for the first base
    bVal = float(currArr[bIdx])
    # adds this to the sum
    sum += bVal
  # returns the final energy value
  return sum