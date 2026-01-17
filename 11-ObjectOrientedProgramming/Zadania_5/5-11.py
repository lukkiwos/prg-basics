class C():
    def __init__(self, sectors):
        self.sectors = sectors

    def m1(self, s, n):
        self.sectors[s] = n

    def m2(self, s):
        total = 0
        for sector in s:
            if sector in self.sectors:
                total += self.sectors[sector]
        return total
    

def main():
    stadium = C({"A":120, "D":150, "G":90, "K":110})

    stadium.m1("G", 130)

    print(stadium.m2("GD"))   # 280
    print(stadium.m2("KEJ"))  # 110


if __name__ == '__main__':
    main()