import re
def test(txt,nu,mas1,mas2):
    if nu==1:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(mas1)
        txt=input(mas2)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return txt
    elif nu==2 :
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print(mas1)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
###########################################################################################################################
#to can to handling edit 
def contr():
    try:
        cont=0
        r=int(input(""))
        if r==1:
            cont=1 
        elif r==2:
            cont=2
        else:
            test(t,2,"input is wrong please choose form list","")
            return contr()
    except:
        test(t,2,"input is wrong please choose form list","")
        return contr()
    return cont
#---------------------------------------------------------------------------------------------------
def no_cond(word):
    #to use in condtion stetment
    c=""
    print ("how many condation you want in statment")
    no=int(input(""))
    print("______________________________________________________________________________")
    if no==1:
        print("enter the condation ")
        text=input("") 
        if langa==1 or langa==2 :
            c=word+"("+text+") {\n"
        elif langa==3:
            c=word+text+ ":\n"     
        
    else :
        print("____________________________________________________________________________")
        print("you want \n1-the  all of condations event\n2-one at least event ")
        r=int(input(""))
        rela=""
        if r==1:
            if langa==1 or langa==2  :
                rela="&&"                 
            elif langa==3:
                rela="and"    
        elif r==2:
            if langa==1 or langa==2  :
                rela="||"                 
            elif langa==3:
                rela="or"       
        if langa==1 or langa==2: 
            c+= word+"("                  
        elif langa==3:
            c+=word      
        for i in range(0,no-1):
            print("enter condation", i+1, "\n")
            text=input("")
            if langa==1 or langa==2: 
                c+=" "+text+" "+rela+" " 
            elif langa==3:
                c+=" "+text+" "+rela+" "
            print("______________________________________________________________________________")
                   
        print("enter condation", no, "\n")
        text=input("")
        if langa==1 or langa==2: 
            c+=text+" )  {\n"                  
        elif langa==3:
            c+=text+" :\n"
    return c            
#----------------------------------------------------------------------------------------------------
#to choose the value of varible
def value(value,n):
    def revalue():

        try:
            if n==1:
                print("do you want it in value or defualt or without value")
                print("1-value\n2-defualt\n3-without value")
                print("______________________________________________________________________________")
                ch=int(input(""))
                print("______________________________________________________________________________")
                if ch==1:
                    v=" = "+input("enter the value : ")
                    print("______________________________________________________________________________")
                elif ch==2:
                    v=" = "+value
                elif ch==3:
                    v=""
                    
                    
            
            elif n ==2:  
                print("do you want it in value or defualt (0)")
                print("1-value\n2-defualt")
                print("______________________________________________________________________________")
                ch=int(input(""))
                print("______________________________________________________________________________")
                if ch==1:
                    v=input("enter the value : ")
                    print("______________________________________________________________________________")
                elif ch==2:
                    v=value
            else:
                v=""
            return v         
        except:
            test(t,2,"input is wrong please choose form list","")
            val= revalue()
            return val
    val=revalue()
    return val

#--------------------------------------------------------------------------------------------------------    
#to choose the  language    
def lang():
    try:
        print("______________________________________________________________________________")
        print("what langauge you want\n1-c++\n2-java\n3-python")
        print("______________________________________________________________________________")
        l=int(input(""))
        if l==1:
            lan=1
        elif l==2:
            lan=2
        elif l==3:
            lan=3
        
        return lan
    except:
        test(l,2,"input is wrong please choose form list","")
        lang()
print("hi , programming is now easier\n")
#---------------------------------------------------------------------------------------------------------------------------
langa=lang()
#----------------------------------------varible-------------------------------------------------------------------------------
def varible (langa,na,fun):
    control_value=na
    print("enter the name of ",fun," :")
    print("______________________________________________________________________________")
    n=input("")
    while n=="":
        m="enter the name of "+fun+" :"
        n=test(n,1,m,"")

    def type():
        try:
            print("______________________________________________________________________________")
            print("enter the type of", fun,"\n1-integer\n2-float\n3-double\n4-string\n5-boolean\n6-char\n7-other  ")
            print("______________________________________________________________________________")
            t=int(input(""))
            if t==1:#integer 
                if langa==1 or langa==2:
                    c="int"+" "+n+value("0",control_value)+";" 
                elif langa==3:
                    c=n+" "+value("0",control_value)
            elif t==2:
                if langa==1 or langa==2:
                    c="float"+" "+n+value("0.0",control_value)+";" 
                elif langa==3 :
                    c=n+value("0.0",control_value)
            elif t==3:
                if langa==1 or langa==2:
                    c="double"+" "+n+value("0.0",control_value)+";" 
                elif langa==3 :
                    c=n+" "+value("0.0",control_value)
            elif t==4:
                if langa==1 or langa==2:
                    c="String"+" "+n+value("\"\"",control_value)+";" 
                elif langa==3 :
                    c=n+" "+value("\"\"",control_value)
            elif t==5:
                print("______________________________________________________________________________")
                print("defualt is true")
                print("______________________________________________________________________________")
                if langa==1 or langa==2:
                    c="Boolean"+" "+n+value("true",control_value)+";" 
                elif langa==3 :
                    c=n+" "+value("true",control_value)
            elif t==6:
                if langa==1 or langa==2:
                     c="char"+" "+n+value("\'\'",control_value)+";" 
                elif langa==3 :
                    c=n+" "+value("\'\'",control_value)       
            elif t==7:
                print("enter the type of",fun, " :")
                s=input("")
                if langa==1 or langa==2:
                    c=s+" "+n+value("",control_value)+";" 
                elif langa==3 :
                    c=n+" "+value("",control_value)
            return c
        except:
            test(t,2,"input is wrong please choose form list","")
            cd=type()
            return cd
    cd=type()
    return cd

#---------------------------------argument--------------------------------------------------------------------------------
def arg(lang,func):
    langaa=lang
    if langaa==1 or langaa==2: 
        func_of_arg=func
        arg1=varible(langaa,4,func_of_arg)
        arg2=arg1[:len(arg1)-1]
    elif langaa==3:
        print("enter the name of ",func," :")
        arg2=input("")
        print("______________________________________________________________________________")
        while arg2=="":
            m="enter the name of "+func+" :"
            arg2=test(arg2,1,m,"")
        
    
    return arg2
    
#--------------------------------input----------------------------------------------------------------------------------------    
def inp(langa,word):
    cd=""
    print("enter the name of varible ")
    n=input("")
    while n=="":
        n=test(n,1,"enter the name of varible","")
    if langa==1  :
        cd=word+">>"+n+";"+"\n"
        return cd
    def type():
        try:
            print("______________________________________________________________________________")
            print("enter the type of varible\n1-integer\n2-float\n3-double\n4-string\n5-boolean\n6-char")
            print("______________________________________________________________________________")
            t=int(input(""))
            print("______________________________________________________________________________")
            if t==1:#integer             
                if langa==2:
                    c=n+"=" +word+".nextInt()"+";"
                elif langa==3:
                    c=n+"=int(input(\"\"))"                
                    
            elif t==2:#float                  
                if langa==2:
                    c=n+"=" +word+".nextFloat()"+";"
                elif langa==3:
                    c=n+" =float(input(\"\"))"
            elif t==3: #double             
                if langa==2:
                    c=n+"=" +word+".nextDouble()"+";"
                elif langa==3:
                    c=n+"=double(input(\"\"))"
            elif t==4:                  
                if langa==2:
                    c=n+"=" +word+".nextLine()"+";"
                elif langa==3:
                    c=n+"=input(\"\")"                
            elif t==5:                  
                if langa==2:
                    c=n+"=" +word+".nextBoolean()"+";"
                elif langa==3:
                    c=n+"=boolean(input(\"\")) "
            elif t==6:                  
                if langa==2:
                    c=n+"=" +word+".nextChar()"+";"
                elif langa==3:
                    c=n+"=input(\'\')"                      
        
            return c
        except:
            test(t,2,"input is wrong please choose form list","")
            cd=type()
            return cd

        
    cd=type()
    return cd

#--------------------------------------------output--------------------------------------------------------------------------------------------------------  
def out(langa,word):
    try:
        print("______________________________________________________________________________")
        print ("how many arg you want print in one line")
        no=int(input(""))
        print("______________________________________________________________________________")
  
        if no==1:
            print("______________________________________________________________________________")
            print("enter the text of argument you want to print")
            text=input("if it is text put it between \"\"")
            print("______________________________________________________________________________")
            while text=="":
                text=test(text,1,"enter the text of argument you want to print","if it is text put it between \"\"")
            if langa==1:
                c=word +"<< "+text+"<<"+"endl;\n"                  
            elif langa==2:
                c=word+".println("+text+")"+";"+"\n"
            elif langa==3:
                c=word+"("+text+ ",\"\\n\") \n"    
        
        else :
            print("____________________________________________________________________________")
            print("enter the text of argument 1 you want to print")
            text=input("if it is text put it between \"\"")
            print("______________________________________________________________________________")
            while text=="":
                text=test(text,1,"enter the text of argument 1 you want to print","if it is text put it between \"\"")
            if langa==1:
                c=word+"<<"+text                  
            elif langa==2:
                c=word+".println("+text+")"+";"+"\n"
            elif langa==3:
                c=word+"("+text+","    
            for i in range(1,no-1):
                print("______________________________________________________________________________")
                print("enter the text of argument", i+1, "you want to print\n")
                text=input("you want to print if it is text put it between \"\" ")
                print("______________________________________________________________________________")
                while text=="":
                    mas1="enter the text of argument"+ str(i+1)+"you want to print\n"
                    text=test(text,1,mas1,"if it is text put it between \"\"")
                if langa==1: 
                    c+="<<"+text                  
                elif langa==2:
                    c+=word+".println("+text
                elif langa==3:
                    c+=text
            print("______________________________________________________________________________")
            print("enter the text of argument ",no, "you want to print")
            print("______________________________________________________________________________")
            text=input("if it is text put it between \"\"")
            print("______________________________________________________________________________") 
            while text=="":
                mas1="enter the text of argument"+ str(no)+"you want to print\n"
                text=test(text,1,mas1,"if it is text put it between \"\"")
            if langa==1:
                c+="<<"+text+"<<"+"endl ;\n"                  
            elif langa==2:
                c+="+"+text+")"+";"+"\n"
            elif langa==3:
                c+=","+text+",\"\\n\") \n"               
                    
        return c
    except:
        test(t,2,"input is wrong please integer number","")
        return out(langa)
#------------------------------------------looping-------------------------------------------------------------------------
def for_loop (langa):
    c=""
    ty_arg=""
    argu=""
    ty_arg=arg(langa,"argument")#int n1 (as example)
    argu=re.split("\s",ty_arg)#divide string to list and divide it by space
   
    start=input("enter the start value")
    while start=="":
        start=test(start,1,"","please enter the start value ")
    step=input("enter the step value(ex +2 / -2) : ")
    while step=="" :
        step=test(step,1,"","please enter the step value(ex *2/+2 / -2) :")
    while not step.startswith("+") and not step.startswith("-") and not step.startswith("*"):
         step=test(step,1,"","please enter the step value in this form (ex / *2/+2 / -2) :")
    if langa==1 or langa==2  :
        cond=input("enter the condation ")
        while cond=="":
            cond=test(cond,1,"","please enter the condation ")
        c="for("+ty_arg+"="+start+";"+cond+";"+argu[1]+"="+step+") {\n"#argu[1]-->n1 only
    elif langa==3:
        end=input("enter the end of loop")
        c="for"+" "+ty_arg+" "+"in range"+"("+start+","+end+","+step+")" +":\n"
    return c        
############################################################################################################################
def while_loop(langa):
    c=no_cond("while")
    return c
############################################################################################################################3
def loop(langa):
    try:
        langa=langa
        cd=""
        control=0
        t=0
        ccd=""
        print("choose\n1-for loop\n2-while loop")
        con=int(input(""))
        if con==1:
            ccd=for_loop(langa)
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd=for_loop()
                elif t==2:
                    cd=ccd
                    control=1             
        elif con==2:
            ccd=while_loop(langa)
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd=while_loop(langa) 
                elif t==2:
                    control=1
                    cd=ccd
                                   
        return cd
            
    except:
        test(t,2,"input is wrong please choose form list","")
        return loop(langa)
    
#-------------------------------------------condation------------------------------------------------------------------------------------------
def if_statment(langa):
    try:
        c=""
        print("1- if \n2-if else \n3-else")
        sel=int(input(""))
        word=""
        if sel==1 :
            word="if"
        elif sel==2:
            if langa==1 or langa==2 :
                word="else if"
            elif langa==3:
                word="elif"
        elif sel==3:
            if langa==1 or langa==2: 
                c="else {"                  
            elif langa==3:
                c="else :"
        else:
            test(t,2,"input is wrong please choose form list","")
            return if_statment(langa)       
                
            return c
        c=no_cond(word)
        
    except:
        test(t,2,"input is wrong please choose form list","")
        return if_statment(langa)       
    return c
##########################################################################################################################
def switch (langa):
    try:
        if langa==1 or langa==2:
            print("1-new switch \n2-new case\n3-close case \n4-default")
            sel=int(input(""))
            if sel==1:
                print(" enter the Expression of the switch")
                swt=input("")
                while swt=="":
                    swt=test(swt,1," please enter the Expression of the switch","")
                c="switch ("+" "+swt+" ) {"
            elif sel==2:
                print(" enter the constant of the switch","")
                case=input("")
                while case=="":
                    case=test(case,1," please enter the constant of the switch")
                c= "case"+" "+case+" :"
            elif sel==3:
                c="break;"
            elif sel==4:
                c="defualt :"
        elif langa==3:
            print("I'm sorry but  python does not support switch you can use (if and elif) instead of it ")
            c=""
        return c    
    except:
        test(t,2,"input is wrong please choose form list","")
        return switch(langa)
    
##############################################################################################################################
def cond (langa):
    try:
        langa=langa
        cd=""
        ccd=""
        control=0
        print("choose\n1-if statment\n2-switch")
        con=int(input(""))
        if con==1:
            ccd=if_statment(langa)
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
            if t==1:
                ccd=if_statment(langa) 
            else:
                cd=ccd
                control=1                
        elif con==2:
            ccd=switch(langa)
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd=if_statment(langa) 
                else:
                    cd=ccd
                    control=1
        else:
            test(t,2,"input is wrong please choose form list","")
            return cond(langa)
            
        return cd
    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("input is wrong please choose form list")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return cond(langa)
#---------------------------------------------funcation-----------------------------------------------------------------------------------
def func(langa):
    try:
        ty_fun=""
        ty_fun=arg(langa,"function")
        no_arg=int(input("enter the no of argument : "))
        if langa==1 :
            c=ty_fun+" "+"("                
        elif langa==3:
            c="def "+ty_fun+" "+"("
        for i in range (0,no_arg-1):
            if langa==1 :
                ty_arg=arg(langa,"argument "+str(i+1))
                c+=" "+ty_arg+" , "
            elif langa==3:
                ty_arg=arg(langa,"argument "+str(i+1))
                c+=" "+ty_arg+" , "
        if langa==1 :
            ty_arg=arg(langa,"argument "+str(no_arg))
            c+=" "+ty_arg+ " ) { \n"
        elif langa==3:
            ty_arg=arg(langa,"argument "+str(no_arg))
            c+=" "+ty_arg+" ) : \n"  
            
        return c
    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("input is wrong please integer number")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return func(langa)
#---------------------------------------------files------------------------------------------------------------------------
def files (langa) :
    lang=langa
    try:
        nmfile=input("enter the name of file")
        nmfile+=".txt"
        print("1-write to file\n2-read form file")
        sel=int(input(""))
        if sel==1:
            if lang==1:  
                c="ofstream outfile; \n outfile.open( \" " + nmfile+"\");\n"
                c+= out(lang,"outfile")+"\n"
                c+="outfile.close() ;\n"
            elif lang==2:
                c="PrintWriter outputStream = \n new PrintWriter(new FileWriter ( \" "+ nmfile +"\" ));\n"
                c+= out(lang,"outputStream")+"\n"
                c+="outputStream.close();\n"
            elif lang==3:
                c="f= open ( \' "+nmfile+"\' ,  \' w \' )\n"
                c+= out(lang,"f.write")
                c+="f.close()\n"
                
        elif sel==2:
            if lang==1:   
                c="ifstream infile; \n infile.open(\" " + nmfile+"\");\n"
                c+= inp(lang,"infile")+"\n"
                c+="infile.close(); \n"
            elif lang==2:
                c="Scanner smileyInStream =new Scanner(new File ( \" "+ nmfile +"\" )); \n"
                c+= inp(lang,"smileyInStream")
                c+="smileyInStrea.close();\n"
            elif lang==3:
                c="f= open ( \' "+nmfile+"\' ,  \' r \' ) \n"
                c+="f.read()"
                    
        return c                
                    
    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("input is wrong please choose form the list")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return files(langa)
        
    
            
    

#------------------------------addations--------------------------------------------------------------------------------------
def library(langa):
    try:
        if langa==1:
            print("___________________________________________________________________________________________________")
            print("1-Time manipulation(ctime)\n2-Character handling(cctype)\n3-C numerics library(math)\n4-String conversion(cstdlib)\n5-C Strings(cstring)\n6-C library to perform Input/Output operations(cstdio)")
            print("___________________________________________________________________________________________________")
            lib=int(input("choose library you need"))

            if lib==1:
                c="#include <ctime>"
            elif lib==2:
                c="#include <cctype>"
            elif lib==3:
                c="#include <cmath>"
            elif lib==4:
                c="#include <cstdlib>"    
            elif lib==5:
                c="#include <cstring>"
            elif lib==6:
                c="#include <cstdio>"
        elif langa==2:
            print("______________________________________________________________________________________________________")
            print("1-Time manipulation\n2-Creat arrey list\n3-divide strings\n4-library to perform Input\n5-Exception handling\n6-To use the Random class\n7-collections ")
            print("______________________________________________________________________________________________________")
            lib=int(input("choose library you need"))
            if lib==1:
                c="import java.util.Calendar;\nimport java.util.Date;"
            elif lib==2:
                c="import java.util.ArrayList;"
            elif lib==3:
                c="import java.util.StringTokenizer;"
            elif lib==4:
                c="import java.io.BufferedReader;"   
            elif lib==5:
                c="import java.io.IOException;"
            elif lib==6:
                c="import java.util.Random;"    
            elif lib==7:
                c="import java.util.*;"
        elif langa==3:
             c="It will be ready soon. You can write it manually in free code"

        return c
    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("input is wrong please choose form the list")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return library(langa)

#################################################################################################################################
def resre(langa):
    try:
        print("1-return\n2-break\n3-close block")
        word=int(input(""))
        if word==1:
            c="return "+value("0",2)+" ;\n"
        elif word==2:
            c="break ;\n"
        elif word==3:
            if langa==1 or langa==2:
                c="}\n"
        return c
    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("input is wrong please choose form the list")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return resre(langa)

################################################################################################################################        
def add(langa):
    try:
        control=0
        cd=""
        ccd=""
        print("1-libraries\n2-reserved words")
        ad=int(input(""))
        if ad==1:
            ccd=library(langa)
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd=library(langa) 
                else:
                    cd=ccd
                    control=1     
        elif ad==2:
            ccd= resre(langa)
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd= resre(langa) 
                else:
                    cd=ccd
                    control=1
        else:
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("input is wrong please choose form the list")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                return resre(langa)
        return cd
    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("input is wrong please choose form the list")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return add(langa)

              
#---------------------------------------------------------------------------------------------------------------------------
def chooser(a):
    try:
        control=0
        ccd=""
        cod=""
        if a==1:
            var=""
            print("if it more than varible in the same type enter them in one varible in form a,b,c,....")
            no=int(input("number of varible"))
            for i in range (0,no):
                control=0
                var=varible(langa,1,"varible"+str(i+1))+"\n"
                while control==0:
                    print(var)
                    print("1-Edit code\n2-finish")
                    t=contr()
                    if t==1:
                        var=varible(langa,1,"varible"+str(i+1))
                    else:
                        ccd=ccd+var+"\n"
                        print(ccd)
                        control=1
            cod=ccd            
        elif a==2:
            if langa==1:
                ccd=inp(langa,"cin")
            elif langa==2 or langa==3 :
                ccd=inp(langa,"new Scanner(System.in)")
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd=inp(langa) 
                else:
                    cod=ccd
                    control=1
        elif a==3:
            if langa==1:
                ccd=out(langa,"cout")
            elif langa==2 :
                ccd=out(langa,"System.out")
            elif langa==3 :
                ccd=out(langa,"println")
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd=out(langa) 
                else:
                    cod=ccd
                    control=1       
        elif a==4:
            cod=loop(langa) 
        elif a==5:
            cod=cond(langa)       
        elif a==6:
            ccd=func(langa)
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd=func(langa) 
                else:
                    cod=ccd
                    control=1
        elif a==7:
            ccd=files(langa)
            while control==0:
                print(ccd)
                print("1-Edit code\n2-finish")
                t=contr()
                if t==1:
                    ccd=files(langa) 
                else:
                    cod=ccd
                    control=1
            
        elif a==8:
            print("enter your free code")
            cod=input("")
        elif a==9:
             cod=add(langa) 
        elif a==10 :
            if langa==1:
                cod="int main (){ "    
            elif langa==2:
                clas=input("enter the name of main class : ")
                cod="public class "+clas+" {\npublic static void main(String[] args) {"     
                      
        else :
            more(code)
        return cod
    except:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        print("input is wrong please choose form the list")
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return chooser(a)

    
#-------------------------------------------------------------------------------------------------------------------------
def start(code):
    mycd=""
    print("1-varible\n2-input\n3-output \n4-looping \n5-condation\n6-function\n7-files\n8-free code\n9-addation words " )
    if langa==1 or langa==2 :
        print("10-add main function")
    print("______________________________________________________________________________")
    a=int(input(""))
    print("______________________________________________________________________________")
  
    mycd=chooser(a)
    print("______________________________________________________________________________")
    print(mycd)
    print("______________________________________________________________________________")
  
    print("do you want to add it to your code\n1-yes\n2-no")
    x=int(input(""))
    print("______________________________________________________________________________")
  
    if x==1:
        code+=mycd+"\n"
    else:
        mycd=""
    return code    
#----------------------------------------------------------------------------------------------------------------
def more (code):
    flag=0
    while flag==0:
        print("______________________________________________________________________________")
  
        print("can i help you more\n1-continue\n2-show code\n3-delete code\n4-exit")
        print("______________________________________________________________________________")
  
        decide=int(input(""))
        if decide==1:
            code=start(code)
        elif decide==2:
            print("______________________________________________________________________________")
  
            print(code)
            print("______________________________________________________________________________")
  
        elif decide==3:
            code=""
            if langa==1:
                code+="#include<iostream> \nusing namespace std;\n"
            elif langa==2:
                pack=input("enter the name of package : ")
                code+="package com.mycompany."+pack+" ;\nimport java.util.Scanner ;\n"
        elif decide==4:
            print("thank you")  
            flag=1
        else:
            print("please choose form chooices")
            
#main start form here
code=""
if langa==1:
    code+="#include<iostream> \nusing namespace std;\n"
elif langa==2:
    pack=input("enter the name of package : ")
    code+="package com.mycompany."+pack+" ;\nimport java.util.Scanner ;\n"
print("______________________________________________________________________________")
print("now... what do you want to do??\n")
print("______________________________________________________________________________")

code=start(code)+"\n"
more(code)