
class Multiplier:
    num1:int = 0
    num2:int = 0

    def getProduct(self):
        return self.num1 * self.num2

def main():
    m = Multiplier()
    m.num1 = 7
    m.num2 = 3
    print(f"{m.num1} X {m.num2} = {m.getProduct()}")

if __name__ == "__main__":
    main()