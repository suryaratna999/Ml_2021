import random 
from datetime import datetime
def chatbot():
    print("hello Iam State info bot I will help you for finding state details ")
def greetings():
    responses=["May i know your name"," what is your name"] 
    print(random.choice(responses))
def get_time():
    current_time=datetime.now().hour
    time="gud mrng"
    if(current_time<12):
        time="gud mrng" 
    elif(current_time>12 and current_time<17):
        time="gud afternoon" 
    elif(current_time>17 and current_time>22):
        time="it's late"
    return(time)
def welcome(name):
    message=["nice to meet you "]
    print( f"{get_time()},{random.choice(message)}") 
def show_menu():
    print("1.state info")
    print("2.date and time")
    print("3. enter calculations")
    print("4.end the chat")
    print("---------------------")
    try:
        return(int(input("enter ur choice[1-4]")))
    except:
        print("enter choice from 1,2,3") 
        return(0)
def evu_exp():
    expr=input("enter exp") 
    try:
        print("result=",eval(expr))
    except Exception as e:
        print(str(e))

def menu_1(place):
    print("1.Andhra Pradesh")
    print("2.Telangana")
    print("3.Assam")
    print("4.chhattisgarh")
    print("5.Bihar")
    print("6.Goa")
    print("7.Gujarat")
    print("8.Haryana")
    print("9.HimachalPradesh")
    print("10.Jammu&kashmir")
    print("11.Jharkhand")
    print("12.Karnataka")
    print("13.Kerela")
    print("14.Maharastra")
    print("15.Manipur")
    print("16.MadhyaPradesh")
    print("17.Meghalaya")
    print("18.Mizoram")
    print("19.Nagaland")
    print("20.Odisha")
    print("21.Punjab")
    print("22.Rajasthan")
    print("23.Sikkim")
    print("24.Tripura")
    print("25.UttarPradesh")
    print("26.West Bengal")
    print("27.Uttarakhand")
    print("28.ArunachalPradesh")
    print("..............")

def menu(state):
    print("**********")
    if(state=="1"):
        print("state:Andhra pradesh","AP CM: Y S Jaganmohan Reddy ","Governor: Biswabhusan Harichandan","Capital: Amaravati","No.of.disticts: 13","Famous Dance: Kuchipudi","Covid Active case: 40047",sep="\n")
    elif(state=="2"):
        print("state:Telangana","TS CM: K. Chandrashekar Rao","Governor: Tamilisai Soundararajan","Capital: Hyderabad","No.of.disticts: 31","Famous Dance: Gusadi ","Covid Active case: 23203",sep="\n")
    elif(state=="3"):
        print("state:Assam","Assam CM: Sarbananda Sonowal","Governor: Jagdish Mukhi","Capital: Dispur","No.of.disticts: 34","Famous Dance: Bihu ","Covid Active case: 28804",sep="\n")
    elif(state=="4"):
        print("state:chhattisgarh","CM: Bhupesh Baghel","Governor: Anusuiya Uikey","Capital: Raipur","No.of.disticts: 28","Famous Dance:  Folk dance","Covid Active case: 433",sep="\n")
    elif(state=="5"):
        print("state:Bihar","CM: Nitish Kumar","Governor: Phagu chauhan","Capital: patna","No.of.disticts: 38","Famous Dance:  Bidesia","Covid Active case: 20922 ",sep="\n")
    elif(state=="6"):
        print("state:Goa","CM: Pramod Pandurag Sawant","Governor: Bhagat Singh Koshyari","Capital: panaji","No.of.disticts: 2","Famous Dance:  Fugdi","Covid Active case: 5423 ",sep="\n")
    elif(state=="7"):
        print("state:Gujarat","CM: Vijay Rupani","Governor: Acharya Devvrat","Capital: Ahmedabad","No.of.disticts: 33","Famous Dance:  Garba","Covid Active case: 14782 ",sep="\n")
    elif(state=="8"):
        print("state:Haryana","CM: Monohar Lal Khattar","Governor: Satyadev Narayan Arya","Capital: Chandigarh","No.of.disticts: 22","Famous Dance:  naach","Covid Active case: 18185 ",sep="\n")
    elif(state=="9"):
        print("state:Himachal Pradesh","CM: Jai Ram Thakur","Governor: bandaru Dattatreya","Capital: Shimla","No.of.disticts: 12","Famous Dance:  Nati","Covid Active case: 3161",sep="\n")
    elif(state=="10"):
        print("state:Jammu&kashmir","CM: Farooq Abdullah","Governor: Manoj Sinha","Capital: Srinaga","No.of.disticts: 20","Famous Dance: Rouf Dance","Covid Active case: 54267 ",sep="\n")
    elif(state=="11"):
        print("state:Jharkhand","CM: Hemant Soren","Governor: Draupadi Murmu","Capital: ranchi","No.of.disticts: 24","Famous Dance: Jhumair","Covid Active case: 8819",sep="\n")
    elif(state=="12"):
        print("state:Kharnataka","CM: B.S.Yediyurappa","Governor: Vajubhai vala","Capital: Mysore","No.of.disticts: 30","Famous Dance: Dollu Kunitha","Covid Active case:113557 ",sep="\n")
    elif(state=="13"):
        print("state:Kerela","CM: Piaarayi Vijayan","Governor: Arif Mohammad Khan","Capital: Thiruvananthapuram","No.of.disticts: 14","Famous Dance: Kathakali","Covid Active case: 67061",sep="\n")
    elif(state=="14"):
        print("state:Maharastra","CM: Uddhav","Governor: Bhagat Siggh Koshyari","Capital: Mumbai","No.of.disticts: 36","Famous Dance: Lavani","Covid Active case:23010 ",sep="\n")
    elif(state=="15"):
        print("state:Manipur","CM: N.Biven Singh","Governor: Najma Heptulla","Capital: Imphal","No.of.disticts: 16","Famous Dance: Jagoi","Covid Active case: 714",sep="\n")
    elif(state=="16"):
        print("state:MadhyaPradesh","CM: Shivraj Singh Choham","Governor: Lalji Tandon","Capital: Bhopal","No.of.disticts: 52","Famous Dance: Shikha Goyal","Covid Active case: 18519",sep="\n")
    elif(state=="17"):
        print("state:Meghalaya","CM: Conrad Sangma","Governor: satya Pal Malik","Capital: Shillong","No.of.disticts: 11","Famous Dance: Nongkrem","Covid Active case: 1193",sep="\n")
    elif(state=="18"):
        print("state:Mizoram","CM: zoramthanga","Governor: P.S.Sreedharan Pillai","Capital: AiZawl","No.of.disticts: 11","Famous Dance: Bamboo dance","Covid Active case: 270",sep="\n")
    elif(state=="19"):
        print("state:Nagaland","CM: Neiphiu Rio","Governor: RN Ravi","Capital: Kohima","No.of.disticts: 12","Famous Dance: War dance","Covid Active case:1221 ",sep="\n")
    elif(state=="20"):
        print("state:Odisha","CM: Naveen Patnaik","Governor: Ganesh Lal","Capital: Bhubaneswar","No.of.disticts: 30","Famous Dance: Ghumura","Covid Active case: 26891",sep="\n")
    elif(state=="21"):
        print("state:Punjab","CM: Amarinder Singh","Governor: V.P.Singh Badnore","Capital: Chandigarh","No.of.disticts: 22","Famous Dance: Bhangra","Covid Active case: 11982",sep="\n")
    elif(state=="22"):
        print("state:Rajasthan","CM: Ashok Gehlot","Governor: Kalraj Mishra","Capital: Jaipur","No.of.disticts: 33","Famous Dance: Ghoomar","Covid Active case: 3219",sep="\n")
    elif(state=="23"):
        print("state:Sikkim","CM: Prem Singh Tamang","Governor: Ganga Prasad ","Capital: Gangtok","No.of.disticts: 4","Famous Dance: Maruni","Covid Active case: 344",sep="\n")
    elif(state=="24"):
        print("state:Tamilnadu","CM: K.Palaniswamy","Governor: Banwarilal","Capital: Chennai","No.of.disticts: 38","Famous Dance: Bharatanatyam","Covid Active case: 57968",sep="\n")
    elif(state=="25"):
        print("state:Tripura","CM: Bipal Kumar Deb","Governor: Ramesh Bias","Capital: Agartala","No.of.disticts: 4","Famous Dance: Hozagiri","Covid Active case: 3314",sep="\n")
    elif(state=="26"):
        print("state:Uttarpradesh","CM: Yogi Adityanath","Governor: Anandiben Patel","Capital: Lucknow","No.of.disticts: 75","Famous Dance: Kathak","Covid Active case:45024 ",sep="\n")
    elif(state=="27"):
        print("state:West Bengal","CM: Mamata Banerjee","Governor: Jagdeep Dhankhar","Capital: Kolkata","No.of.disticts: 23","Famous Dance: Chhau dance","Covid Active case:27299",sep="\n")
    elif(state=="28"):
        print("state:Uttarakhand","CM: Trivendra Singh Rawat","Governor: Baby Rani Maurya","Capital: Gairsain","No.of.disticts: 13","Famous Dance: Chholiya","Covid Active case: 860",sep="\n")
    elif(state=="29"):
        print("state:ArunachalPradesh","CM: Pema Khandu","Governor: B.D.Mishra","Capital: Itanagar","No.of.disticts: 25","Famous Dance: Buiya","Covid Active case: 88",sep="\n")
    else:
        print("Something Went Wrong")
    print("**********")
        

def bot():
    chatbot()
    greetings() 
    name = input()
    welcome(name)
    print("Good to see you here "+ str(name)+"..." 
    " Lets Have some Fun ....!  "+
         "Choose one to proceed further" )
    choice=show_menu()
    while choice!=4:
        if choice==1:
            place = ""
            menu_1(place)
            state = input("Plese enter state serial number from above to know more about That state : ")
            menu(state)
        elif choice==2:
            print(str(datetime.now()))
        elif choice==3:
            evu_exp()
        else:
            print("Something went wrong")
        choice=show_menu()
bot()