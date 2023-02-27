from pyzbar.pyzbar import decode, ZBarSymbol
from PIL import Image
import os

folder = './sample_file_folders/2000005044986390'

for basename in os.listdir(folder):
    
    print(f"Basename: {basename}")

    filepath = os.path.join(folder, basename)
    if os.path.isfile(filepath):
        
        print(f"Filepath: {filepath}")

        possible_qr = Image.open(filepath)
        decoded_list = decode(possible_qr)

        print(f"Decoded list: {decoded_list}")


    
    


