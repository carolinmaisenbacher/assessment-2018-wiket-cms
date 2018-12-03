const url_local = 'http://localhost:5000/';
let res_data;

window.onload = function(){
    getRestaurant();
}
document.execCommand("defaultParagraphSeparator", false, "br")

function getRestaurant() {
fetch(url_local + "api/restaurants/3")
.then(response => {
    if (response.status === 200) {
        return response.json()
    } else {
        throw new Error ("Couldn't fetch lists API")
    }
})
.then(data => {
    console.log(data)
    res_data=data;
    initialView(res_data);
}    
).catch(error => {
    console.error(error);
});
}

function initialView(data) {
    let myContainer = document.getElementById('canvas');
    let navigation = document.createElement("div");
    navigation.style.gridRow = "1";
    

    if (data.contact) {
        let contact = document.createElement("div");
        contact.classList.add("menuitem");
        contact.addEventListener('click',() => contactManager());
        let name = document.createElement("p");
        name.innerHTML = "Kontakt";
        contact.append(name);
        navigation.append(contact);
    }

    if (data.menu) {
        let menu = document.createElement("div");
        menu.classList.add("menuitem");
        menu.addEventListener('click',() => menuManager());
        let name = document.createElement("p");
        name.innerHTML = "Menü";
        menu.append(name);
       navigation.append(menu);
    }

    if (data.content.texts) {
        let menu = document.createElement("div");
        menu.classList.add("menuitem");
        menu.addEventListener('click',() => textManager());
        let name = document.createElement("p");
        name.innerHTML = "Texte";
        menu.append(name);
        navigation.append(menu);
    }

    // if (data.openinghours) {
        let menu = document.createElement("div");
        menu.classList.add("menuitem");
        menu.addEventListener('click',() => openingHoursManager());
        let name = document.createElement("p");
        name.innerHTML = "Öffnungszeiten";
        menu.append(name);
        navigation.append(menu);
    // }lcd Cod

    myContainer.append(navigation)
}

// Manager = () => {
//     title;
//     function display(){};
//     function save(){};

// }

// class Manager {
//     constructor(title, div) {
//         this.title = make;
//         this.menudiv = div;
//     }
// }

// Manager.prototype.display = function() {
//     console.log("hey there")
// }

function exitDisplay() {
    clearView()
    initialView(res_data)
        view_active = false;
}


let view_active = false;
function contactManager() {
        

        if(view_active === false){
            displayContact()
        }else {
            exitDisplay();
            displayContact();
        };
}

function displayContact() {
    let myContainer = document.getElementById('canvas');
        let contact = document.createElement("div");
        contact.style.gridColumn = 2 + "/" + 3;
        contact.classList.add("subsubheading");
        let name = document.createElement("p");
        name.innerHTML = "Kontakt";
        contact.append(name);
        myContainer.append(contact);
        view_active = true;
}

function menuManager() {
    if(view_active === false){
        displaymenu()
        }else {
            exitDisplay();
            displaymenu();
        };
}

function displaymenu() {
    let myContainer = document.getElementById('canvas');
        let menu = document.createElement("div");
        menu.style.gridColumn = 2 + "/" + 3;
        menu.classList.add("subsubheading");
        let name = document.createElement("p");
        name.innerHTML = "Menü";
        menu.append(name);
        myContainer.append(menu);
        view_active = true;
}

function textManager() {

    if(view_active === false){
        displayText()
        }else {
            exitDisplay();
            displayText();
        };
}

let changedTexts = null;

function displayText() {
    let myContainer = document.getElementById('canvas');
        let text_heading = document.createElement("div");
        text_heading.style.gridColumn = 2 + "/" + 3;
        text_heading.classList.add("subsubheading");
        let name = document.createElement("p");
        name.innerHTML = "Texte";
        let explanaition = document.createElement("p");
        explanaition.innerHTML = "Das sind deine Texte, die zur Zeit auf der Website zu sehen sind. Verändere sie und speichere deine Änderungen, damit sich auch der Inhalt deiner Website ändert.";
        explanaition.classList.add("help");
        text_heading.append(name);
        text_heading.append(explanaition);
        myContainer.append(text_heading);
        view_active = true;

        //show current texts
        if (res_data.content.texts){
            let text_container = document.createElement("div");
            text_container.classList.add("contentcontainer");
            
        
            for(let i = 0, len = res_data.content.texts.length; i < len; i++){
                let text_box = document.createElement("div");
                text_box.classList.add("contentitem");

                //title of text
                let text_title = document.createElement("div");
                text_title.classList.add("subheading");
                // text_title.contentEditable = 'true';
                text_title.innerHTML = res_data.content.texts[i].title;
                text_box.append(text_title)

                let title_help = document.createElement("p");
                title_help.classList.add("help", "helpitem");
                title_help.innerHTML = "Titel (wird nicht auf Website angezeigt)";
                text_box.append(title_help);

                //text content
                let text = document.createElement("div");
                text.classList.add("textbox");
                // text.contentEditable = 'true';
                text.innerHTML = res_data.content.texts[i].text;
                text_box.addEventListener('input',function() {
                    alert("hello")
                });
                
                
                text_box.append(text);
                let button = new Button([text_title, text])
                console.log(button);
                text_box.append(button);
                text_container.append(text_box);
            }
            myContainer.append(text_container);
        }
}

let Button = function(targetElements) {
    this.targets = targetElements;
    this.el = document.createElement("button")
    this.el.type = "button";
    this.el.innerHTML = "Bearbeiten";
    
    
    this.edit = function(){
        for(target in this.targets) {
            this.targets[target].classList.add("editable"); 
            this.targets[target].contentEditable = 'true';
        }
        this.el.innerHTML = "Sichern";
        this.el.addEventListener('click', () => {this.save()});
    };
    this.save = function() {
        for(target in this.targets) {
            this.targets[target].classList.remove("editable"); 
            this.targets[target].contentEditable = 'false';
        }
        this.el.innerHTML = "Bearbeiten"
        this.el.addEventListener('click', () => {this.edit()});
    };
    this.el.addEventListener('click', () => {this.edit()});
    return this.el
}

function openingHoursManager() {
    if(view_active === false){
        displayOpeningHours()
        }else {
            exitDisplay();
            displayOpeningHours();
        };
}

function displayOpeningHours() {
    let myContainer = document.getElementById('canvas');
        let openingHours = document.createElement("div");
        openingHours.style.gridColumn = 2 + "/" + 3;
        openingHours.classList.add("subsubheading");
        let name = document.createElement("p");
        name.innerHTML = "Öffnungszeiten";
        openingHours.append(name);
        myContainer.append(openingHours);
        view_active = true;
}



function clearView(){
    let myContainer = document.getElementById('canvas');
    while (myContainer.hasChildNodes()) {
        myContainer.removeChild(myContainer.lastChild);
    }


} 