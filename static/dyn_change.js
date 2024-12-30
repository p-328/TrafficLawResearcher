function dyn_change() {
    let choice = document.getElementById("id_query_choice");
    let formatInput = document.getElementById("id_format_of_data");
    let parentOfFormat = formatInput.parentNode;
    let id = formatInput.id;
    let name = formatInput.name;
    let className = formatInput.className;
    parentOfFormat.removeChild(formatInput);
    let newFormatInput = document.createElement("input");
    newFormatInput.name = name;
    newFormatInput.id = id;
    newFormatInput.className = className;
    if (choice.value == "general") {
        newFormatInput.type = "hidden";
    } else {
        newFormatInput.type = "text";
    }
    let newLabel = document.createElement("p");
    let text = document.createTextNode("Format of data:");
    newLabel.appendChild(text);
    parentOfFormat.appendChild(newLabel);
    parentOfFormat.appendChild(newFormatInput);
}