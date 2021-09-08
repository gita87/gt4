
from art import *

tprint("PESAN - SANDI\n CONVERTER", "small")

abjad = \
    [
        'a', 'b', 'c','d', 'e',
        'f', 'g', 'h','i', 'j',
        'k', 'l', 'm','n', 'o',
        'p', 'q', 'r','s', 't',
        'u', 'v', 'w','x', 'y',
        'z', 'a', 'b','c', 'd',
        'e', 'f', 'g','h', 'i',
        'j', 'k', 'l','m', 'n',
        'o', 'p', 'q','r', 's',
        't', 'u', 'v', 'w','x',
        'y', 'z'
         ]
def encrypt(txt, sft) :
    sandi = ''
    for abjad_kata in txt :
        if abjad_kata in abjad :
            posisi = abjad.index(abjad_kata)
            posisi_baru = posisi + (skip % 25)
            huruf_sandi = abjad[posisi_baru]
            sandi += huruf_sandi
        else:
            sandi += abjad_kata
    print(f"Pesan anda berubah dari :\n>>> {kata}\nmenjadi :\n>>> {sandi}")

def decrypt (txt, sft) :
    pesan = ''
    for abjad_kata in txt :
        if abjad_kata in abjad :
            posisi = abjad.index(abjad_kata)
            if skip >= 25:
                posisi_baru = posisi - (skip % 25)
            elif skip < 25:
                posisi_baru = posisi - skip + 26
            sandi = abjad[posisi_baru]
            pesan += sandi
        else:
            pesan += abjad_kata
    print(f"Sandi anda adalah :\n>>> {kata}\ntelah diubah menjadi :\n>>> : {pesan}")

def penyandian(a, b, c) :
    a = pilih_mode
    b = kata
    c = skip
    if pilih_mode == 'encode':
        encrypt(txt=kata, sft=skip)
    elif pilih_mode == 'decode':
        decrypt(txt=kata, sft=skip)

lanjut = True
while lanjut :
    pilih_mode = input("ketik 'encode' untuk encrypt, ketik 'decode' untuk decrypt :\n")
    kata = input("Ketik pesan anda :\n").lower()
    skip = int(input("ketik angka untuk merubah pesan anda menjadi sandi rahasia :\n"))

    penyandian(a=pilih_mode, b=kata, c=skip)
    Continue = input("Lanjut nggak nih?\nketik : (kuy) untuk lanjut\nketik :(gak) untuk berhenti \n")
    if Continue == 'gak':
        lanjut = False
        print("Ya udah, hati hati jangan sampai ketahuan")