# project kane
import random
import datetime
import json
import os
MEMORY_FILE="kane_memory.json"
def load_memory():
    if os.path.excist(MEMORY_FILE):
      with open (MEMORY_FILE,"r") as f:
        return json.load(f)
      return{"name": None, "favourite_colour": None , "mood" : "nuetral","history":[]}
    def save_memory(data):
       with open(MEMORY_FILE, "W")as f:
          json.dump(data.f)
          memory=load_memory
          user_name=memory.get("name")
          responses={
             "greeting":["Hey{name}!","yo{name}, what's good?","sup human?","kane reporting in!","Hello there , legend."],
             "jokes":[
                "I told my therapist'm afraid of random letters...she sad I have type A personality"
                "parallel lines have so much in common . It's a shame they will never meet."
                "I only know 25 letters of the alphabet. i dont know y"
                "Want hre a joke about construction , sorry am working on it"
             ],
             "compliment":[
                "You are my favourite human, don't tell the others"
                "YOU are so cool you make penguins gealous"
                "if you were a vagetable, you'd be a cute-cumber"
             ],
             "roast":{
                "you are like a cloud. When you disappear it is buetiful day"
                "If you were any slower , you'd be going backwards."
                "you,re proof that even mistake  can be lovable."
             }
          }  
          print("KANE:*Boots up with dramatic music*")
          print("kane:I am kane the best for you!")
          while True:
             messge=input(f"{'you':<12}:").strip().lower()
             if message in ["bye","goodbye","exit","quit","see ya","see u"]:
                print