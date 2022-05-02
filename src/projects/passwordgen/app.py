import sqlite3
import requests
import random
import json
import math
from flask import Flask, jsonify, render_template
from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__, template_folder='templates')

# numberPass = request.form.get("passAmount")
# lenghPass = request.form.get("passLength")
# typeOfPass = request.form.get("preference")

@app.route("/", methods = ['POST', 'GET'])
def index():
    typeOfPass = request.form.get("preference")
    number = request.form.get("passLength")
    numberPass = request.form.get("passAmount")
    apiRoutes = [typeOfPass, number, numberPass]
    if request.method == "POST" :
       a= digitsFunc(typeOfPass, int(numberPass), int(number))
       
       return render_template("index.html", a = a.json )
      #  return jsonify({"Password Type": typeOfPass, "Number of Password": numberPass, "Password Length": number })
    return render_template('index.html')




@app.route("/api/<typeOfPass>/<int:numberPass>/<int:number>", methods=["GET", "POST"])
def digitsFunc(typeOfPass, numberPass, number):
    digits = ["2","3","4","5","6","7","8","9"]
    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    upperAndlower = uppercase + lowercase
    letter_and_digits = upperAndlower + digits
    special_characters = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.', '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']
    jungleJuice = letter_and_digits + special_characters
    f = open("/home/firdavs/Desktop/CS460/src/projects/passwordgen/words.txt", "r")
    templist = []
      
    for line in f:
       templist.append(line)
    temppList = []
    for ch in templist:
       tem = ''
       for x in ch:
          if x.isalpha():
             tem += x
       temppList.append(tem)

    numberofPasswords = []

    
    
    
    if typeOfPass == "digits":

     
      cal = int(math.log((len(digits)**number), 2))

      if cal < 40:
         status = "Avoid"
      elif cal > 40 and cal < 60:
         status = "Very Weak"
      elif cal > 60 and cal < 80:
         status = "Weak"
      elif cal > 80 and cal < 100:
         status = "Strong"
      elif cal > 100:
         status = "Very Strong"
      
      # choice.append(status)


      for i in range(numberPass):


         temp = random.sample(digits*10,int(number))
      
         password = "".join(temp)
         numberofPasswords.append(password)

    if typeOfPass == "lowerCase":

      cal = int(math.log((len(lowercase)**number), 2))

      if cal < 40:
         status = "Avoid"
      elif cal > 40 and cal < 60:
         status = "Very Weak"
      elif cal > 60 and cal < 80:
         status = "Weak"
      elif cal > 80 and cal < 100:
         status = "Strong"
      elif cal > 100:
         status = "Very Strong"





      for i in range(numberPass):

         temp = random.sample(lowercase*26,int(number))
      
         password = "".join(temp)
         numberofPasswords.append(password)

    if typeOfPass == "upperCase":


      cal = int(math.log((len(uppercase)**number), 2))

      if cal < 40:
         status = "Avoid"
      elif cal > 40 and cal < 60:
         status = "Very Weak"
      elif cal > 60 and cal < 80:
         status = "Weak"
      elif cal > 80 and cal < 100:
         status = "Strong"
      elif cal > 100:
         status = "Very Strong"


      for i in range(numberPass):

         temp = random.sample(uppercase*26,int(number))
      
         password = "".join(temp)
         numberofPasswords.append(password)

    if typeOfPass == "lowUpCase":


      cal = int(math.log((len(upperAndlower)**number), 2))

      if cal < 40:
         status = "Avoid"
      elif cal > 40 and cal < 60:
         status = "Very Weak"
      elif cal > 60 and cal < 80:
         status = "Weak"
      elif cal > 80 and cal < 100:
         status = "Strong"
      elif cal > 100:
         status = "Very Strong"

      for i in range(numberPass):

         temp = random.sample(upperAndlower,int(number))
      
         password = "".join(temp)
         numberofPasswords.append(password)

    if typeOfPass == "digitsandLetters":

      cal = int(math.log((len(letter_and_digits)**number), 2))

      if cal < 40:
         status = "Avoid"
      elif cal > 40 and cal < 60:
         status = "Very Weak"
      elif cal > 60 and cal < 80:
         status = "Weak"
      elif cal > 80 and cal < 100:
         status = "Strong"
      elif cal > 100:
         status = "Very Strong"




      for i in range(numberPass):

         temp = random.sample(letter_and_digits,int(number))
      
         password = "".join(temp)
         numberofPasswords.append(password)
    
    if typeOfPass == "specialCharacters":

      cal = int(math.log((len(special_characters)**number), 2))

      if cal < 40:
         status = "Avoid"
      elif cal > 40 and cal < 60:
         status = "Very Weak"
      elif cal > 60 and cal < 80:
         status = "Weak"
      elif cal > 80 and cal < 100:
         status = "Strong"
      elif cal > 100:
         status = "Very Strong"

      for i in range(numberPass):

         temp = random.sample(special_characters*100,int(number))
      
         password = "".join(temp)
         numberofPasswords.append(password)

    if typeOfPass == "everything":

      cal = int(math.log((len(jungleJuice)**number), 2))

      if cal < 40:
         status = "Avoid"
      elif cal > 40 and cal < 60:
         status = "Very Weak"
      elif cal > 60 and cal < 80:
         status = "Weak"
      elif cal > 80 and cal < 100:
         status = "Strong"
      elif cal > 100:
         status = "Very Strong"

      for i in range(numberPass):

         temp = random.sample(jungleJuice*100,int(number))
      
         password = "".join(temp)
         numberofPasswords.append(password)


    if typeOfPass == "phrase":

       

     
      cal = int(math.log((len(temppList)**number), 2))

      if cal < 40:
         status = "Avoid"
      elif cal > 40 and cal < 60:
         status = "Very Weak"
      elif cal > 60 and cal < 80:
         status = "Weak"
      elif cal > 80 and cal < 100:
         status = "Strong"
      elif cal > 100:
         status = "Very Strong"
      
      # choice.append(status)
      chars = ["@", "#", "$", "*", "&"]

      sel = random.choice(chars)
      
      nums = []

      for i in range(number):
         x = random.choice(temppList)
         nums.append(x)

      for n in range(number):
         temp = []
         for i in range(numberPass):
            
            # temp = random.sample(len(temppList),int(number))
            randomName = random.choice(temppList)
            # rand2 = random.choice(nums)
            
            connect1 = randomName + sel 
            xy = "".join(connect1)
         
            temp.append(xy)
         xyz = ''.join([str(item) for item in temp])

         numberofPasswords.append([xyz])

        


    return jsonify({"Entropy": cal, "Password":numberofPasswords, "Recommendation": status})
    # f"{number}"






# typeOfPass = request.form.get("preference")
# number = request.form.get("passLength")
# numberPass = int(request.form.get("passAmount"))
# apiRoutes = [typeOfPass, number, numberPass]
# digitsFunc(numberPass)



if __name__ == "__main__":
    app.debug = True
    
    app.run()