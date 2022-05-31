from random import randint


class RS4:
    _key: str
    
    def __init__(self, key_length: int):
        if not 1 < key_length < 256:
            raise ValueError('Key length should be in range [2,255]')
        self._key = ''.join([chr(randint(65, 122)) for c in range(key_length)])
    
    def _key_permutation(self):
        permutated = [c for c in range(256)]
        
        j = 0
        for i in range(256):
            j = (j + permutated[i] + ord(self._key[i % len(self._key)])) % 256
            permutated[i], permutated[j] = permutated[j], permutated[i]
        return permutated
    
    def _get_keystream(self, length):
        keystream = [0] * length
        permutated = self._key_permutation()
        i, j = 0, 0
        for k in range(length):
            i = (i + 1) % 256
            j = (j + permutated[i]) % 256
            permutated[i], permutated[j] = permutated[j], permutated[i]
            s = (permutated[i] + permutated[j]) % 256
            keystream[k] = permutated[s]
        return keystream
    
    def run(self, data: str):
        if not data:
            raise ValueError('Invalid input')
        keystream = self._get_keystream(len(data))
        result = ''.join([chr(ord(c) ^ keystream[i]) for i, c in enumerate(data)])
        return result