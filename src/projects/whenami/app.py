import zipfile

password = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla et dui eu libero fringilla facilisis. Aenean porttitor, tellus ut posuere sagittis, quam turpis fringilla elit, quis tincidunt est leo at quam. Quisque consectetur enim ipsum, at consequat tort or ullamcorper id. Donec in venenatis nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vulputate, eros at bibendum mollis, erat sem semper lectus, ac interdum neque nunc ut velit. Praesent commodo turp is arcu, non viverra tortor consectetur nec. Ut euismod at velit sit amet faucibus. Praesent eleifend pellentesque pellentesque. Vivamus sed condimentum purus. Suspendisse ultrices luctus eleifend. Curabitur sodales purus vitae tellus pulvinar, at euismod elit congue. Vestibulum vitae euismod mi. In ornare eros tellus, quis efficitur eros mattis vel. Nam risus enim, convallis eget sem eu, luctus sagittis ex. Integer tristique tellus ac purus fermentum, vel accumsan felis finibus."

transformed1 = password.replace(",", "")
transformed2 = transformed1.replace(".","")
finalPassword = transformed2.split(" ")
for i in range(len(finalPassword)):
    singlePassword = finalPassword[i]
    print(singlePassword)



def crackZip(file_name, passwd):
    file = zipfile.ZipFile(file_name)
    try:
        file.extractall(pwd = bytes(passwd, 'utf-8'))
        return True
    except Exception:
        return False
 
        
passwords = finalPassword
file_name = 'secret.1'
for password in passwords:
    ret = crackZip(file_name, password)
    if (ret):
        print('The password is',password)
    else:
        continue


secret1 = "pellentesque"
secret2 = ""
print(finalPassword)