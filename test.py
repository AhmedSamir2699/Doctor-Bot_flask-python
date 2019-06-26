import Question_Maker
import Prediction
import sqlite3
'''
mylist=[]
l=len(mylist)
if(l<1): 
    mylist3=Question_Maker.filter2(mylist)
    mylist3=Question_Maker.fillter(mylist3)
else:    
    mylist3=Question_Maker.fillter(mylist)
'''
 
def run(mylist3):
    mypre=[]
    mypre2=[]
    for i in range(10):
       p=Prediction.predict(mylist3)
       mypre2.append(p)
       if p not in mypre:
           mypre.append(p)
            
       
    ll=len(mypre2)
    l=len(mypre) 
    mypre3=[0]*l
    for i in range(l):
        for j in range(ll):
            if(mypre[i]==mypre2[j]):
                mypre3[i]+=1
        mypre3[i]=mypre3[i]/10*100
         
    mypre = [' '.join(item) for item in mypre]
    mypredict = []
    for i in range(l):
        disease = mypre[i].replace('Â', '')
        disease2 = disease.replace('\xa0',' ')
        mypredict.append(disease2)
    
    return mypredict,mypre3 



def s():
    con = sqlite3.connect("mydatabase.db")
    cur = con.cursor()
    query_string = """SELECT DISTINCT symptom FROM symptoms"""
    cur.execute(query_string)
    tips = cur.fetchall()
    cur.close()
    if len(tips) > 0:
        return tips
    return []


s22 = "cushingoidÃ\x82Â\xa0habitus"

s22 = s22.replace('Ã','')
s22 = s22.replace('Â','')
s22 = s22.replace('\xa0',' ')
s22 = s22.replace('\x82','')
print(s22)
if s22 == "cushingoid habitus":
    print("yes")


mylist3=["yellow sputum", "diarrhea", "neck stiffness", "headache", "chill", "transaminitis", "myalgia", "spontaneous rupture of membranes"]
# mylist3=Question_Maker.fillter(mylist) 
'''a = s()
for b in a:
    print(b[0])
'''


     
