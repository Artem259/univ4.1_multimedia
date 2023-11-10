import numpy as np


def to_zigzag(matrix: np.ndarray, n: int) -> list:
    zigzag_list = []
    for i in range(2 * n - 1):
        if i % 2 == 0:
            for j in range(max(0, i - n + 1), min(i, n - 1) + 1):
                zigzag_list.append(matrix[i - j, j])
        else:
            for j in range(max(0, i - n + 1), min(i, n - 1) + 1):
                zigzag_list.append(matrix[j, i - j])
    return zigzag_list


def from_zigzag(zigzag_list: list, n: int) -> np.ndarray:
    matrix = np.zeros((n, n))
    count = 0
    for i in range(2 * n - 1):
        if i % 2 == 0:
            for j in range(max(0, i - n + 1), min(i, n - 1) + 1):
                matrix[i - j, j] = zigzag_list[count]
                count += 1
        else:
            for j in range(max(0, i - n + 1), min(i, n - 1) + 1):
                matrix[j, i - j] = zigzag_list[count]
                count += 1
    return matrix


def run_length_encoding(data: list) -> list:
    encoded_data = []
    current_num = data[0]
    count = 1

    for num in data[1:]:
        if num == current_num:
            count += 1
        else:
            if count == 1:
                encoded_data.append(current_num)
            else:
                encoded_data.append((current_num, count))
            current_num = num
            count = 1

    encoded_data.append((current_num, count))
    return encoded_data


def run_length_decoding(encoded_data: list) -> list:
    data = []
    for elem in encoded_data:
        if isinstance(elem, tuple):
            num, count = elem
            data.extend([num] * count)
        else:
            data.append(elem)
    return data


def encode(data: np.ndarray, n: int):
    return run_length_encoding(to_zigzag(data, n))


def decode(encoded_data: list, n: int):
    return from_zigzag(run_length_decoding(encoded_data), n)
