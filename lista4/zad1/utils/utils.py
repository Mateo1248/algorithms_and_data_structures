import re


class Utils:
    
    
    @staticmethod
    def match(key, pattern_match = re.compile(".?[a-zA-Z]+.?"), pattern_search = re.compile("[a-zA-Z]+")):
        if pattern_match.fullmatch(key):
            try:
                return pattern_search.search(key).group(0)
            except:
                return None
        return None