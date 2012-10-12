$(document).ready(function() {
    var postButton;
    var dropbox = document.getElementById("dropbox")

	// init event handlers
	dropbox.addEventListener("dragenter", dragEnter, false);
	dropbox.addEventListener("dragexit", dragExit, false);
	dropbox.addEventListener("dragover", dragOver, false);
	dropbox.addEventListener("drop", drop, false);

	// init the widgets
	$("#progressbar").progressbar();
});

function dragEnter(evt) {
	evt.stopPropagation();
	evt.preventDefault();
}

function dragExit(evt) {
	evt.stopPropagation();
	evt.preventDefault();
}

function dragOver(evt) {
	evt.stopPropagation();
	evt.preventDefault();
}

function drop(evt) {
	evt.stopPropagation();
	evt.preventDefault();

	var files = evt.dataTransfer.files;
	var count = files.length;

	// Only call the handler if 1 or more files was dropped.
	if (count > 0)
    handleFiles(files, count-1);
}

function handleFiles(files, x) {
    document.getElementById("file_name").innerHTML = files[x].name;
}
