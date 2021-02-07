import requests, os, time

os.system("clear")
header = """   _____    _     _
  /  _  \\  / \\   |_|  Json Raw
  | | | | / _ \\  | |  Simpan file jsonmu di sini
  | |_| |/ ___ \\ | |
  \\_____/_/   \\_\\|_|  Github : https://github.com/OA-i"""
  
#Json raw api
url = "https://highland-bypasses.000webhostapp.com/json-raw/api?value="

def body():
  print(header)
  print("\n  " + 40 * "=")
  print("\n  (1) Simpan dari text\n  (2) Simpan dari file")
  pilih()
  
#Cara menyimpan
def pilih():
  cara_menyimpan = input("\n  Pilih cara menyimpan : ")
  
  if cara_menyimpan == "1":
    simpan_text()
  elif cara_menyimpan == "2":
    simpan_file()
  else:
    print("  Pilihan tidak ada")
    time.sleep(0.5)
    os.system("clear")
    body()
  
#Simpan dari text
def simpan_text():
  text_json = input("\n  Masukkan text json : ")
  try:
    req = requests.get(url + text_json.replace(" ", "%20").replace("\\n", "%0A"))
    print("  Hasil : https://highland-bypasses.000webhostapp.com/json-raw/api/" + req.text)
  except:
    print("  Gagal menyimpan")
    
#Simpan dari file
def simpan_file():
  file_json = input("\n  Masukkan file json : ")
  buka_file_json = open(file_json, "r")
  baca_file_json = buka_file_json.read()
  try:
    req = requests.get(url + baca_file_json.replace(" ", "%20").replace("\n", "%0A"))
    print("  Hasil : https://highland-bypassess.000webhostapp.com/json-raw/api/" + req.text)
    buka_file_json.close()
  except:
    print("  Gagal menyimpan")
  
body()
