const url_local = 'http://localhost:5000/';


window.onload = function(){
    getRestaurants();
}


function getRestaurants() {
fetch(url_local + "api/restaurants")
.then(response => {
    if (response.status === 200) {
        return response.json()
    } else {
        throw new Error ("Couldn't fetch lists API")
    }
})
.then(data => {
    showRestaurantsOverview(data);
}    
).catch(error => {
    console.error(error);
});
}
function showRestaurantsOverview(data) {
    let myContainer = document.getElementById('canvas');
    console.log(data)
    let row = document.createElement("div");
    row.className = "row";
    for(restaurant in data.restaurants) {
        let el = document.createElement("a");
        el.innerHTML = data.restaurants[restaurant].name;
        el.classList.add("seven")
        el.classList.add("columns")
        row.append(el);
        el.href = data.restaurants[restaurant]._links["self_website"];
        // el.classList.add("button-primary");
        el.classList.add("button");
        el.classList.add("button-primary");
    }
    myContainer.append(row)

}
