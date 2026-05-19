class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        head = ""
        for s in strs:
            head = str(len(s))
            encoded += head+"#"+s
        return encoded

    def decode(self, s: str) -> List[str]:
        encoded = s
        decoded = []
        len_encoded = len(encoded)
        while len_encoded:
            digits = 0
            for c in encoded:
                if c == "#":
                    break
                digits+=1

            word_lenght = int(encoded[:digits])
            word_start=digits+1
            word_end=word_start+word_lenght
            word = encoded[word_start:word_end]
            
            encoded = encoded[word_end:]
            
            len_encoded = len(encoded)
            decoded.append(word)
        return decoded