import numpy as np


_n: int
_q50: np.ndarray
_t: np.ndarray


def _quality_matrix(quality: int) -> np.ndarray:
    q = _q50 if quality == 50 else (_q50 * (100 - quality) / 50 if quality > 50 else _q50 * 50 / quality)
    q = np.clip(np.round(q), 1, 255).astype(int)
    return q


def _to_zigzag(matrix: np.ndarray) -> list:
    zigzag_list = []
    for i in range(2 * _n - 1):
        if i % 2 == 0:
            for j in range(max(0, i - _n + 1), min(i, _n - 1) + 1):
                zigzag_list.append(matrix[i - j, j])
        else:
            for j in range(max(0, i - _n + 1), min(i, _n - 1) + 1):
                zigzag_list.append(matrix[j, i - j])
    return zigzag_list


def _from_zigzag(zigzag_list: list) -> np.ndarray:
    matrix = np.zeros((_n, _n))
    count = 0
    for i in range(2 * _n - 1):
        if i % 2 == 0:
            for j in range(max(0, i - _n + 1), min(i, _n - 1) + 1):
                matrix[i - j, j] = zigzag_list[count]
                count += 1
        else:
            for j in range(max(0, i - _n + 1), min(i, _n - 1) + 1):
                matrix[j, i - j] = zigzag_list[count]
                count += 1
    return matrix


def _run_length_encoding(data: list) -> list:
    encoded_data = []
    current_num = data[0]
    count = 1

    for num in data[1:]:
        if num == current_num:
            count += 1
        else:
            if count == 1:
                encoded_data.append((current_num, ))
            else:
                encoded_data.append((current_num, count))
            current_num = num
            count = 1

    encoded_data.append((current_num, count))
    return encoded_data


def _run_length_decoding(encoded_data):
    data = []
    for elem in encoded_data:
        if len(elem) == 1:
            data.append(elem[0])
        else:
            num, count = elem
            data.extend([num] * count)
    return data


def compress(image: np.ndarray, quality: int = 50) -> list:
    if image.shape[0] % _n != 0 or image.shape[1] % _n != 0:
        raise ValueError(f"image.shape[0] % {_n} != 0 or image.shape[1] % {_n} != 0")
    if not (1 <= quality <= 100):
        raise ValueError("not (1 <= quality <= 100)")

    q = _quality_matrix(quality)

    encoded_image = [quality]
    for block_i in range(0, image.shape[0], _n):
        encoded_row = []
        for block_j in range(0, image.shape[1], _n):
            block = image[block_i:block_i + _n, block_j:block_j + _n].astype(int)
            m = block - 128
            d = np.matmul(np.matmul(_t, m), np.transpose(_t))
            c = np.round(d / q).astype(int)
            encoded_block = _run_length_encoding(_to_zigzag(c))

            encoded_row.append(encoded_block)
        encoded_image.append(encoded_row)

    return encoded_image


def decompress(encoded_image: list) -> np.ndarray:
    quality, *encoded_rows = encoded_image
    q = _quality_matrix(quality)
    image = np.zeros((len(encoded_rows) * _n, ) * 2, dtype=np.uint8)
    for encoded_row, block_i in zip(encoded_rows, range(0, image.shape[0], _n)):
        for encoded_block, block_j in zip(encoded_row, range(0, image.shape[1], _n)):
            c = _from_zigzag(_run_length_decoding(encoded_block))
            r = q * c
            n = np.clip(np.round(np.matmul(np.matmul(np.transpose(_t), r), _t)) + 128, 0, 255)
            image[block_i:block_i + _n, block_j:block_j + _n] = n
    return image


def setup():
    global _n, _q50, _t

    _n = 8

    _q50 = np.array([[16, 11, 10, 16, 24, 40, 51, 61],
                     [12, 12, 14, 19, 26, 58, 60, 55],
                     [14, 13, 16, 24, 40, 57, 69, 56],
                     [14, 17, 22, 29, 51, 87, 80, 62],
                     [18, 22, 37, 56, 68, 109, 103, 77],
                     [24, 35, 55, 64, 81, 104, 113, 92],
                     [49, 64, 78, 87, 103, 121, 120, 101],
                     [72, 92, 95, 98, 112, 100, 103, 99]])

    a = 1 / np.sqrt(_n)
    b = np.sqrt(2 / _n)
    _t = np.array(
        [[a if i == 0 else b * np.cos((2*j+1) * i * np.pi / (2*_n)) for j in range(_n)]
         for i in range(_n)])


setup()
