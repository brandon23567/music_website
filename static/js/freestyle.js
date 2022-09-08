let btn = document.getElementById("btn");
let output = document.getElementById("output");

let words = [
	"school, fool, pool",
	"red, grandma, die",
	"hello, shoot, shock",
	"green, grass, short",
	"superman, bully, dark",
];


btn.addEventListener('click', function(){
	var randomWord = words[Math.floor(Math.random() * words.length)]
	output.innerHTML = randomWord
})