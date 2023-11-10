import numpy as np

from compression._encoding import encode, decode


__n: int
__eps: float
__h: np.ndarray
__h_t: np.ndarray


def __h1(size: int) -> np.ndarray:
    h = np.zeros((size, size))
    for i in range(0, size, 2):
        h[i, i // 2] = 0.5
        h[i + 1, i // 2] = 0.5
    for i in range(size-1, -1, -2):
        h[i,  size - (size - i + 1) // 2] = -0.5
        h[i - 1,  size - (size - i + 1) // 2] = 0.5
    return h


def __h2(size: int) -> np.ndarray:
    h = np.zeros((size, size))
    h[:size // 2, :size // 2] = __h1(size // 2)
    h[size // 2:, size // 2:] = np.eye(size // 2)
    return h


def __h3(size: int) -> np.ndarray:
    h = np.eye(size)
    h[0, 0] = h[0, 1] = h[1, 0] = 0.5
    h[1, 1] = -0.5
    return h


def __comp_h(size: int) -> np.ndarray:
    h1, h2, h3 = __h1(size), __h2(size), __h3(size)
    return np.matmul(np.matmul(h1, h2), h3)


def compress(image: np.ndarray, eps: float) -> list:
    if image.shape[0] % __n != 0 or image.shape[1] % __n != 0:
        raise ValueError(f"image.shape[0] % {__n} != 0 or image.shape[1] % {__n} != 0")
    row_n, col_n = image.shape[0] // __n, image.shape[1] // __n

    image_blocks = np.zeros((row_n, col_n, __n, __n))
    for row_i in range(row_n):
        for col_i in range(col_n):
            block_i, block_j = row_i * __n, col_i * __n
            block = image[block_i:block_i + __n, block_j:block_j + __n].astype(int)
            image_blocks[row_i, col_i, ...] = np.matmul(np.matmul(__h_t, block), __h)
    image_blocks[np.abs(image_blocks) <= eps] = 0
    return [[encode(block, __n) for block in blocks_row] for blocks_row in image_blocks]


def decompress(encoded_image: list) -> np.ndarray:
    image = np.zeros((len(encoded_image) * __n, len(encoded_image[0]) * __n), dtype=np.uint8)
    for encoded_row, block_i in zip(encoded_image, range(0, image.shape[0], __n)):
        for encoded_block, block_j in zip(encoded_row, range(0, image.shape[1], __n)):
            block = decode(encoded_block, __n)
            block = np.matmul(np.matmul(np.linalg.inv(__h_t), block), np.linalg.inv(__h))
            block = np.clip(np.round(block), 0, 255)
            image[block_i:block_i + __n, block_j:block_j + __n] = block
    return image


def __setup():
    global __n, __h, __h_t

    __n = 8
    __h = __comp_h(__n)
    __h_t = np.transpose(__h)


__setup()
