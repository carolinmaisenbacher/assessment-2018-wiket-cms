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
        text_manager = new TextManager(data.content.texts)
        let menu = document.createElement("div");
        menu.classList.add("menuitem");
        menu.addEventListener('click',() => text_manager.display());
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

class TextManager {
    constructor(raw_texts){
        this.texts = [];
        for(let i = 0, n = raw_texts.length; i < n; i++){
            this.texts.push(new Text(raw_texts[i].id, raw_texts[i].title, raw_texts[i].text, i))
        }
    }
    
    display() {
        if(view_active === false){
            this._displayTexts()
            }else {
                exitDisplay();
                this._displayTexts();
            };
    }

    _displayTexts() {
        console.log(this.texts[0].todict());
        console.log(this.texts[0])
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
            let text_container = document.createElement("div");
            text_container.classList.add("contentcontainer");
            
        
            for(let i = 0, len = this.texts.length; i < len; i++){
                text_container.append(this.texts[i].display());
            }
            myContainer.append(text_container);
    }
    
    save() {
        let data = []
        for(let i = 0, n = this.texts.length; i < n; i++){
            if (this.texts[i].changed) {
                data.push(this.texts[i].todict())
            }
        }

        fetch('http://localhost:5000/api/texts/', {
                method: 'PUT',
                headers: {
                    'Content-Type' : 'application/json'
                }, 
                body: JSON.stringify(data)
            }).then(response => {
                console.log(response)
                if (response.status === 201){
                    console.log("huray")
                }
                else {
                    alert("We couldn't save the texts")
                }
            })
        }
    }

class Text{
    constructor(id, title, text, position){
        this.id = id;
        this.title = title;
        this.text = text;
        this.position = position +1;
        this.changed = false;
    }
    todict() {
        let data = {
            "id" : this.id,
            "title" : this. title,
            "text" : this.text,
            "position" : this.position,
        }
        return data
    }
    display() {
        let text_box = document.createElement("div");
        text_box.classList.add("contentitem");

        //title of text
        let text_title = document.createElement("div");
        text_title.classList.add("subheading");
        text_title.innerHTML = this.title;
        text_box.append(text_title)

        let title_help = document.createElement("p");
        title_help.classList.add("help", "helpitem");
        title_help.innerHTML = "Titel (wird nicht auf Website angezeigt)";
        text_box.append(title_help);

        //text content
        let content = document.createElement("div");
        content.classList.add("textbox");
        content.innerHTML = this.text;
        text_box.addEventListener('input', () => {this.changed=true});
        
        
        text_box.append(content);
        let button = new Button([text_title, content], this)
        console.log(button);
        text_box.append(button);

        return text_box
    }

    save() {
        if (this.changed === true) {
            let data = this.todict()

            fetch('http://localhost:5000/api/texts/', {
                    method: 'PUT',
                    headers: {
                        'Content-Type' : 'application/json'
                    }, 
                    body: JSON.stringify(data)
                }).then(response => {
                    if (response.status === 201){
                        // what happens if texts are saved?
                        console.log(response)
                    }
                    else {
                        alert("We couldn't save the texts")
                    }
                })
            }       
        }
    }


let Button = function(targetElements, textElement) {
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
        this.el.addEventListener('click', () => {this.save();
            textElement.save();});
    };
    this.save = function() {
        for(target in this.targets) {
            this.targets[target].classList.remove("editable"); 
            this.targets[target].contentEditable = 'false';
        }
        this.el.innerHTML = "Bearbeiten"
        this.el.addEventListener('click', () => {
            this.edit()
        });
    };
        // initial eventListener
    this.el.addEventListener('click', () => {
          this.edit();
    });

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