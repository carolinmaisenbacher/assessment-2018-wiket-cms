const url_local = 'http://localhost:5000';


window.onload = function(){
    getRestaurants();
}


function getRestaurants() {
fetch(url_local + "/api/restaurants")
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
    let myList = document.getElementById('restaurants');

    for(restaurant in data.restaurants) {
        let el = document.createElement("option");
        el.innerHTML = data.restaurants[restaurant].name;
        el.value = data.restaurants[restaurant].id;
        console.log(el.value)
        console.log(el)
        console.log(myList)
        myList.append(el);
    }

}

