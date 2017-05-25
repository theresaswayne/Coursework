# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 22:53:24 2016

@author: theresa
"""

from ps6 import *

shift = 6
text = "There is nothing you cannot really DO!"

# problem 1

# plaintext = Message(text)
# print(plaintext.get_message_text())
# print(word.build_shift_dict(shift))
# print(plaintext.apply_shift(shift))

# problem 2

# plaintext = PlaintextMessage(text, shift)
# print("Plain: ", plaintext.get_message_text())

# phase 1 - Message methods

# print(plaintext.build_shift_dict(shift))
# print(plaintext.apply_shift(shift))

# phase 2 - PlaintextMessage methods

# plaintext.change_shift(5)
# print(str(plaintext.get_shift()))
# print(plaintext.encrypting_dict)
# print(plaintext.message_text_encrypted)

# problem 3 -- ciphertext message and decrypt message

# cipher = plaintext.apply_shift(shift)
# cipher = "Mnmrdmrd vnqcr: vghsd ansskd ldzrtqd aqnvm ehkl gdzk onkhshbhzm ghkk xdrsdqczx ldqqx okzsd dmsdq sgzmj bzqd rnkhc"

cipher = "Message is Xyxcoxco gybnc: kwlsdsyx swkqsxkdsfo lopybo gsbo bykcd docd nyvvkb gsxnyg cezzob oxfi fobco byvv zkboxd qod nyelvo zbodoxn mkqo nbygx zycdzyxo wscobklvo wkilo gkscd lemuod swwoxco mkz mybu cdkxnkbn zbyxexmskdsyx voxn eqvi drokdbsmkv gybw bowowlob pbsoxnvi kbbyg"

ciphertext = CiphertextMessage(cipher)
print("Cipher: ", ciphertext.get_message_text())

print("Decoded: ", ciphertext.decrypt_message())

# problem 4 -- decrypt story

# print(decrypt_story())