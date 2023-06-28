//wait for page to load
document.addEventListener("DOMContentLoaded", function () {
  // query for submit btn and input task and store in variables
  const submit = document.querySelector("#submit");
  const newTask = document.querySelector("#task");
  //enable/not  disable attribute of a submit-btn -t/f
  //disable submit btn by default:
  submit.disabled = true;
  //listen for input to be typed into the field
  newTask.onkeyup = () => {
    if (newTask.value.length > 0) {
      submit.disabled = false;
    } else {
      submit.disabled = true;
    }
  };
  //listen for submission of form:
  document.querySelector("form").onsubmit = () => {
    //find task the user just submitted
    const task = newTask.value;
    //create a new task list item and add task to it
    const li = document.createElement("li");
    li.innerHTML = task;

    //add new element to our unordered list:
    document.querySelector("#tasks").append(li);
    //clear out input field
    newTask.value = "";
    //disable the submit btn again ;
    submit.disabled = true;
    //stop form submission after every entry;
    return false;
  };
});




//stop the default submission of form by return=f
//createElement function to make new html elems and then append them to DOM