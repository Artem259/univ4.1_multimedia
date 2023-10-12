import argparse
import os
import shutil
import cv2
import numpy as np

import dct
import wav
import psnr


input_path = "data/lena512.png"
output_path = "data/out/"
dct_quality = 50
wav_compression_ratio = 1


def print_list_to_file(l, file):
    print('\n'.join([str(i) for i in l]), file=file)


def main():
    parser = argparse.ArgumentParser(description='Apply DCT or Wavelet Transform to an input image.')
    parser.add_argument('--dct', action='store_true', help='Apply Discrete Cosine Transform (DCT)')
    parser.add_argument('--wav', action='store_true', help='Apply Wavelet Transform')
    args = parser.parse_args()

    if os.path.exists(output_path):
        shutil.rmtree(output_path)
    os.makedirs(output_path)

    input_image = cv2.imread(input_path, 0)
    input_file = os.path.splitext(os.path.basename(input_path))[0]
    in_txt_file = output_path + input_file + '_int.txt'
    out_txt_file = output_path + input_file + '_out.txt'
    decompressed_image: np.ndarray
    if args.dct:
        compressed_image = dct.compress(input_image, dct_quality)
        with (open(in_txt_file, 'w') as in_file, open(out_txt_file, 'w') as out_file):
            print_list_to_file(input_image.tolist(), in_file)
            print_list_to_file(compressed_image, out_file)
        decompressed_image = dct.decompress(compressed_image)
        print(f"{input_path} --> DCT")
    elif args.wav:
        compressed_image = wav.compress(input_image, wav_compression_ratio)
        with (open(in_txt_file, 'w') as in_file, open(out_txt_file, 'w') as out_file):
            print_list_to_file(input_image.tolist(), in_file)
            print_list_to_file(compressed_image.tolist(), out_file)
        decompressed_image = wav.decompress(compressed_image)
        print(f"{input_path} --> Wavelet")
    else:
        print("Provide one of the flags: --dct or --wav")
        return

    print(f"PSNR-value: {psnr.psnr(input_image, decompressed_image)}")
    cv2.imshow("Input Image", input_image)
    cv2.imshow("Decompressed Image", decompressed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
