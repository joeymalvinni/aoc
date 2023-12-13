// ==UserScript==
// @name         AoC copy code blocks
// @description  copy code blocks in Advent of Code
// @version      1.1.0
// @author       mcpower, joeymalvinni
// @match        https://adventofcode.com/*
// ==/UserScript==

let style = document.createElement("style");
style.innerHTML = `

code.copied:before{background: #30304f;}

code {
    -webkit-transition: background-color 0.2s ease-in-out;
    -ms-transition: background-color 0.2s ease-in-out;
    transition: background-color 0.2s ease-in-out;
}

@keyframes fadeInAnimation {
	0% {
		opacity: 0;
		 margin-top: 5px;
	}
	100% {
		opacity: 1;
		margin-top: 0px;
	 }
}

@keyframes fadeOutAnimation {
    0% {
        opacity: 1;
        margin-top: 0;
    }
    100% {
        opacity: 0;
        margin-top: 5px;
    }
}
`;
document.head.appendChild(style);

let codeElements = document.getElementsByTagName('code');

for (var i = 0; i < codeElements.length; i++) {
    codeElements[i].style.cursor = 'pointer';
}

function popup(event) {
    const clickedCodeElement = event.target;
    const codeRect = clickedCodeElement.getBoundingClientRect();

    const x = codeRect.left + codeRect.width / 2;
    const y = event.clientY + window.scrollY - 50;

    const element = document.createElement("div");
    element.style.cssText = `
        background-color: #1b1928;
        position: absolute;
        top: ${y}px;
        left: ${x}px;
        transform: translateX(-50%); /* Center in x-direction */
        color: #cfcfcf;
        animation: fadeInAnimation ease 0.2s;
        animation-fill-mode: forwards;
    `;

    const paragraph = document.createElement("p");
    paragraph.style.cssText = `
        margin: 0;
        padding: 5px;
    `;
    paragraph.textContent = "Copied!";

    element.appendChild(paragraph);
    document.body.appendChild(element);

    return element;
}

Array.from(document.getElementsByTagName("code")).forEach(el => {
    el.addEventListener("click", async event => {
        if (window.getSelection().type === "Range") {
            return;
        }
        await navigator.clipboard.writeText(el.textContent);
        el.classList.add("copied");

        let copied = popup(event);
        await new Promise(resolve => setTimeout(resolve, 500));

        copied.style.animation = "fadeOutAnimation ease 0.2s";
        await new Promise(resolve => setTimeout(resolve, 200));

        el.classList.remove("copied");
        copied.remove();
    });
});
