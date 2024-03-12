column = ['Name','Gender','Age','Mobile No.','Adhaar No.','Email ID','PASSWORD']

with open('Account_data.csv','w') as f:
    f.write(','.join(column) + '\n')


columns = ['Name','Gender','Age','Booking Mobile No.','Booking email-ID','Adhaar No.','Train No.','Train Name','Class','Set No.','PNR No.','Booking Date','Journey Date']

with open('Main.csv','w') as f:
    f.write(','.join(columns) + '\n')










