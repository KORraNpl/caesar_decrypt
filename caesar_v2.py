#!/usr/bin/env python2
# -*- coding: utf-8 -*-

base_text = """Cbo qd vzlhflh vrelh Sbwkrq,
Nwrub rgsrzlhgcl cqd qd zlhoh sbwdq.
Mdgdo cgurzr, cbo vcfchvolzlh,
Mxc suchvwdqh er urel vlh cebw fnolzlh.
Udc cmdzlo vlh mhjrprvf, fr sbwdqlh cdgdo wuxgqh
gclzqh, wurfkę odwzh ,wurfkh wuxgqh.
Mhśolv flhndz rwr rqr:
Vurghn qrfb, gr guczl sxndqlh vobvcbvc.
Nwrv zbubzd Flh ch vcsrqóz vorgnlhm flvcb.
Ph sbwdqlh cdjdgnrzh,
Fr rwzlhudvc mdnr slhuzvch?
Cjdgqlhvc?
Fcb rgsrzlhvc zlhuvchp?"""

alphabet = "abcdefghijklmnopqrstuvwxyz"
decoded_text = ""
shift = -3

def decode(letter, shift):
    if shift == 0:
        return letter
    isUpper = letter.isupper()
    origin_pos = alphabet.find(letter.lower())
    new_pos = origin_pos + shift

    return alphabet[new_pos].upper() if isUpper else alphabet[new_pos]


for letter in base_text:
    if letter.isalpha():
        decoded_text += decode(letter, shift)
    else:
        decoded_text += letter

print decoded_text
