let welcome = document.querySelector('.message');
let message = document.querySelector('.message div');
let action = document.querySelector('.action');
let show = document.getElementsByClassName('.show');
let boxContainer2 = document.querySelector('.box-container2')
welcome.addEventListener('click', () => {
    welcome.textContent = "Have a Good Time!";
});

action.addEventListener('click', () => {
    boxContainer2.style.display = 'flex';
});
