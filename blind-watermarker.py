from blind_watermark import WaterMark
import os


def embed():
    try: 
        pic = input("path to picture that you want to embed in: ")
        if os.path.exists(pic):
            if pic.lower().endswith('.png'):
                bwm1 = WaterMark(password_wm=1, password_img=1)
                bwm1.read_img(pic)
                wm = input("Insert watermark string: ")
                bwm1.read_wm(wm, mode='str')
                bwm1.embed("embedded.png")
                len_wm = len(bwm1.wm_bit)
                try:
                    with open('wmlen.txt', 'x') as f:
                        f.write(str(len_wm))
                except FileExistsError:
                    with open ('wmlen.txt', 'w') as w:
                        w.write(str(len_wm))
                print('Put down the length of wm_bit {len_wm}'.format(len_wm=len_wm))
                print("Embed done. wm_len saved as wmlen.txt.")
            else:
                print(f'The file "{file_path}" exists, but it is not a .png file. Quitting...')
                exit()
        else:
            print("[!] File does not exist! Quitting...")
            exit()
    except KeyboardInterrupt:
        print()
    

def extract():
    try:
        pic = input("path to picture that you want to extract: ")
        if os.path.exists(pic):
            if pic.lower().endswith('.png'):
                bwm1 = WaterMark(password_img=1, password_wm=1)
                wm_len = int(input("len_wm of the original pic: "))
                wm_extract = bwm1.extract(pic, wm_shape=wm_len, mode='str')
                try:
                    with open('extracted.txt', 'x') as f:
                        f.write(wm_extract)
                except FileExistsError:
                    with open ('extracted.txt', 'w') as w:
                        w.write(wm_extract)
                print("Extraction done. Saved as extracted.txt.")
            else:
                print(f'The file "{file_path}" exists, but it is not a .png file. Quitting...')
                exit()
        else:
            print("[!] File does not exist! Quitting...")
            exit()
    except KeyboardInterrupt:
        print()


print("""
BLIND WATER-MARK TOOLKIT
BY orangetheorange
https://github.com/orangetheorange/blind-water-marker-toolkit
    
[*] please install the required packages using: pip install blind-watermark
[*] Only availeble for .png files

_______________________________________________________________________________
    
    [1] embed
    [2] extract
    [99] exit
    
_______________________________________________________________________________
""")


while True:
    try:
        mode = input("Menu: ")
        if mode == "1":
            embed()
        elif mode == "2": 
            extract()
        elif mode == "99": 
            exit()
        else:
            print("[!] Type a valid mode!")
    except KeyboardInterrupt:
        exit()
