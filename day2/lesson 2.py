13#ბილეთი ღირს 25 ლარი
#ბავშვებისთვის უფასოა 
#მყავს 13 ადამიანი 
#3 პატარა
#10 სრულწლოვანი
#რამდენი ლარი დასჭირდებათ?

ticket_price=0
age_count=0

while age_count<13:
    age = int(input("enter age"))
    if age_count <=18:
        ticket_price+=0
        age_count+=0
    else :
        ticket_price += 25 
        age_count +=1

print(ticket_price)