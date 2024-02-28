from unit1 import cube

def main():
    test_cube()

def test_cube():
   if cube(2) ==8:
      print("2 cube was 8")
   if cube(3) ==25:
      print("3 cube was 27")
if __name__=="__main__":
    main()