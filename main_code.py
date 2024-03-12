import pandas as pd

csv_path = r'./Account_data.csv'
df = pd.read_csv(csv_path)

main_csv_path = r'./Main.csv'



def Account() :
  """
  --- User Account ---
  user must create account for their personal details like name,age,adhar no,phone no,E-mail id
  so create account password and it used whenever user try to book ticket
  """
  print('-------------Account--------------')
  print('Fill All Details For Create Account')

  pessenger = []

  ## NAME -- IT MUST BE IN ALPHABETS

  first_name = input("Enter Your first_name : ").strip()
  while first_name.isalpha() == False:
    print("Please Enter Valid Input")
    first_name = input("Enter Your first_name : ").strip()


  middle_name = input("Enter Your middle_name : ").strip()
  while middle_name.isalpha() == False:
    print("Please Enter Valid Input")
    middle_name = input("Enter Your middle_name : ").strip()

  last_name = input("Enter Your last_name : ").strip()
  while last_name.isalpha() == False:
    print("Please Enter Valid Input")
    last_name = input("Enter Your last_name : ").strip()

  name = first_name.title() + " " + middle_name.title() + " " + last_name.title()

  ## GENDER -- M OR F OR OTHER

  print("Plaese Select Your Gender :\n1. Male \n2. Female \n3. Other ")
  gender = input("Select One Option From Above : ")

  while True:
      if gender == '1' or gender == '2' or gender == '3':
          if gender == '1':
              gn = 'Male'
          elif gender == '2':
              gn = 'Female'
          elif gender == '3':
              gn = 'Other'
          break
      else:
          gender = input("Select One Option From Above : ")


  ## AGE -- IT MUST BE WITHIN IN 150 YEARS

  age = input("Plesse Enter Your Age :")
  while age.isdigit() == False or (0 < (int(age)) < 150) == False:
      print("Please Enter Your Valid Age :")
      age = input("Please Enter Your Age :")

  ## PHONE DETAILS -- IT MUST BE IN DIGITS AND HAVE COMPUSARY 10 NUMBERS AND IT'S STARTS WITN 9,8,7,6
  phone_no = input("Enter Your Mobile No : ")
  while True:
      if phone_no.isdigit() and len(phone_no) == 10:
          if phone_no[0] == '9' or phone_no[0] == '8' or phone_no[0] == '7' or phone_no[0] == '6':
              break
          else:
              print("Enter Valid Mobile No")
              phone_no = input("Enter Your Mobile No : ")
      else:
          print("Enter Valid Mobile No")
          phone_no = input("Enter Your Mobile No : ")

  ## ADHAAR -- IT MUST BE IN DIGITS AND DIGITS ARE 12

  adhaar_no = input("Please Enter Your Adhaar No Without Any Space : ")
  while adhaar_no.isdigit() == False or len(adhaar_no)!=12:
     print("Please Enter Your Valid Adhaar No :")
     adhaar_no = input("Please Enter Your Adhaar No Without Any Space : ")


  ## Email_id -- unique id so we use as accound login id

  email_id = input("Plese Enter Your E-mail Id :")
  while "@" and "." not in email_id :
    print("Plese Enter Valid E-mail Id :")
    email_id = input("Plese Enter Your E-mail Id :")

  ## Password -- for login account and book tickets
  PASSWORD = input(
      "Write password you Want (Password must contain at least one symbol,letter and number and also more than 5 words) :")
  special = ['!', '@', '#', '$', '%', '^', '&', '*', '?']
  while True:
      if (any(char in special for char in PASSWORD)) and len(PASSWORD) > 5:
          if (any(char.isdigit() for char in PASSWORD)):
              if (any(char.isalpha() for char in PASSWORD)):
                  print('Password set successfully')
                  break
      else:
          print('plese make strong Password')
          PASSWORD = input("Write password you Want :")

  ddf = pd.DataFrame({'Name':[name],
                      'Gender':[gn],
                      'Age':[age],
                      'Mobile No.':[phone_no],
                      'Adhaar No.':[adhaar_no],
                      'Email ID':[email_id],
                      'PASSWORD':[PASSWORD]})
  ddf.to_csv(csv_path,mode='a',header=False,index=False)


# show train details
def show_train_details():
    Trains = {1: 'Gandhinagar To Surat(Vande Bharat)',
              2: 'Ahmedabad To Veraval(Somanath Express)',
              3: 'Ahmedabad To Mumbai(IRCTC Tejas Exp.)',
              4: 'Ahmedabad To Delhi(Ashram Express)',
              5: 'Veraval To Dwarka(SMNH OKHA Exp.)'}


    for key, value in Trains.items():
        print(f'Train {key} : {value}')
    print()

# Booking Tickets
def booking():

    import datetime

    date_input = input('Enter date for journey, enter in this format (yyyy-mm-dd): ')

    while True:
            try:
                year, month, day = map(int, date_input.split('-'))
                input_date = datetime.date(year, month, day)
                current_date = datetime.date.today()

                if input_date <= current_date:
                    print('Please enter a future date.')
                elif month == 2 and day > 29 and (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    print('Please enter a valid date for February in leap years.')
                elif month == 2 and day > 28 and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
                    print('Please enter a valid date for February in non-leap years.')
                else:
                    # print('Date is valid.')
                    break
            except ValueError:
                print('Please enter a valid date in the specified format.')

            date_input = input('Enter date for the journey, enter in this format (yyyy-mm-dd): ')




    import pandas as pd

    d = pd.Timestamp(date_input)
    day = d.day_name()



    Trains = { 1 : 'Gandhinagar To Surat(Tapi Express)',
             2 : 'Ahmedabad To Veraval(Somanath Express)',
             3 : 'Ahmedabad To Mumbai(IRCTC Tejas Exp.)',
             4 : 'Ahmedabad To Delhi(Ashram Express)',
             5 : 'Veraval To Dwarka(SMNH OKHA Exp.)'}


    Train_1 = ['Sun','Mon','Wed','Fri','Sat']
    Train_3 = ['Sun','Tue','Fri']
    All_days = ['Sun','Mon','Tue','Wed','Thu','Fri','Sat']

    T_D = [[20902,'Train 1 : Gandhinagar To Surat(Tapi Express)','14: 05 - 17:13',250,120,800,Train_1],
         [22957,'Train 2 : Ahmedabad To Veraval(Somanath Express)','22:10 - 06:00',320,200,990,All_days],
         [82902,'Train 3 : Ahmedabad To Mumbai(IRCTC Tejas Exp.)','06:40 - 13:05',345,220,1100,Train_3],
         [12915,'Train 4 : Ahmedabad To Delhi(Ashram Express)','19:25 - 10:00',490,300,1295,All_days],
         [19251,'Train 5 : Veraval To Dwarka(SMNH OKHA Exp.)','23:05 - 07:01',255,140,695,All_days]]

    xx = []
    for i in T_D:
        if day[0:3] in i[-1]:
            xx.append(i[1][6])   # 'Train 1 : Gandhinagar To Surat(Vande Bharat)' this is first elememt of i and 6th chr of this append in xx
            print(i[1])
            # print(xx)

    x = input("Which Trains's details you want to know (Enter only no. like 1,2,3...) : ").strip()
    print()

    while True:
      if x.isnumeric() and x in xx:
          break
      else:
          print('plz,Enter valid option')
          x = input("In Which Train you want to book a Ticket (Enter only no. like 1,2,3...) : ").strip()
    print()

    T_Name = Trains[int(x)]           #Train
    TN = T_D[(int(x) - 1)][0]         #Train Number
    TT = T_D[(int(x) - 1)][2]         #Train Time
    TR = T_D[(int(x) - 1)][-1]        #Train Runs of which days
    slF = T_D[(int(x) - 1)][3]        #Sleeper Fare
    gF = T_D[(int(x) - 1)][4]         #General Fare
    acF = T_D[(int(x) - 1)][5]        #Ac Fare


    main_df = pd.read_csv(main_csv_path)

    df_train_no = main_df['Train No.'].tolist()
    df_class = main_df['Class'].tolist()

    T_Class = []   #in this train class append

    for i, j in zip(df_train_no, df_class):
      if i == TN:
          T_Class.append(j)
    # print(T_Class)

    SL_SEAT_NO = T_Class.count('SLEEPER')
    AC_SEAT_NO = T_Class.count('AC')
   # print(SL_SEAT_NO)
   # print(AC_SEAT_NO)

    sl_seat = 50 - SL_SEAT_NO
    ac_seat = 50 - AC_SEAT_NO

    print(f'Train is {T_Name}'
            f'\nTrain No. is {TN}'
            f'\nTime is {TT}'
            f'\nTrain Runs on {TR}'
            f'\nThere are three Class in this Train like vise SL,GEN,AC'
            f'\nSeat Availability in Different Class Are as per below,\n'
            f'\n{sl_seat} out of 50 Seats Available in Sleeper(SL) Class\nAnd Fair is Rs.{slF}\-\n'
            f'\n{ac_seat} out of 50 Seats Available in Air-Conditioner Class)\nAnd Fair is Rs.{acF}\-')


    df = pd.read_csv(csv_path)

    df_email = df['Email ID'].tolist()
    # print(df_email)

    df_password = df['PASSWORD'].tolist()
    df_PW = [str(i) for i in df_password]
    # print(df_PW)


    print('To book ticket first you have to login your Account :')

    user_id = input('Enter Your E-mail id : ')
    password = input('Enter Your Password : ')

    while True:
      if user_id in df_email and password in df_PW:
          print('Now You can book the ticket')
          break
      else:
          print('User Name Or Password is Inncorrect')
          user_id = input('Enter Your User Name : ')
          password = input('Enter Your Password : ')
    print()

    no_ticket = input('Enter How many tickets you want to book? : ')
    while True:
        if no_ticket.isdigit() and 0 < int(no_ticket) < 7:
            break
        else:
            print('please enter valid input and you can book maximum 6 tickets at a time')
            no_ticket = input('Enter How many tickets you want to book? : ')

    p_list = []

    for i in range(1, int(no_ticket) + 1):

      temp_list = []

      print(f'Add details of passenger {i};')
      # add-passenger name
      NAME = input("Enter Name : ")
      temp_list.append(NAME)

      # GENDER -- M OR F OR OTHER
      print("Plaese Select Your Gender :\n1. Male \n2. Female \n3. Other ")
      GENDER = input("Select One Option From Above : ")


      while True:
          if GENDER == '1' or GENDER == '2' or GENDER == '3':
              if GENDER == '1':
                  GN = 'Male'
                  temp_list.append(GN)

              elif GENDER == '2':
                  GN = 'Female'
                  temp_list.append(GN)

              elif GENDER == '3':
                  GN = 'Other'
                  temp_list.append(GN)
              break
          else:
              GENDER = input("Select One Option From Above : ")

      ## AGE -- IT MUST BE WITHIN IN 150 YEARS
      AGE = input("Plesse Enter Your Age :")
      while AGE.isdigit() == False or (0 < (int(AGE)) < 150) == False:
          print("Please Enter Valid Age :")
          AGE = input("Enter Age :")
      temp_list.append(AGE)

      ## PHONE NUMBER - DEFUALT

      df_mobile_no = df['Mobile No.'].tolist()
      # print(df_mobile_no)

      for i,j in zip(df_email,df_mobile_no):
          if i == user_id:
              # print(j)
              MOBILE_NO = j

      ## ADHAAR -- IT MUST BE IN DIGITS AND DIGITS ARE 12

      ADHAAR_NO = input("Please Enter Adhaar No Without Any Space : ")
      while ADHAAR_NO.isdigit() == False or len(ADHAAR_NO) != 12:
          print("Please Enter Your Valid Adhaar No :")
          ADHAAR_NO = input("Please Enter Adhaar No Without Any Space : ")


      TRAIN_NO = TN
      TRAIN_NAME = T_Name

      main_df = pd.read_csv(main_csv_path)

      df_train_no = main_df['Train No.'].tolist()
      df_class = main_df['Class'].tolist()

      T_Class = []  # in this train class append

      for i, j in zip(df_train_no, df_class):
          if i == TN:
              T_Class.append(j)
      # print(T_Class)

      SL_SEAT = T_Class.count('SLEEPER')
      AC_SEAT= T_Class.count('AC')

      print('In which class you want to book\n1.GENERAL CLASS\n2.SLEEPER CLASS\n3.AC CLASS')
      CLASS = input('select any option from above : ')


      while True:
          if CLASS.isdigit():
              if CLASS == '1' or CLASS == '2' or CLASS == '3':
                  if CLASS == '1':
                      ticket_class = 'GENERAL'
                      temp_list.append(ticket_class)
                      SEAT_NO = '-'
                      temp_list.append(SEAT_NO)
                      gen_fare = T_D[(int(x) - 1)][4]
                      temp_list.append(gen_fare)


                  elif CLASS == '2':
                      ticket_class = 'SLEEPER'
                      temp_list.append(ticket_class)
                      SEAT_NO = SL_SEAT + 1
                      temp_list.append(SEAT_NO)
                      sl_fare = T_D[(int(x) - 1)][3]
                      temp_list.append(sl_fare)



                  elif CLASS == '3':
                      ticket_class = 'AC'
                      temp_list.append(ticket_class)
                      SEAT_NO = AC_SEAT + 1
                      temp_list.append(SEAT_NO)
                      ac_fare = T_D[(int(x) - 1)][5]
                      temp_list.append(ac_fare)

                  break

              else:
                  print('Plz,Enter valid input')
                  CLASS = input('select any option from above')
          else:
              print('Plz,Enter valid input')
              CLASS = input('select any option from above')

      df_adhaar_no = df['Adhaar No.'].tolist()
      # print(df_adhaar_no)

      for i, j in zip(df_email, df_adhaar_no):
          if i == user_id:
              # print(j)
              adhaar = str(j)


      PNR_NO = str(TRAIN_NO) + adhaar[0:5]

      main_df = pd.DataFrame({'Name': [NAME],
                              'Gender': [GN],
                              'Age': [AGE],
                              'Mobile No.': [MOBILE_NO],
                              'Email-ID': [user_id],
                              'Adhaar No.': [ADHAAR_NO],
                              'Train No.': [TRAIN_NO],
                              'Train Name': [T_Name],
                              'Class': [ticket_class],
                              'Seat No.': [SEAT_NO],
                              'PNR No.': [PNR_NO],
                              'Booking date': [datetime.date.today()],
                              'Journey Date': [date_input]})
      main_df.to_csv(main_csv_path, mode='a', header=False, index=False)

      p_list.append(temp_list)

    ## Payment

    pay_password = input('Enter Your Account Password for confirm Ticket : ')

    while True:
          if user_id in df_email and pay_password in df_PW:
              print('Payment successfully !!')
              break
          else:
              print('oops!! Inncorrect Password')
              pay_password = input('Enter Your Password : ')
    print()

    print('|| TICKET ||')
    print("-----------------------------------------------------------------------------------------------\n"
              f"\nPNR NO : {PNR_NO}"
              f"\nTRAIN NAME : {TRAIN_NAME}"
              f"\nTRAIN NO : {TRAIN_NO}"
              f"\nJOURNEY DATE : {date_input}\n"
               
              f"\n-----------------------------------PASSENGER DETAILS------------------------------------------\n")
    TF = 0
    for i ,j in  enumerate(p_list):
        print(f'P{i+1} | {j[0]}   GENDER : {j[1]}     AGE :{j[2]}    CLASS : {j[3]}    SEAT NO. : {j[4]}' )
        TF = TF+j[5]

    print("\n-----------------------------------------------------------------------------------------------\n")
    print(f'TOTAL FARE IS : RS. {TF} /-')


def cancel_ticket():
    can_pnr = int(input('Enter your PNR no :'))
    can_date = input('Enter Jorney Date (DD-MM-YYYY) : ')
    final_date = "-".join(can_date.split("-")[::-1])
    df = pd.read_csv(main_csv_path)

    pnr_list = df['PNR No.'].tolist()
    date_list = df['Journey Date'].tolist()
    # print(pnr_list)
    # print(date_list)
    if can_pnr in pnr_list and final_date in date_list:
        csv_file = main_csv_path

        pnr_index = []
        for i, j in enumerate(pnr_list):
            if j == can_pnr:
                # print(i)
                pnr_index.append(i)
        # print(pnr_index)

        confirmation = input("Do you want to delete this Ticket? (y/n): ")
        if confirmation.lower() == "y" or confirmation.upper() == "Y":
            pnr_df = df.drop(pnr_index)
            pnr_df.to_csv(csv_file, index=False)
            print(f"\nTicket with PNR No. {can_pnr} deleted successfully.")
        else:
            print(f"\nDeletion canceled. Ticket with PNR No. {can_pnr} not deleted.")
    else:
        print(f"PNR No. {can_pnr} not found.")












print("Welcome to Ticket Booking System")
user_input = input("what do you want to do ???\n"
                       "1) Create Account:\n"
                       "2) Show train Details:\n"
                       "3) Book Ticket:\n"
                       "4) Cancel Ticket:\n"
                       "Enter Here:")
while user_input != "1" and user_input != "2" and user_input != "3" and user_input != "4":
    print("Invalid!, Enter valid Input")
    user_input = input("what do you want to do ???\n"
                            "1) Create Account:\n"
                       "2) Show train Details:\n"
                       "3) Book Ticket:\n"
                       "4) Cancel Ticket:\n"
                       "Enter Here:")
if user_input == "1":
    Account()
elif user_input == "2":
    show_train_details()
elif user_input == "3":
    booking()

elif user_input == "4":
    cancel_ticket()