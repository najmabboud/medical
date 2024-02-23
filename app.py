

#قسم المكاتب

from pywebio.platform.flask import webio_view
from flask import Flask
import pywebio
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *
import mysql.connector as mysql
import smtplib
import email_to
#================================================= 
app = Flask(__name__)
pywebio.config(title="خدمات طبية",)

senderemail=''
senderpassword=''




#انشاء حساب مستخدم
def great_account():
    
    put_row([
        put_link("عودة",url="/account").style('color:red;'),
        
    ])
    
    datagreat=input_group("ادخل البيانات التالية",[
            
            input("الاسم الكامل",name='fnameg',required=True),
            input("الايميل ",name='emailg',required=True),
            input("كلمة المرور",name='pasg',required=True)
            
            
        ])



    e1g=datagreat['fnameg']
    e2g=datagreat['emailg']
    e3g=datagreat['pasg']


    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

    cur = con.cursor()
    cur.execute("SELECT DISTINCT email FROM users WHERE email=%s   ORDER BY email ASC", (e2g,))
    outg = (cur.fetchall())
    con.commit()
    con .close()
    
    outg11=[data[0]for data in outg]
    if outg11==[] :
            


        
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

        cur = con.cursor()
        query = 'INSERT INTO `users`(`fullname`, `email` ,`password`,`passwordt` ) VALUES(%s,%s,%s,%s)'
        val = (e1g,e2g,e3g," ")
        cur.execute(query, val)   
        con.commit()
        con.close()
        popup(title=" مرحبا بك😃",content="تمت اضافة حسابك")
        
        
        server = email_to.EmailServer('smtp.gmail.com',587,senderemail,senderpassword)
        message=server.message()
        message.add("تم انشاء حسابك على موقع   MED-N")
        message.style='h1{color:blue}'
        message.send(e2g,'مرحبا')
        
        


    else:
        popup("عذرا",content="الحساب موجود مسبقا اذا اردت انشاء حساب جديد يرجى حذف الحساب القديم")
        

    
    
    
    
    
#انشاء حساب طبيب
def great_account_d():
    put_row([
        put_link("عودة",url="/account").style('color:red;'),
        
    ])
    
    datagd=input_group("ادخل البيانات التالية",[
            
        input("الاسم الكامل",name='fnamegd',required=True),
        input("الايميل ",name='emailgd',required=True),
        input(" كلمة مرور التطبيق",name='pas1gd',required=True),
        input(" كلمة مرور الخدمات",name='pas2gd',required=True)
            
            
        ])



    e1gd=datagd['fnamegd']
    e2gd=datagd['emailgd']
    e3gd=datagd['pas1gd']
    e4gd=datagd['pas2gd']
        

    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

    cur = con.cursor()
    cur.execute("SELECT DISTINCT email FROM users WHERE email=%s   ORDER BY email ASC", (e2gd,))
    outgd = (cur.fetchall())
    con.commit()
    con.close()
    
    outgd1=[data[0] for data in outgd]
    print(outgd1)
    if (outgd1==[]) :
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

        cur = con.cursor()
        query = 'INSERT INTO `users`(`fullname`, `email` ,`password`,`passwordt` ) VALUES(%s,%s,%s,%s)'
        val = (e1gd,e2gd,e3gd,e4gd)
        cur.execute(query, val)   
        con.commit()
        con.close()
        popup(title="مرحبا بك",content="تمت اضافة حسابك")
        
        server = email_to.EmailServer('smtp.gmail.com',587,senderemail,senderpassword)
        message=server.message()
        message.add("تم انشاء حسابك على موقع   MED-N")
        message.style='h1{color:blue}'
        message.send(e2gd,'مرحبا')
        
    else:
        popup("عذرا",content="الحساب موجود مسبقا اذا اردت انشاء حساب جديد يرجى حذف الحساب القديم")
        
        




#حذف حساب
def deltacc():
    put_link("عودة",url="/account").style('color:red;')
    
    put_html('<style> .pe{color:red;} </style>')
    put_html('<center><p class=pe>عند حذف حسابك سيتم حذف جميع بياناتك على الموقع بما فيها مواعيدك وما الى ذلك</p></center>')
    emda=input("الايميل",required=True)
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

    cur = con.cursor()
    cur.execute("SELECT DISTINCT email FROM users WHERE email=%s   ORDER BY email ASC", (emda,))
    outdelac = (cur.fetchall())
    con.commit()
    con.close()
    
    outdelac1=[data[0] for data in outdelac]
    if outdelac1==[]:
        popup("عذرا",content="الايميل غير موجود")
        accou()
    else:
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

        cur = con.cursor()
        cur.execute('DELETE FROM `users` WHERE email=%s',(emda,))
        con.commit()
        con.close()
        
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

        cur = con.cursor()
        cur.execute('DELETE FROM `doctors` WHERE email=%s',(emda,))
        con.commit()
        con.close()
        
        
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

        cur = con.cursor()
        cur.execute('DELETE FROM `dectorstimes` WHERE dectoremail=%s',(emda,))
        con.commit()
        con.close()
        
        
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

        cur = con.cursor()
        cur.execute('DELETE FROM `dectorstimes` WHERE customeremail=%s',(emda,))
        con.commit()
        con.close()
        
        
        popup("",content="تم حذف حسابك بنجاح")
        
        server = email_to.EmailServer('smtp.gmail.com',587,senderemail,senderpassword)
        message=server.message()
        message.add("تم حذف حسابك على موقع   MED-N")
        message.style='h1{color:blue}'
        message.send(emda,'مرحبا')
        
        
        
        

#انشاء حساب    
def accou():
 
    put_html('<style> @keyframes ani{0% {color:blue;} 30% {color:red;} 70%{color:green;} 100%{color:red;}}  .p1{animation:ani 2s linear infinite ; font-size:70px; text-shadow:5px 5px 5px white;  border-radius:20px;}</style>')
    put_html('<marquee class=p1>اعدادات الحساب </marquee>')
    put_html('<center><h2>  قم بانشاء حسابك الخاص في حال كانت هذه زيارتك الاولى .بالنسبة للاطباء يمكنكم بالاضافة الى ذلك انشاء كلمة مرور من اجل خصوصية التحكم بالمواعيد من خلال الروابط الموجودة في الاسفل</h2><center>')
    img=open('8.png','rb').read()
    put_image(img,width='100%').style('height:500px; ' )

   
   
        
    
    put_html('<center><a  href=/ > الصفحة الرئيسيه</a> </center>')
    put_html('<center><a href=/gu >انشاء حساب مستخدم</a> </center>')
    put_html('<center><a class=aa href=/gd > انشاء حساب طبيب </a> </center>')
    put_html('<center><a class=aa href=/da > حذف حساب </a> </center>')
    


  
 
 
 



# اضافة البيانات
def pas3():
        
        
        
        
        
    put_link("عودة",url="/doctor").style('color:red;') 
    infpas=input_group("ادخل البيانات ",[
            
        input("ايميلك",name="emdpas",required=True),
        input("كلمة المرور",name="padpas",required=True)
            
        
            
                                            
                                            ])
        
    
        
            
    
    empas=infpas['emdpas']
    papas=infpas['padpas']
    
    
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

    cur = con.cursor()
        
    cur.execute("SELECT DISTINCT email FROM users WHERE email=%s   ORDER BY email ASC", (empas,))
    out12 = (cur.fetchall())
    con.commit()
    con.close() 
    
    out123=[data[0] for data in out12]
    
    if out123==[]:
        popup("عذرا",content="الايميل غير موجود")
    else:
        
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

        cur = con.cursor()
           
        cur.execute("SELECT DISTINCT passwordt FROM users WHERE email=%s   ORDER BY email ASC", (empas,))
        out = (cur.fetchall())
        con.commit() 
        con.close() 
        
        out1=[data[0] for data in out]
        
        if (papas==out1[0]):
            
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

            cur = con.cursor()
            
            cur.execute("SELECT DISTINCT email FROM doctors WHERE email=%s   ORDER BY email ASC", (empas,))
            outq = (cur.fetchall())
            con.commit()
            con.close()  
            
            outq1=[data[0] for data in outq]
            if outq1==[]:
                put_link("عودة",url="/doctor").style('color:red;')
                day=["الاحد-","الاثنين-","الثلاثاء-","الاربعاء-","الخميس-","الجمعه-","السبت"]
                data=input_group("ادخل البيانات ",[
                    
                input("الاسم الكامل",name="flname",required=True),
                input("الاختصاص",name="work",required=True),
                    
                checkbox("ايام المشفى",options=day,inline=True,name="hosp",required=True),
                checkbox("ايام العيادة",options=day,inline=True,name="wo",required=True),
                textarea("ساعات الدوام ",name="hwork",required=True)
                    
                                                    
                                                    ])
                
                e1=data['flname']
                e2=data['work']
                    
                e3=empas
                e4=str(data['hosp'])
                e5=str(data['wo'])
                e6=str(data['hwork'])
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')

                cur = con.cursor()
                query = 'INSERT INTO `doctors`(`fullname`, `work`, `email`, `dayinhospital`, `dayinhome`, `hourofwork`) VALUES(%s,%s,%s,%s,%s,%s)'
                val = (e1,e2,e3,e4,e5,e6)
                cur.execute(query, val)
                con.commit()
                con.close()
                popup("بيانات الطبيب",content="تمت اضافة بياناتك بنجاح")
                
            else:
                popup("عذرا",content="لقد قمت باضافة بياناتك سابقا ")
                
        else:
            popup("كلمة المرور خاطئه",content="تأكد من حسابك وكلمة مرورك")
            
                
            
#تعديل البيانات    
def pas2():
        
        

        
    put_link("عودة",url="/doctor").style('color:red;')   
    infpas2=input_group("ادخل البيانات ",[
            
        input("ايميلك",name="emdpas2",required=True),
        input("كلمة المرور",name="padpas2",required=True)
            
        
            
                                            
                                            ])
    
    
    empas2=infpas2['emdpas2']
    papas2=infpas2['padpas2']
    
    
    
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
        
    cur.execute("SELECT DISTINCT email FROM doctors WHERE email=%s   ORDER BY email ASC", (empas2,))
    out124 = (cur.fetchall())
    con.commit() 
    con.close() 
    
    out1234=[data[0] for data in out124]
    
    if out1234==[]:
        popup("عذرا",content="الايميل غير موجود")
    else:
        
    
    
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        cur = con.cursor()
            
        cur.execute("SELECT DISTINCT passwordt FROM users WHERE email=%s   ORDER BY email ASC", (empas2,))
        out = (cur.fetchall())
        con.commit()
        con.close()
        
        outr=[data[0] for data in out]   
            
        if (papas2==outr[0]):
              
            xx=["الاسم الكامل ","الاختصاص","ايام المشفى","ايام العيادة","ساعات العمل"]
            s=select("ما الذي ترغب بتعديله",options=xx)
            
            
            if s=="الاسم الكامل ":
                    
                p2=input("ادخل الاسم الجديد",required=True)
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                cur = con.cursor()
                cur.execute('UPDATE `doctors` SET fullname=%s WHERE email=%s ', (p2, empas2))
                con.commit()
                con.close()
                popup("",content="   تم تعديل اسمك بنجاح")
                
                
        
                    
            elif s=="الاختصاص":
                    
                p211=input("ادخل  الاختصاص الجديد",required=True)
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                cur = con.cursor()
                cur.execute('UPDATE `doctors` SET work=%s WHERE email=%s ', (p211, empas2))
                con.commit()
                con.close()
                popup("",content="   تم تعديل الاختصاص بنجاح")
                
                    
            elif s=="ايام المشفى":
                    
                    
                day2=["الاحد-","الاثنين-","الثلاثاء-","الاربعاء-","الخميس-","الجمعه-","السبت"]
                p24=checkbox("ايام المشفى الجديدة",options=day2,inline=True,required=True)
                p224=str(p24)
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                cur = con.cursor()
                cur.execute('UPDATE `doctors` SET dayinhospital=%s WHERE email=%s ', (p224, empas2))
                con.commit()
                con.close()
                popup("",content="   تم تعديل ايام المشفى بنجاح")
                
            elif s=="ايام العيادة":
                    
                day3=["الاحد-","الاثنين-","الثلاثاء-","الاربعاء-","الخميس-","الجمعه-","السبت"]
                p35=checkbox("ايام العيادة الجديدة",options=day3,inline=True,required=True)
                p335=str(p35)
                    
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')    
                cur = con.cursor()
                cur.execute('UPDATE `doctors` SET dayinhome=%s WHERE email=%s ', (p335, empas2))
                con.commit()
                con.close()
                popup("",content="   تم تعديل ايام العيادة بنجاح")
                
            elif s=="ساعات العمل":
                    
                p226=textarea("ساعات الدوام ",required=True)
                p2226=str(p226)
                    
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')   
                cur = con.cursor()
                cur.execute('UPDATE `doctors` SET hourofwork=%s WHERE email=%s ', (p2226, empas2))
                con.commit()
                con.close()
                popup("",content="   تم تعديل ساعات العمل بنجاح")
                
        else:
            popup("كلمة المرور خاطئه",content="تأكد من حسابك وكلمة مرورك")
            





#المواعيد
def sel():
        
        
        
            
        
        
    put_link("عودة",url="/doctor").style('color:red;')   
    infsel=input_group("ادخل البيانات ",[
            
        input("ايميلك",name="emsel",required=True),
        input("كلمة المرور",name="pasel",required=True)
            
        
            
                                            
                                            ])
    
    
    emsel=infsel['emsel']
    pasel=infsel['pasel']
    
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT email FROM users WHERE email=%s   ORDER BY email ASC", (emsel,))
    outsele = (cur.fetchall())
    con.commit()
    
    con.close()
    
    outsele1=[data[0] for data in outsele]
    
    if outsele1==[]:
        popup("عذرا ",content="الايميل غير موجود")
    else:
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        cur = con.cursor()
                
        cur.execute("SELECT DISTINCT passwordt FROM users WHERE email=%s   ORDER BY email ASC", (emsel,))
        outpa = (cur.fetchall())
        con.commit()
        con.close()
        outpa1=[data[0] for data in outpa]
          
        if (pasel==outpa1[0]):   
        
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            cur = con.cursor()
            cur.execute("SELECT DISTINCT dectoremail FROM dectorstimes WHERE dectoremail=%s   ORDER BY dectoremail ASC", (emsel,))
            outsel = (cur.fetchall())
            con.commit()
            con.close()
            
            outsel1=[data[0] for data in outsel]
            
            if outsel1==[]:
                popup("",content="ليس لديك مواعيد بعد☺")
            
            else:
            
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                cur = con.cursor()
                cur.execute("SELECT DISTINCT date FROM dectorstimes WHERE dectoremail=%s   ORDER BY date ASC", (emsel,))
                out=cur.fetchall()
                k=[date[0] for date in out]
                con.commit()
                con.close()
                
                l=select("اختر التاريخ",options=k)
                    
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                cur = con.cursor()
                cur.execute("SELECT DISTINCT time FROM dectorstimes WHERE dectoremail=%s AND date=%s   ORDER BY date ASC", (emsel,l,))
                ou2=cur.fetchall()
                con.commit()
                con.close()
                
                    
                    
                put_text(l).style('text-align:center;')
                ou22=[dat[0] for dat in  ou2]
                    
                ch=checkbox("اختر المواعيد التي ترغب بقبولها لهذا التاريخ"+l,options=ou22)
                for chh in ch :
                    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                    cur = con.cursor()
                        
                    cur.execute("SELECT fullname  FROM doctors WHERE email=%s ", (emsel,))
                    
                    con.close()  
                    
                        
                    fulln=cur.fetchall()
                    fulln1=[dat[0] for dat in fulln]
                    fulln10=fulln1[0]
                
                    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                    cur = con.cursor()
                        
                    cur.execute("SELECT customeremail  FROM dectorstimes WHERE dectoremail=%s AND date=%s AND time=%s ", (emsel,l,chh))
                     
                    con.close() 
                    
                        
                    custem=cur.fetchall()
                    custem1=[dat[0] for dat in custem]
                    
                    custem11=custem1[0]
                        
                    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                    cur = con.cursor()
                    cur.execute("DELETE  FROM dectorstimes WHERE dectoremail=%s  AND  date=%s AND time=%s ORDER BY date ASC", (emsel,l,chh))
                    
                    con.close()
                    
                    
                    ms="تمت الموافقة على موعدك لدى الطبيب"
                    mss=ms+fulln10
                    
                    server = email_to.EmailServer('smtp.gmail.com',587,senderemail,senderpassword)
                    message=server.message()
                    message.add(mss)
                    message.add(l)
                    message.style='h1{color:blue}'
                    message.send(custem11,'مرحبا')       
                    popup("",content="😃تم ارسال الموافقه")
                    
                    
                con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                cur = con.cursor()
                cur.execute("SELECT DISTINCT time FROM dectorstimes WHERE dectoremail=%s AND date=%s   ORDER BY date ASC", (emsel,l,))
                ou23=cur.fetchall()
                
                con.close()
                
                ou233=[dat[0] for dat in ou23]
                ch23=checkbox("اختر المواعيد التي ترغب برفضها لهذا التاريخ"+l,options=ou233)
                for chh28 in ch23 :
                
                    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                    cur = con.cursor()
                        
                    cur.execute("SELECT fullname  FROM doctors WHERE email=%s ", (emsel,))
                    
                    con.close()   
                    
                        
                    fulln2=cur.fetchall()
                    fulln12=[dat[0] for dat in fulln2]
                    fulln120=fulln12[0]
                        
                    
                        
                    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
                    cur = con.cursor()
                        
                    cur.execute("SELECT customeremail  FROM dectorstimes WHERE dectoremail=%s AND date=%s AND time=%s ", (emsel,l,chh28))
                    
                    con.close()
                  
                    
                        
                    custem2=cur.fetchall()
                    custem12=[dat[0] for dat in custem2]
                    custem120=custem12[0]
                    
                        
                    
                    cur = con.cursor()
                    cur.execute("DELETE  FROM dectorstimes WHERE dectoremail=%s  AND  date=%s AND time=%s ORDER BY date ASC", (emsel,l,chh))
                    
                    con.close()
                    
                        
                    ref="تم رفض موعدك لدى الطبيب" 
                    ref1=ref+fulln120
                    server = email_to.EmailServer('smtp.gmail.com',587,senderemail,senderpassword)
                    message=server.message()
                    message.add(ref1)
                    message.add(l)
                    message.style='h1{color:blue}'
                    message.send(custem120,'مرحبا')       
                    
                    
                      
                        
                    popup("",content="😃تم ارسال الرفض") 
                    
                        
                            
                        
                    
                
                    
                    
                
        else:
            popup("",content="كلمة المرور خاطئه")
            



#خدمات الطبيب   
def doctor():
    
    
    
    put_html('<style> @keyframes ani{0% {color:blue;} 30% {color:red;} 70%{color:green;} 100%{color:red;}}  .p1{animation:ani 2s linear infinite ; font-size:70px; text-shadow:5px 5px 5px white; border-radius:20px;}</style>')
    put_html('<marquee class=p1> طبيب </marquee>')
    
    put_html('<center><h2 >   قم باضافة بيانات العمل الخاص بك لكي يتمكن المرضى من التواصل معك والاطلاع على ايام عملك وما الى ذلك من خلال الروابط في الاسفل  </h2><center>')

    img=open('8.png','rb').read()
    put_image(img,width='100%').style('height:500px; ' )
    
    
    
    
    put_html('<center><a  href=/ > الصفحة الرئيسيه</a> </center>')
    put_html('<center><a href=/pas3> اضافة بياناتي </a> </center>')
    put_html('<center><a class=aa href=/pas2 > تعديل بياناتي   </a> </center>')
    put_html('<center><a class=aa href=/sel>  المواعيد </a> </center>')


    
 
#حجز موعد
def page3_2():
    put_link("عودة",url="/pation").style('color:red;')
    a=input("اسم الطبيب",required=True)
        
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT work FROM doctors WHERE fullname=%s   ORDER BY work ASC", (a,))
    dates = cur.fetchall()
    con.commit()
    con.close()
    
    h=[date[0] for date in dates]
        
    b=select("الاختصاص",options=h,required=True)
    
        
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT email FROM doctors WHERE fullname=%s AND work=%s  ORDER BY work ASC", (a,b))
    dates2 = cur.fetchall()
    h2=[date[0] for date in dates2]
    con.commit()
    con.close()
    
    c=select("ايميل الطبيب",options=h2,required=True)
    
        
    d=input("ايميلك",required=True)
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT email FROM users WHERE email=%s  ", (d,))
    m = cur.fetchall()
    con.commit()
    con.close()
    
    
    md=[data[0] for data in m]
    
    if md==[]:
        popup("عذرا",content="ايميلك غير موجود")
    else:
        md0=md[0]
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        cur = con.cursor()
        cur.execute("SELECT DISTINCT password FROM users WHERE email=%s  ", (md0,))
        pm = cur.fetchall()
        con.commit()
        con.close()
         
        pm1=[data[0] for data in pm]
        e=input(" هل هذه كلمة المرور الخاصة بك",required=True,value=pm1)
    
    
        f=input("تاريخ الحجز",type=DATE,required=True)
        
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        cur = con.cursor()
        cur.execute("SELECT  date FROM dectorstimes WHERE customeremail=%s AND dectoremail=%s  ", (md0,c,))
        vm = cur.fetchall()
        con.commit()
        con.close()
        
        u=[dat[0] for dat in vm]
        
        if (f in u):
            popup("",content="لديك حجز سابق بهذا التاريخ")
        
        else:
            
            tim=["6:30","7:00","7:30","8:00","8:30","9:00","9:30","10:00","10:30"]
            
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            cur = con.cursor()
            cur.execute("SELECT  time FROM dectorstimes WHERE date=%s AND dectoremail=%s  ", (f,c,))
            t1 = cur.fetchall()
            con.commit()
            con.close()
            
            t2=[dat[0] for dat in t1]
            
            
            
            tim1=[]

            
            for j in tim:
                if j in t2:
                    print("in")
                else:
                    tim1.append(j)
                        
            g=select("اختر الوقت المتاح للحجز الذي يتناسب مع دوام الطبيب",options=tim1) 
            
            con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
            cur = con.cursor()
            cur.execute('INSERT INTO `dectorstimes` (`dectoremail`, `customeremail`, `date`, `time`) VALUES(%s,%s,%s,%s)', (c,md0,f,g,))
            con.commit()
            con.close()
            
            popup(" ",content= "تم حجز الموعد")
            
              
            
            
            
              
              
        
        
        
#حذف الموعد      
def delt():
    put_link("عودة",url="/pation").style('color:red;')
    a=input("ادخل ايميلك",required=True)
    b=input("اسم الطبيب بالكامل ",required=True)
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT work FROM doctors WHERE fullname=%s   ORDER BY work ASC", (b,))
    ou=cur.fetchall()
    con.commit()
    con.close()
    
    ou1=[da[0] for da in ou]
    c=select("الاختصاص",options=ou1)
        
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT email FROM doctors WHERE fullname=%s AND work=%s  ORDER BY work ASC", (b,c,))
    oue=cur.fetchall()
    con.commit()
    con.close()
    
    oue1=[dat[0] for dat in oue]
        
        
        
    dd=oue1[0]
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT date FROM dectorstimes WHERE dectoremail=%s AND customeremail=%s  ORDER BY date ASC", (dd,a,))
    our=cur.fetchall()
    con.commit()
    con.close()
    
    eur1=[da[0] for da in our]
        
    d=select("اختار التاريخ ",options=eur1)
        
        
        
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT time FROM dectorstimes WHERE dectoremail=%s AND customeremail=%s AND date=%s ORDER BY date ASC", (dd,a,d,))
    ou=cur.fetchall()
    con.commit()
    con.close()
    
    eu11=[da[0] for da in ou]
        
        
        
    def remo():
        r=eu11[0]
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        cur = con.cursor()
        cur.execute('DELETE FROM `dectorstimes` WHERE date=%s AND time=%s', (d,r,))
        con.commit()
        con.close()
        
        popup("",content="تم الغاء الموعد بنجاح")
        clear("a")
        
        
    with use_scope("a"):
        put_text("")  
        put_row([
                put_text(eu11[0]),
                put_button("حذف الموعد",onclick=remo,outline=True,link_style=True)
                
            
                
            ],scope="a")
           
        
            
            
           
        
        
#معلومات الطبيب            
            
def getinfo():
    put_link("عودة",url="/pation").style('color:red;')     
    a1=input("اسم الطبيب",required=True)
        
    con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
    cur = con.cursor()
    cur.execute("SELECT DISTINCT work FROM doctors WHERE fullname=%s   ORDER BY work ASC", (a1,))
    dates = cur.fetchall()
    con.commit()
    con.close()
    
    h1=[date[0] for date in dates]
        
    b1=select("الاختصاص",options=h1,required=True)
 
    xx=[" ايام المشفى "," ايام العيادة "," ساعات العمل"]
    s=select("ما الذي ترغب بالحصول علية",options=xx)
    #
    if s==" ايام المشفى ":
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')
        cur = con.cursor()
        cur.execute('SELECT dayinhospital FROM `doctors` WHERE fullname=%s AND work=%s ',(a1,b1))
        ww=cur.fetchall()
        con.commit()
        con.close()
        www=[dat[0] for dat in ww]
        put_text(a1).style('text-align:right;')
        put_text("ايام المشفى").style('text-align:center;')
        put_text(www[0]).style('text-align:center;')
        
        
        
            
    elif  s==" ايام العيادة ":
                
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')       
        cur = con.cursor()
        cur.execute('SELECT dayinhome FROM `doctors` WHERE fullname=%s AND work=%s ',(a1,b1))
        ww=cur.fetchall()
        www=[dat[0] for dat in ww]
        con.commit()
        con.close()
        put_text(a1).style('text-align:right;')
        put_text("ايام العيادة").style('text-align:center;')
        put_text(www[0]).style('text-align:center;')
        
        
        
        
    else:   
                
        con = mysql.connect(host="btsasdqlxusuqgzvyqxv-mysql.services.clever-cloud.com", user="u5yudvgpvk1rsxdi", password="NWx6wqA0lCL9kxTvDoAy", database='btsasdqlxusuqgzvyqxv')       
        cur = con.cursor()
        cur.execute('SELECT hourofwork FROM `doctors` WHERE fullname=%s AND work=%s ',(a1,b1))
        ww=cur.fetchall()
        con.commit()
        con.close()
        www=[dat[0] for dat in ww]
        put_text(a1).style('text-align:right;')
        put_text("ساعات العمل").style('text-align:center;')
        put_text(www[0]).style('text-align:center;')
        
        
        
             
    
    
#مريض    
def pation ():
   

    
    put_html('<style> @keyframes ani{0% {color:blue;} 30% {color:red;} 70%{color:green;} 100%{color:red;}}  .p1{animation:ani 2s linear infinite ; font-size:70px; text-shadow:5px 5px 5px white;  border-radius:20px;}</style>')
    put_html('<marquee class=p1>مريض  </marquee>')
    
    put_html('<center><h2>احجز موعدك لدى طبيبك </h2><center>')
    put_html('<center><h2>احصل على معلومات طبيبك</h2><center>')
    
    put_html('<style> .h{color:red;}</style>')
    put_html('<center><h2 class=h>ستصلك رسالة على ايميلك بخصوص حالة موعدك ☺</h2><center>')

    
    img=open('8.png','rb').read()
    put_image(img,width='100%',).style('height:500px;  ' )
    
    
    
    put_html('<center><a  href=/ > الصفحة الرئيسيه</a> </center>')
    put_html('<center><a href=/page3_2 >حجز موعد </a> </center>')
    put_html('<center><a class=aa href=/delt > حذف موعد   </a> </center>')
    put_html('<center><a class=aa href=/getinfo >  معلومات الطبيب </a> </center>')
    
    
#الصفحة الرئيسية
def index():
    
    
  
    put_html('<style> @keyframes ani{0% {color:blue;} 30% {color:red;} 70%{color:green;} 100%{color:red;}}  .p1{animation:ani 2s linear infinite ; font-size:70px; text-shadow:5px 5px 5px white; border-radius:20px;}</style>')
    put_html('<marquee class=p1>الخدمات الطبية</marquee>')
    
    put_html('<center><h2 >   يمكن للمرضى من خلال هذا الموقع حجز موعد لدى الطبيب الخاص او الاطلاع على ايام عمله واماكن تواجدة ويمكن للاطباء تنظيم مواعيدهم والتحكم بها بسهولة ويمكن الحصول على هذا الخدمات من خلال الروابط الموجودة في الاسفل</h2><center>')
    
    
    
    img=open('8.png','rb').read()
    put_image(img,width='100%',).style('height:500px;  ' )
    
    
    put_html('<center><p>  طبيب: يمكنك اضافة بيانات العمل الخاصة بك والتحكم بمواعيدك بخصوصيه😃  </p><center>')
    put_html('<center> <p>   مريض : يمكنك حجز موعد لدى طبيبك الخاص 😊  </p></center>')
    put_html('<center><p>اعدادات الحساب : قم بانشاء حسابك الخاص لاستخدام الموقع بشكل أمن😉 </p></center>')
    
    
    put_html('<center><a  href=/doctor > طبيب </a> </center>')
    put_html('<center><a href=/pation> مريض </a> </center>')
    put_html('<center><a class=aa href=/account>  اعدادات الحساب  </a> </center>')
    
    
    
    
    
    




#روابط الصفحات


app.add_url_rule('/','home',webio_view(index),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/pation','pation',webio_view(pation),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/doctor','doctor',webio_view(doctor),
                  methods=['GET','POST','OPTIONS'])


app.add_url_rule('/account','accounts',webio_view(accou),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/pas3','pas3',webio_view(pas3),
                  methods=['GET','POST','OPTIONS'])


app.add_url_rule('/gu','gu',webio_view(great_account),
                  methods=['GET','POST','OPTIONS'])



app.add_url_rule('/gd','gd',webio_view(great_account_d),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/da','da',webio_view(deltacc),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/pas2','pas2',webio_view(pas2),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/sel','sel',webio_view(sel),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/page3_2','page3_2',webio_view(page3_2),
                  methods=['GET','POST','OPTIONS'])
app.add_url_rule('/delt','delt',webio_view(delt),
                  methods=['GET','POST','OPTIONS'])

app.add_url_rule('/getinfo','getinfo',webio_view(getinfo),
                  methods=['GET','POST','OPTIONS'])


#=========================================================

 

if __name__ == "__main__":
    
    app.run()