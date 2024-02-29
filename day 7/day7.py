

avarage_score=0

user1=int(input("enter avgarage_score"))
user2=int(input("enter avarage_score"))
user3= int(input("enter avarage_score"))

avarage_score= ((user1 + user2 + user3) /3  )
if avarage_score > 9:
    print("გილოცავ მატრიცელო შენ მოიგე 300 ლარიანი ტოსტერი")


if avarage_score < 5:
    print("გილოცავ შენ გაექეცი მატრიცას")

if avarage_score >5 and avarage_score<9:
    print("YOU ARE MID")

if avarage_score > 10 and avarage_score <0:
    print (" THERE IS SOMETHING WRONG WITH YOU")