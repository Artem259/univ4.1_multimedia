import numpy as np


__eps: float


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


def __h(size: int) -> np.ndarray:
    h1, h2, h3 = __h1(size), __h2(size), __h3(size)
    return np.matmul(np.matmul(h1, h2), h3)


def compress(image: np.ndarray, compression_ratio: float = 1.5) -> np.ndarray:
    if image.shape[0] != image.shape[1]:
        raise ValueError("image.shape[0] != image.shape[1]")
    size = image.shape[0]
    if not ((size & (size-1) == 0) and size != 0):
        raise ValueError("The size of the input image must be a power of two.")

    h = __h(size)
    h_t = np.transpose(h)
    b = np.matmul(np.matmul(h_t, image), h)

    non_zero = round(np.sum(np.abs(b) > __eps) / compression_ratio)
    to_zero = b.size - non_zero

    b_flat = b.flatten()
    sorted_indices = np.argsort(b_flat)
    b_flat[sorted_indices[:to_zero]] = 0
    b = b_flat.reshape(b.shape)
    return b


def decompress(encoded_image: np.ndarray) -> np.ndarray:
    size = encoded_image.shape[0]
    h = __h(size)
    h_t = np.transpose(h)
    decompressed = np.matmul(np.matmul(np.linalg.inv(h_t), encoded_image), np.linalg.inv(h))
    decompressed = np.clip(np.round(decompressed), 0, 255)
    return decompressed.astype(np.uint8)


def __setup():
    global __eps
    __eps = 1e-10


__setup()
