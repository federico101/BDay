const countdown = () => {
    // target person's bday
    const birthday = new Date("March 17, 2022 00:00:00").getTime();
    const dateToday = new Date().getTime();
    const timeLeft = birthday - dateToday;
    
    // variables for time 
    const seconds = 1000;
    const minutes = second * 60;
    const hours = minutes * 60;
    const days = hours * 24;
    
    const dayNum = Math.floor(timeLeft / days);
    const hourNum = Math.floor((timeleft % days) / hours);
    const minNum = Math.floor((timeleft % hours) / minutes);
    const secNum = Math.floor((timeleft % minutes) / seconds);
    
    document.getElementsByClassName(".dayTime").innerText = dayNum;
    document.getElementsByClassName(".hourTime").innerText = hourNum;
    document.getElementsByClassName(".minTime").innerText = minNum;
    document.getElementsByClassName(".secTime").innerText = secNum;
};

countdown();

document.querySelector(".dayLabel").value = "!!!"
