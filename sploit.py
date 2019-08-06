import base64, zlib, marshal, sys
 
W = '\x1b[1;37m'
RR = '\x1b[1;37m\x1b[31m'
O = '\x1b[33m'
B = '\x1b[34m'

echo $bi"  _____       _ ______ "           
echo $me" / ____|     | |  ____|"           
echo $pu"| (___  _ __ | | |__   _ __   ___" 
echo $cy" \___ \| '_ \| |  __| | '_ \ / __|"
echo $pur" ____) | |_) | | |____| | | | (__" 
echo $bi"|_____/| .__/|_|______|_| |_|\___|" 
       echo $pu"| |"                        
       echo $bi"|_|"    echo $cy"Coders By TheSploit"
			  echo $pu"WA : 081316577616" 
  
      echo $cy"⊱XͭPͪLͤᗝIƬ༻₁₀₀ᵏ Menu:"
	  echo $bi"["$pu"1"$bi"]"$i" endcrypt file dengan base64"
	  echo $bi"["$pu"2"$bi"]"$i" endcrypt file dengan base16"  
	  echo $bi"["$pu"3"$bi"]"$i" endcrypt file dengan base32"  
	  echo $bi"["$pu"4"$bi"]"$i" endcrypt file dengan marshal"
	  echo $bi"["$pu"6"$bi"]"$i" endcrypt file dengan zlib&base64"
	  echo $bi"["$pu"7"$bi"]"$i" endcrypt file dengan zlib&base64&marshal"
	  echo $bi"["$pu"8"$bi"]"$i" endcrypt file dengan zlib&base16&marshal"
	  echo $bi"["$pu"9"$bi"]"$i" endcrypt file dengan zlib&base32&marshal"
	  echo $bi"["$pu"10"$bi"]"$i" keluar"
	  echo $bi"["$pu"11"$bi"]"$i" tentang").format(W, O, W, RR, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W, B, RR, B, W)
 
def main():
    choice = raw_input(RR + '[++ ' + W + 'Choose: ')
    if choice == '1' or choice == '01':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b64encode(fileopen)
            b = "import base64\nexec(base64.b64decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()
 
    if choice == '2' or choice == '02':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b16encode(fileopen)
            b = "import base64\nexec(base64.b16decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()
 
    if choice == '3' or choice == '03':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = base64.b32encode(fileopen)
            b = "import base64\nexec(base64.b32decode('" + a + "'))"
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()
 
    if choice == '4' or choice == '04':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            a = compile(fileopen, 'dg', 'exec')
            m = marshal.dumps(a)
            s = repr(m)
            b = 'import marshal\nexec(marshal.loads(' + s + '))'
            c = file.replace('.py', '_endcrypt.py')
            d = open(c, 'w')
            d.write(b)
            d.close()
            print RR + '[*] ' + W + 'OUTPUT:', c
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()
 
    if choice == '5' or choice == '05':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            c = zlib.compress(fileopen)
            d = base64.b64encode(c)
            e = 'import marshal,zlib,base64\nexec(zlib.decompress(base64.b64decode("' + d + '")))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()
 
    if choice == '6' or choice == '06':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b64encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b64decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()
 
    if choice == '7' or choice == '07':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b16encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b16decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()
 
    if choice == '8' or choice == '08':
        try:
            file = raw_input(RR + '[+] ' + W + 'File: ')
            fileopen = open(file).read()
            sa = compile(fileopen, 'dg', 'exec')
            sb = marshal.dumps(sa)
            c = zlib.compress(sb)
            d = base64.b32encode(c)
            e = 'import marshal,zlib,base64\nexec(marshal.loads(zlib.decompress(base64.b32decode("' + str(d) + '"))))'
            f = file.replace('.py', '_endcrypt.py')
            g = open(f, 'w')
            g.write(e)
            g.close()
            print RR + '[*] ' + W + 'OUTPUT:', f
            main()
        except:
            print RR + '[-] ' + W + 'File not found!'
            main()
 
    if choice == '9' or choice == '09':
        sys.exit(RR + '[*] ' + W + 'See you and Thanks for using this tools')
    else:
        if choice == '10':
            print '\n\tCODERS\n\t===================================\n\tCODERS BY : TheSploit\n\tCODERS   : Sploit1109\n\tPASTEBIN   : https://pastebin.com/u/TheSPloit\n\tGITHUB     : https://github.com/TheSploit\n\t\t     \n\tSUBS My YOUTUBE ACCOUNT FOR MORE DETAILS\n\t===================================\n\tYoutube : TryOne\n\tGITHUB : TheSploit\n\t===================================\n\t'
            main()
        else:
            print RR + '[-] ' + W + 'WRONG INPUT!!'
            sys.exit(RR + '[*] ' + W + 'See you and Thanks for using this tools')
 
 
if __name__ == '__main__':
    main()
