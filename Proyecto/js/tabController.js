function openPage(pageName, elmnt, color) {
  var i, tabcontent, tablinks;
  tabcontent = document.getElementsByClassName("tabcontent");
  for (i = 0; i < tabcontent.length; i++) {
    tabcontent[i].style.display = "none";
  }
  tablinks = document.getElementsByClassName("tablink");
  for (i = 0; i < tablinks.length; i++) {
    tablinks[i].style.backgroundColor = "";
  }
  document.getElementById(pageName).style.display = "block";
  elmnt.style.backgroundColor = color;
}

function searchEngine() {
  var input, filter, ul, li, a, i, txtValue;
  input = document.getElementById("myInput");
  filter = input.value.toUpperCase();
  ul = document.getElementById("myUL");
  li = ul.getElementsByTagName("li");
  for (i = 0; i < li.length; i++) {
    a = li[i].getElementsByTagName("py-button")[0];
    console.log("Valor de a: " + a);
    txtValue = a.textContent || a.innerText;
    console.log("Valor de texto: " + txtValue);
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      li[i].style.display = "";
    } else {
      li[i].style.display = "none";
    }
  }
}

function weather() {
  //API Key: 29523f5ed8df496a980268afea48f3f3
  //URL: https://api.weatherbit.io/v2.0/current?postal_code=44350&country=MX&units=l&key=29523f5ed8df496a980268afea48f3f3
  const postalCodeInput = document.querySelector("#postalCodeInput");
  let postalCode = postalCodeInput ? postalCodeInput.value : "44630";

  const apiKey = "29523f5ed8df496a980268afea48f3f3";

  const apiUrl = `https://api.weatherbit.io/v2.0/current?postal_code=${postalCode}&country=MX&units=l&key=${apiKey}`;

  fetch(apiUrl)
    .then((response) => response.json())
    .then((jsonData) => {
      //show data
      console.log(data);
      let weatherData = jsonData.data[0];
      let city_name = weatherData.city_name;
      let temp = weatherData.temp;
      let wind_cdir_full = weatherData.wind_cdir_full;
      let wind_spd = weatherData.wind_spd;
      let lat = weatherData.lat;
      let lon = weatherData.lon;
      let sunrise = weatherData.sunrise;
      let sunset = weatherData.sunset;
      let description = weatherData.weather.description;
      let icon = weatherData.weather.icon;

      document.getElementById("city_name").textContent = city_name;
      document.getElementById("temp").textContent = temp + "°C";
      document.getElementById("wind_cdir_full").textContent = wind_cdir_full;
      document.getElementById("wind_spd").textContent = wind_spd;
      //document.getElementById("lat").textContent = lat;
      //document.getElementById("lon").textContent = lon;
      document.getElementById("sunrise").textContent = sunrise;
      document.getElementById("sunset").textContent = sunset;
      document.getElementById("description").textContent = description;
      document.getElementById("icon").src = `../images/icons/${icon}.png`;
    })
    .catch((error) => {
      cityName.innerText = "Error al obtener los datos del clima";
    });
}