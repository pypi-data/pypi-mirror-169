from hexlib.HexRow import HexRow

class HexTwin():
    def __init__(self, path="") -> None:
        self.path = path
        self.rows = []
        if(path != ""):
            self.__read()

    def fromHexValues(hexValues):
        # Split hexValues into rows of 16 bytes
        # hexValues need to: ["ab", "0f", "3d", "ec", ....]
        h = HexTwin("")
        splittedRows = [hexValues[x:x+16] for x in range(0, len(hexValues), 16)]
        h.rows = [HexRow(hex(i*16).split("x")[-1], splittedRows[i]) for i in range(0, len(splittedRows))]
        return h
        
    def __read(self):
        with open(self.path, "rb") as f:
            offset = 0
            while True:
                bytes_ = f.read(16)
                if not bytes_:
                    break
                hV = self.__getHexValues(bytes_)
                row = HexRow(self.__formatOffset(offset), hV)
                self.rows.append(row)
                offset += 16

    def __getHexValues(self, bytes_):
        # Convert the bytes to a list of hex values
        hexValues = [hex(x).split('x')[-1].upper() for x in list(bytes_)]
        # While converting the bytes, the leading zeros gets cut of
        # the following instructions check if there are 2 characters
        # and adds a leading zero if necessary
        return [h if len(h)==2 else "0"+h for h in hexValues]

    def __formatOffset(self, offset):
        r = hex(offset).split('x')[-1]
        return r