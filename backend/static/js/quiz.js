const quiz = [{
    q: 'which is the frist PM of russia?',
    options: ['abdu kabeer', 'quaid azam', 'benazir'],
    answer: 1
}, {
    q: 'which is the python meaning ?',
    options: ['happy', 'sad', 'loud', 'depressed'],
    answer: 0
}, {
    q: 'which is the java meaning ?',
    options: ['netwrok', 'language', 'api', 'server'],
    answer: 2
}]
console.log(quiz[0])
const questionNumber = document.querySelector(".question-number");
const questionText = document.querySelector(".question-text");
const optionContainer = document.querySelector(".option-container");
let questionCounter = 0;
let currentQuestion;
let availableQuestions = [];
let availableOptions = [];

function setAvailableQuestions() {

    const totalQuestion = quiz.length;
    for (let i = 0; i < totalQuestion; i++) {
        availableQuestions.push(quiz[i])
    }

}


function getNewQuestion() {
    questionNumber.innerHTML = "Question" + (questionCounter + 1) + "of " + quiz.length;

    const currentQuestion = availableQuestions[questionCounter]
    typeof(currentQuestion)
    questionText.innerHTML = currentQuestion.q;
    // set options
    const optionLen = currentQuestion.options.length;
    optionContainer.innerHTML = '';
    let animationDelay = 0.15;
    for (let i = 0; i < optionLen; i++) {
        availableOptions.push(i)
    }
    for (let i = 0; i < optionLen; i++) {
        const optonIndex = availableOptions[Math.floor(Math.random() * availableOptions.length)];
        console.log(optonIndex)
        const index2 = availableOptions.indexOf(optonIndex);
        console.log(index2)
        availableOptions.splice(index2, 1);
        console.log(availableOptions)

        const option = document.createElement("div");
        option.innerHTML = currentQuestion.options[optonIndex];
        option.id = optonIndex;
        option.style.animationDelay = animationDelay + 's';
        animationDelay = animationDelay + 0.2;
        option.className = "option";
        optionContainer.appendChild(option)
        console.log(currentQuestion)
            //element.classList.add("wrong");
        a = currentQuestion.answer;
        option.setAttribute("onclick", "getResult(this,a)")
        console.log('going to getResult')

    }
    questionCounter++
}

function getResult(element, cq) {

    console.log('inside get result')
    console.log(cq)

    //element.classList.add("correct");
    console.log(element)
    const id = parseInt(element.id);
    if (id === cq) {
        element.classList.add("correct");
        console.log("correct");
    } else { //set red color to wrong options 
        console.log("wrong");
        element.classList.add("wrong");
    }
    unclickableOptions()

}

function unclickableOptions() {
    console.log("in unclickable method")
    const optionLen = optionContainer.children.length;
    for (let i = 0; i < optionLen; i++) { optionContainer.children[i].classList.add("already-answered"); }
}


function next() {
    if (questionCounter === quiz.length) {
        console.log("Quiz over")
    } else {
        getNewQuestion();
    }
}
window.onload = function() {
    setAvailableQuestions();
    getNewQuestion();
}