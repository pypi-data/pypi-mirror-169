class HexTwin():
    def __init__(self, path="") -> None:
        self.path = path
        self.rows = []
        if(path != ""):
            self.__read()
       
    def __read(self):
        with open(self.path, "rb") as f:
            offset = 0
            while True:
                data = f.read(16)
                if(not data):
                    break
                byteArr = bytearray(data)
                isZeroRow = all(v == 0 for v in byteArr)
                isNonAsciiRow = all(not(v >= 32 and v <= 126) for v in byteArr)
                self.rows.append((offset, byteArr, isZeroRow, isNonAsciiRow))
                offset += 16