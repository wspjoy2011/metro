# Transposition Cipher Decryption
# https://www.nostarch.com/crackingcodes (BSD Licensed)

import math, pyperclip


def decryptMessage(key, message):
    numOfColumns = int(math.ceil(len(message) / key))
    numOfRows = key
    numOfShadedBoxes = numOfColumns * numOfRows - len(message)
    plaintext = [''] * numOfColumns

    column = 0
    row = 0

    for symbol in message:
        plaintext[column] += symbol
        column += 1
        if (column == numOfColumns) or (column == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            column = 0
            row += 1

    return ''.join(plaintext)


def main():
    plaintext = decryptMessage(myKey, myMessage)
    pyperclip.copy(plaintext)
    return plaintext


if __name__ == '__main__':
    myMessage = '''Ainlm75gti rrsn-uleo  dtn b   tpmuntab 2litk l ipty.nii  tcyAsrhueggeceN)icenweecuet  nsaaea sheetru-sero siroosaarriHtc slnra eg e.sNs  vwha,wr rlp,cehlr gdr a afrto (1ea n nkBl o areuetoeim iri aeo18msm c  aygstl  dchrdearsdrp lf01b aahfob eeh neeoei dce esrA,  5eatnionbmn eEon g tt hsodtod LD rnhder aeec ntgwnfhooiuf  gaCoe-  e f CgcroAgeihiim unltacr ovc 1Emwlhhehamnisnasr btetesoaKuee28naryea'alpan etesie .,n mm'''
    myKey = 13
    print(main())