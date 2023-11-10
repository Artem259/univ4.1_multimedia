import numpy as np

from compression._encoding import encode, decode


__n: int
__q50: np.ndarray
__t: np.ndarray


def __quality_matrix(quality: int) -> np.ndarray:
    q = __q50 if quality == 50 else (__q50 * (100 - quality) / 50 if quality > 50 else __q50 * 50 / quality)
    q = np.clip(np.round(q), 1, 255).astype(int)
    return q


def compress(image: np.ndarray, quality: int = 50) -> list:
    if image.shape[0] % __n != 0 or image.shape[1] % __n != 0:
        raise ValueError(f"image.shape[0] % {__n} != 0 or image.shape[1] % {__n} != 0")
    if not (1 <= quality <= 100):
        raise ValueError("not (1 <= quality <= 100)")

    q = __quality_matrix(quality)

    encoded_image = [quality]
    for block_i in range(0, image.shape[0], __n):
        encoded_row = []
        for block_j in range(0, image.shape[1], __n):
            block = image[block_i:block_i + __n, block_j:block_j + __n].astype(int)
            m = block - 128
            d = np.matmul(np.matmul(__t, m), np.transpose(__t))
            c = np.round(d / q).astype(int)
            encoded_block = encode(c, __n)

            encoded_row.append(encoded_block)
        encoded_image.append(encoded_row)

    return encoded_image


def decompress(encoded_image: list) -> np.ndarray:
    quality, *encoded_image = encoded_image
    q = __quality_matrix(quality)
    image = np.zeros((len(encoded_image) * __n, len(encoded_image[0]) * __n), dtype=np.uint8)
    for encoded_row, block_i in zip(encoded_image, range(0, image.shape[0], __n)):
        for encoded_block, block_j in zip(encoded_row, range(0, image.shape[1], __n)):
            c = decode(encoded_block, __n)
            r = q * c
            n = np.clip(np.round(np.matmul(np.matmul(np.transpose(__t), r), __t)) + 128, 0, 255)
            image[block_i:block_i + __n, block_j:block_j + __n] = n
    return image


def __setup():
    global __n, __q50, __t

    __n = 8
    __q50 = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                      [12, 12, 14, 19, 26, 58, 60, 55],
                      [14, 13, 16, 24, 40, 57, 69, 56],
                      [14, 17, 22, 29, 51, 87, 80, 62],
                      [18, 22, 37, 56, 68, 109, 103, 77],
                      [24, 35, 55, 64, 81, 104, 113, 92],
                      [49, 64, 78, 87, 103, 121, 120, 101],
                      [72, 92, 95, 98, 112, 100, 103, 99]])

    a = 1 / np.sqrt(__n)
    b = np.sqrt(2 / __n)
    __t = np.array(
        [[a if i == 0 else b * np.cos((2*j+1) * i * np.pi / (2 * __n)) for j in range(__n)]
         for i in range(__n)])


__setup()
