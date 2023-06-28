// alert("hi");

// function Hey() {
//   alert("Hey there!");
// }

// let counter = 0;
// function count() {
//   counter++;
//   // alert(counter);
//   document.querySelector("#counter").innerHTML = `Count: ${counter}`;
//   //alert at every 10
//   if (counter % 10 === 0) {
//     alert(`count is now ${counter}`);
//   }
// }
// document.addEventListener("DOMContentLoaded", function () {
//   document.querySelector("#btn-counter").onclick = count;
//   setInterval(count, 1000);
// });
//automate counter with setInterval builtin function every 1sec/1000 millisec, it will reset to 0 every time page load

/* local storage and set interval */

// if you want to store & reset  info inside web browser use local storage and run it at very begining of function
//first step check if something is already there in local storage if not, set value of counter to 0.
if (!localStorage.getItem("sCounter")) {
  localStorage.setItem("sCounter", 0);
}
function sCount() {
  let sCounter = localStorage.getItem("sCounter");
  sCounter++;
  document.querySelector("#selfCounter").innerHTML = sCounter;
  localStorage.setItem("sCounter", sCounter);
}
document.addEventListener('DOMContentLoaded', function () {
  document.querySelector('#selfCounter').innerHTML =
    localStorage.getItem("sCounter");
  document.querySelector('#btn-sCounter').onclick = sCount;

    setInterval(sCount, 1000);
  });
 