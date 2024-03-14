
//const d = new Date();

//console.log(d)

//data ობიექტები არის სტატიკური

//const d = new Date("2009-11-02")

//console.log(d)

//შექმენით date კონსტრიქტორის მეშვეობით თარიღის ობიექტი
// და გამოიყენეთ ყველა get მეთოდები

//const me = new Date();

//console.log(me.toISOString())


//let me = Date.parse("March 21, 2012");

//console.log(me)

//const a = new Date("2021-03-25");

//console.log(a.getDate())

//const d = new Date("2021-03-25");

//console.log(d.getFullYear())

//const b = new Date("2021-03-25");

//console.log(b.getMinutes())

//const m = new Date("2021-03-25");

//console.log(m.getSeconds())

//გამოიყენეთ date ობიექტი, ყოველ 1 წამში შექმენით date 
//ობიექტი და დააკონსოლ ლოგეთ Date ობიექტის სტრინგ

//setInterval(function(){
//   const me = new Data()
   console.log(me.data()),

1000;} )


let second = 30;
let minut = 5;

const timer = setinterval(function(){
    seconds -- ;
    if (seconds == 0){
        minutes --;
        seconds = 60;
        if (minutes == 0){
            clearInterval(timer)
        }
    }
})



