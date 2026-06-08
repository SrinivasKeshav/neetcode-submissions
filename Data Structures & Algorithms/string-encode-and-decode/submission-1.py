class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded = encoded + "!*#" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        return s.split("!*#")[1:]
