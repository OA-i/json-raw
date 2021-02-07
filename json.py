import requests, os, time

os.system("clear")
header = """   _____    _     _
  /  _  \\  / \\   |_|  Json Raw
  | | | | / _ \\  | |  Simpan file jsonmu di sini
  | |_| |/ ___ \\ | |
  \\_____/_/   \\_\\|_|  Github : https://github.com/OA-i"""
  
#Json raw api
url = "https://highland-bypasses.000webhostapp.com/json-raw/api?value="
urledit = "https://highland-bypasses.000webhostapp.com/json-raw/api"

def body():
  print(header)
  print("\n  " + 40 * "=")
  print("\n  (1) Simpan dari text\n  (2) Simpan dari file\n  (3) Edit file")
  pilih()
  
#Cara menyimpan
def pilih():
  cara_menyimpan = input("\n  Pilih cara menyimpan : ")
  
  if cara_menyimpan == "1":
    simpan_text()
  elif cara_menyimpan == "2":
    simpan_file()
  elif cara_menyimpan == "3":
    edit_file()
  else:
    print("  Pilihan tidak ada")
    time.sleep(1.0)
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
    print("  Hasil : https://highland-bypasses.000webhostapp.com/json-raw/api/" + req.text)
    buka_file_json.close()
  except:
    print("  Gagal menyimpan")

def edit_file():
  global id_json
  id_json = input("\n  Masukkan id file : ")
  try:
    reqii = requests.get(urledit + "/" + str(id_json) + "/index.json")
    print("\n  File : " + reqii.text)
  except:
    print("  Error")
  print("\n  (1) Edit dari text\n  (2) Edit dari file")
  pilihedit()
  
def pilihedit():
  pilihedit = input("\n  Pilih cara mengedit : ")
  
  if pilihedit == "1":
    edit_text()
  elif pilihedit == "2":
    edit_filef()
  else:
    print("  Pilihan tidak ada")
    time.sleep(1.0)
    pilihedit()
    
def edit_text():
  edit_json = input("  Edit file (Ketik Ulang) : ")
  try:
    reqiii = requests.get("https://highland-bypasses.000webhostapp.com/json-raw/api/edit.php?value=" + edit_json.replace(" ", "%20").replace("\\n", "%0A") + "&id=" + str(id_json))
    print("  Hasil : https://highland-bypasses.000webhostapp.com/json-raw/api/" + str(id_json))
  except :
    print("  Gagal mengedit")
    
def edit_filef():
  file_edit_json = input("  Masukkan file json : ")
  buka_edit_json = open(file_edit_json, "r")
  baca_edit_json = bula_file_json.read()
  try:
    reqiii = requests.get("https://highland-bypasses.000webhostapp.com/json-raw/api/edit.php?value=" + baca_edit_json.replace(" ", "%20").replace("\n", "%0A") + "&id=" + str(id_json))
    print("  Hasil : https://highland-bypasses.000webhostapp.com/json-raw/api/" + str(id_json))
    buka_edit_json.close()
  except :
    print("  Gagal mengedit")
    
body()
