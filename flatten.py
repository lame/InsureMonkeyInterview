import re


class Flatten():
    """
    This class will take a list or arbitrary list of lists
    and return a list with just the alpha elements int the
    order they were received regardless of list depth.
    """
    def __init__():
        pass

    def flatten_list(in_list):
        """
        Though this can be done easily iteratively I thought I'd have a little
        fun and do it with regular expressions. Naively I believe not iterating
        might provide some performance enhancements depending on depth of lists.
        """
        return re.findall('(\w[a-zA-Z]*)', str(in_list))
