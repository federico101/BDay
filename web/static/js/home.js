const cakeShow = document.getElementsByClassName(".cake");
const hbdTEXT = document.getElementsByClassName(".hbdtext");

let birthday = new Date("2022-03-17");
const day = document.querySelector(".dayTime");
const hour = document.querySelector(".hourTime");
const minute = document.querySelector(".minTime");
const second = document.querySelector(".secTime");
setInterval(() => {
    const current = new Date();
    const elapsed = birthday - current;
    const secondstotal = Math.floor(elapsed / 1000);
    const days = Math.floor(secondstotal / 3600 / 24);
    const hours = Math.floor(secondstotal / 3600) % 24;
    const minutes = Math.floor(secondstotal / 60) % 60;
    const seconds = Math.floor(secondstotal) % 60;
    day.innerText = days;
    hour.innerText = hours;
    minute.innerText = minutes;
    second.innerText = seconds;
}, 1000);
