def main():
      cart1 = {"dress": "multi", "jacket": "pink", "shoes": "white"}
      cart2 = {"slacks": "black", "blouse": "white", "shoes": "black"}

      cart3 = cart1 | cart2
      print(cart3)

      cart4 = {"blouse": "red", "purse": "red"}
      cart2 |= cart4
      print(cart2)

if __name__ == "__main__":
        main()