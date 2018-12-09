const url_local = 'http://localhost:5000/';

window.onload = function(){
    getRestaurant();
}


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
    buildWebsiteContent(data);
}    
).catch(error => {
    console.error(error);
});
}

function buildWebsiteContent(data) {
    let startRow = 2
    let endRow = 3

    // title
    let myContainer = document.getElementById('canvas');
    let header = document.createElement("div");
    header.className = "header";
    let title = document.createElement("h1");
    title.innerHTML = data.name;
    header.append(title);
    myContainer.append(header);

    // contact box
    if(data.contact) {
        let contact_box = document.createElement("div");
        contact_box.className = "sidebar";
        // contact_box.style.gridArea = "sidebar";
        for(contact_info in data.contact){
            el = document.createElement("p");
            el.innerHTML = data.contact[contact_info];
            contact_box.append(el);
        myContainer.append(contact_box);
    }
}
    
    // info texts
    if (data.content.texts){
        
        for(let i = 0, len = data.content.texts.length; i < len; i++){
            let text_box = document.createElement("div");
            text_box.className = "textbox";
            el = document.createElement("p");
            el.innerHTML = data.content.texts[i].text;
            el.style.gridStartRow = startRow;
            el.style.gridEndRow = endRow;
            startRow++;
            endRow++;
            text_box.append(el);
        myContainer.append(text_box);
    }
}
    // menu
    if (data.menu){
        let space = document.createElement("div");
        space.style.gridRow = startRow + "/" + endRow;
        space.style.height= 10 + "vh";
        myContainer.append(space);
        startRow++;
        endRow++;
        
        let menu_heading = document.createElement("div");
        
        menu_heading.style.gridRow = startRow + "/" + endRow;
        startRow++;
        endRow++;
        let title = document.createElement("h1");
        title.innerHTML = "Menü";
        title.className = "subheading";
        menu_heading.append(title)
        myContainer.append(menu_heading)



        console.log(data)

        
        for(let i = 0, len = data.menu.length; i < len; i++){
            let paragraph_box = document.createElement("div");
            paragraph_box.className = "paragraphBox";
            paragraph_box.style.gridRow = startRow + "/" + endRow;
            paragraph_box.style.gridColumn = 2 + "/" + 3;
       
            menu_paragraph = data.menu[i]
            el = document.createElement("p");
            el.innerHTML = menu_paragraph.title;
            el.className = "subsubheading";
            
            el.style.gridRow = startRow + "/" + endRow;
            el.style.gridColumn = 1+ "/" + 2;
            myContainer.append(el);
            for (let j = 0, len = menu_paragraph.dishes.length; j < len; j++) {
                dish_box = document.createElement("div");
                dish_box.className = "dishbox";
                dish_box.style.gridColumn = 2+ "/" + 3;

                dishName = document.createElement("p");
                dishName.className = "dishname";
                dishName.innerHTML = menu_paragraph.dishes[j].name;
                dish_box.append(dishName);

                dishDescr = document.createElement("p");
                dishDescr.innerHTML = menu_paragraph.dishes[j].description;
                dish_box.append(dishDescr);

                for (let k = 0, len = menu_paragraph.dishes[j].variants.length; k < len; k++) {
                    if(menu_paragraph.dishes[j].variants[k].measurement != "None") {
                        // console.log(menu_paragraph.dishes[j].variants[k])
                        dishVariantMeasurement = document.createElement("p");
                        dishVariantMeasurement.innerHTML = menu_paragraph.dishes[j].variants[k].measurement + " | " + menu_paragraph.dishes[j].variants[k].price;
                        dish_box.append(dishVariantMeasurement);
                        } else {
                            dishVariantPrice = document.createElement("p");
                            dishVariantPrice.innerHTML = menu_paragraph.dishes[j].variants[k].price;
                            dish_box.append(dishVariantPrice);  
                        }
                     
                    }   
                
                paragraph_box.append(dish_box)
                }
            
            startRow++;
            endRow++;
            myContainer.append(paragraph_box);
            
            
        }
        
    }
}

