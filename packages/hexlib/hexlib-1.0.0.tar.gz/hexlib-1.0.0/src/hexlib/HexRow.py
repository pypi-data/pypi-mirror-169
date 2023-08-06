class HexRow():
    def __init__(self, offset, values) -> None:
        self.offset = offset
        self.hexValues = values
        self.asciiValues = []
        self.isZeroRow = False
        self.isNonAsciiRow = False
        self.__getAscii()
        self.__checkZero()
        self.__checkNonAscii()

    def __getAscii(self):
        for hex_ in self.hexValues:
            self.asciiValues.append(self.__hexToAscii(hex_))

    def __hexToAscii(self, hex_):
        result = "."
        if (hex_ != "  "):
            d = int(hex_, 16)
            if (d >= 32 and d <= 126):
                result = chr(d)
        return result

    def __checkZero(self):
        if(self.__isUniqueList(self.hexValues, "00")):
            self.isZeroRow = True

    def __isUniqueList(self, l, v):
        return all(x == v for x in l)

    def __checkNonAscii(self):
        notAnAscii = []
        for hex_ in self.hexValues:
            d = int(hex_, 16)
            if (d >= 32 and d <= 126):
                notAnAscii.append(False)
            else:
                notAnAscii.append(True)
    
        if(all(notAnAscii)):
            self.isNonAsciiRow = True