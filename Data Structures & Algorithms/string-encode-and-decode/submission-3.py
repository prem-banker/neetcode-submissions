class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return 'EMPTYARRAY'
        return 'BITCH'.join(strs)
    def decode(self, s: str) -> List[str]:
        if s == 'EMPTYARRAY':
            return []
        return s.split('BITCH')