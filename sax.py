import numpy as np

SAX_INITIAL_KEY = 0x28559CA0
SAX_KEY_INCREMENT = 0xCEBD531B


def uint32_to_bytes(u):
    return [u & 0xff, (u >> 8) & 0xff, (u >> 16) & 0xff, (u >> 24) & 0xff]


def next_uint32(data_ptr):
    return (((data_ptr[3] << 24) & 0xff000000) + ((data_ptr[2] << 16) & 0xff0000) + ((data_ptr[1] << 8) & 0xff00) + (data_ptr[0] & 0xff)) & 0xffffffff


def uint(x):
    return x & 0xffffffff


def decode_sax_chunk(data_ptr, decode_code):
    """
    This function decodes an 8 bytes chunk (2 x 4-byte uint32_t)

    Note that due to little endian, the bytes are in different order than when used as a byte*
    """

    b0 = next_uint32(data_ptr)
    b0 &= 0xffffffff
    b1 = next_uint32(data_ptr[4:8])
    b1 &= 0xffffffff
    key = SAX_INITIAL_KEY

    i = 0
    while i < 32:
        b1 -= np.uint32(np.uint32(((decode_code[3] + np.uint32(b0 >> 5)) & 0xffffffff)) ^ np.uint32(((key + b0) & 0xffffffff)) ^ np.uint32(((decode_code[2] + b0 * 16) & 0xffffffff)))
        b1 &= 0xffffffff
        b0 -= np.uint32(np.uint32(((decode_code[1] + np.uint32(b1 >> 5)) & 0xffffffff)) ^ np.uint32(((key + b1) & 0xffffffff)) ^ np.uint32(((decode_code[0] + b1 * 16) & 0xffffffff)))
        b0 &= 0xffffffff
        key += SAX_KEY_INCREMENT
        key &= 0xffffffff
        i += 1

    return b0, b1


def decode_sax_data(data_ptr, data_len, decode_code):
    output = []
    i = 0
    ptr = 0
    while i < (data_len >> 3):  # todo: is >> 3 same as /8? can we replace i < len >> 3 with just ptr < len?
        b0, b1 = decode_sax_chunk(data_ptr[ptr:], decode_code)
        output.extend(uint32_to_bytes(b0))
        output.extend(uint32_to_bytes(b1))
        ptr += 8
        i += 1
    return output
