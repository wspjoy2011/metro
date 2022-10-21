# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math, pyperclip


def main():
    myMessage = '''Ainlm75gti rrsn-uleo  dtn b   tpmuntab 2litk l ipty.nii  tcyAsrhueggeceN)icenweecuet  nsaaea sheetru-sero siroosaarriHtc slnra eg e.sNs  vwha,wr rlp,cehlr gdr a afrto (1ea n nkBl o areuetoeim iri aeo18msm c  aygstl  dchrdearsdrp lf01b aahfob eeh neeoei dce esrA,  5eatnionbmn eEon g tt hsodtod LD rnhder aeec ntgwnfhooiuf  gaCoe-  e f CgcroAgeihiim unltacr ovc 1Emwlhhehamnisnasr btetesoaKuee28naryea'alpan etesie .,n mm'''
    myKey = 13

    plaintext = decryptMessage(myKey, myMessage)

    # Print with a | ("pipe" character) after it in case
    # there are spaces at the end of the decrypted message.
    print(plaintext + '|')

    pyperclip.copy(plaintext)


def decryptMessage(key, message):
    # The transposition decrypt function will simulate the "columns" and
    # "rows" of the grid that the plaintext is written on by using a list
    # of strings. First, we need to calculate a few values.

    # The number of "columns" in our transposition grid:
    numOfColumns = int(math.ceil(len(message) / float(key)))
    # The number of "rows" in our grid will need:
    numOfRows = key
    # The number of "shaded boxes" in the last "column" of the grid:
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(message)

    # Each string in plaintext represents a column in the grid.
    plaintext = [''] * numOfColumns

    # The column and row variables point to where in the grid the next
    # character in the encrypted message will go.
    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1 # Point to next column.

        # If there are no more columns OR we're at a shaded box, go back to
        # the first column and the next row:
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)


# If transpositionDecrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == '__main__':
    main()