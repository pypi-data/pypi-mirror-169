from hexlib.HexTwin import HexTwin

class Hexdump():
    def __init__(self,) -> None:
        self.filterZeroRows = False
        self.filterNonAsciiRows = False
        self.zeroRowCounter = 0
        self.nonAsciiRowCounter = 0

    def filter(self, filterZeroRows=False, filterNonAsciiRows=False):
        self.filterZeroRows = filterZeroRows
        self.filterNonAsciiRows = filterNonAsciiRows

    def __filterZeroRows(self, row):
        if(row.isZeroRow):
            self.zeroRowCounter += 1
        elif(not row.isZeroRow):
            if(self.zeroRowCounter > 0):
                self.__printPlaceholder(f"{str(self.zeroRowCounter)} zero rows")
                self.zeroRowCounter = 0
            self.__printRow(row)
    
    def __filterNonAsciiRows(self, row):
        if(row.isNonAsciiRow):
            self.nonAsciiRowCounter += 1
        elif(not row.isNonAsciiRow):
            if(self.nonAsciiRowCounter > 0):
                self.__printPlaceholder(f"{str(self.nonAsciiRowCounter)} non-ascii rows")
                self.nonAsciiRowCounter = 0
            self.__printRow(row)
    
    def printTwin(self, twin):
        self.__printHexTableHeader()
        for row in twin.rows:
            self.__printHexTableRow(row)

    def printHexValues(self, hexValues):
        twin = HexTwin.fromHexValues(hexValues)
        self.printTwin(twin)
      
    def __printHexTableHeader(self):
        h = "{:10}     {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}   {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}      {:5}".format("    Offset", "00", "01", "02", "03", "04", "05",
                                                                                                                          "06", "07", "08", "09", "0A", "0B",
                                                                                                                          "0C", "0D", "0E", "0F", "ASCII")
        print(h)
        print("----------     -------------------------------------------------------------------------------        ----------------")

    def __printHexTableRow(self, row):
        if(self.filterNonAsciiRows):
            self.__filterNonAsciiRows(row)
        elif(self.filterZeroRows):
            self.__filterZeroRows(row)
        else:
            self.__printRow(row)

    def __printRow(self, row):
        formatStr = "{:10}     {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}   {:4} {:4} {:4} {:4} {:4} {:4} {:4} {:4}      {:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}{:1}"
                
        h = [value for value in row.hexValues]
        h.insert(0, self.__paddingOffset(row.offset))

        a = [asc for asc in row.asciiValues]
        a.insert(0, "")

        # Padding for lines with less than 16 bytes
        while True:
            if (len(h) < 17):
                h.append("  ")
                a.append(".")
            else:
                break

        r = formatStr.format(h[0],
                             h[1], h[2],  h[3],  h[4],  h[5],  h[6],  h[7],  h[8],
                             h[9], h[10], h[11], h[12], h[13], h[14], h[15], h[16],
                             a[1], a[2],  a[3],  a[4],  a[5],  a[6],  a[7],  a[8],
                             a[9], a[10], a[11], a[12], a[13], a[14], a[15], a[16])
        print(r)

    def __printPlaceholder(self, text):
        msg = f" Skipped {text} "
        print("")
        print(("-"*45) + ">" + msg + "<" + ("-"*45))
        print("")

    def __paddingOffset(self, offset):
        return str(offset).rjust(10, "0").upper()