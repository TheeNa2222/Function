import os
def Function():
  os.system('cls&title by.theena')
  print('''
  1. a
  2. b
  ''')
  b = input("ข้อความที่ต้องการใส่")
  
  if b == '1':
    print("ข้อความ")
    Function()
    
  if b == '2':
    print("ข้อความ")
    Function()
    
if (__name__ == '__main__'):
  Function()
  #By.TheeNa
