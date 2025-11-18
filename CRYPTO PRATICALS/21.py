# filename: 21_padding_motivation.py
"""
Pad/unpad using '1 followed by zeros' and explain why always include padding block.
"""
def pad_1zeros(data, block_size):
    pad_len = (block_size - (len(data) % block_size)) or block_size
    return data + b'\x80' + b'\x00'*(pad_len-1)

def unpad_1zeros(padded):
    i = len(padded)-1
    while i>=0 and padded[i]==0:
        i-=1
    if i>=0 and padded[i]==0x80:
        return padded[:i]
    raise ValueError("Invalid padding")

if __name__=='__main__':
    msg = b'HELLO'
    bsize = 8
    p = pad_1zeros(msg, bsize)
    print("Padded:", p.hex())
    print("Unpadded:", unpad_1zeros(p))
    print("\nWhy always pad even if message is exact multiple of block size?")
    print("- Prevents ambiguity when plaintext ends with bytes that could look like padding.")
    print("- Simplifies unpadding (always remove at least one block).")
