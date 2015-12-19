// When the window has finished loading create our google map below
google.maps.event.addDomListener(window, 'load', init);
function avg(a) {
  return a.reduce(function(x, y){return x+y;}) / a.length;
}
var all_center = Object.keys(airports).map(key => airports[key].center)
var avg_lat = avg(all_center.map(center => center.lat()));
var avg_lng = avg(all_center.map(center => center.lng()));

function init() {

// Basic options for a simple Google Map
// For more options see: https://developers.google.com/maps/documentation/javascript/reference#MapOptions
var mapOptions = {
zoomControl: true,
mapTypeControl: false,
scaleControl: false,
streetViewControl: false,
rotateControl: false,

// How zoomed in you want the map to start at (always required)
zoom: 4,

// The latitude and longitude to center the map (always required)
center: new google.maps.LatLng(avg_lat, avg_lng),

// How you would like to style the map.
styles: [ {"featureType":"administrative", "elementType":"all", "stylers":[{"visibility":"off"}]}, {"featureType":"landscape", "elementType":"labels", "stylers":[{"visibility":"off"}]}, {"featureType":"landscape","elementType":"geometry","stylers":[{"color":"#eeeeee"},{"visibility":"on"}, {"lightness":-8}]},{"featureType":"poi","elementType":"all","stylers":[{"hue":"#ffffff"},{"saturation":-100},{"lightness":100},{"visibility":"off"}]},{"featureType":"road","elementType":"geometry","stylers":[{"hue":"#bbc0c4"},{"saturation":-93},{"lightness":31},{"visibility":"simplified"}]},{"featureType":"road","elementType":"labels","stylers":[{"hue":"#bbc0c4"},{"saturation":-93},{"lightness":31},{"visibility":"on"}]},{"featureType":"road.arterial","elementType":"labels","stylers":[{"hue":"#bbc0c4"},{"saturation":-93},{"lightness":-2},{"visibility":"simplified"}]},{"featureType":"road.local","elementType":"geometry","stylers":[{"hue":"#e9ebed"},{"saturation":-90},{"lightness":-8},{"visibility":"simplified"}]},{"featureType":"transit","elementType":"all","stylers":[{"hue":"#e9ebed"},{"saturation":10},{"lightness":69},{"visibility":"on"}]},{"featureType":"water","elementType":"all","stylers":[{"color":"#ffffff"},{"saturation":-78},{"lightness":67},{"visibility":"simplified"}]},{featureType: "administrative.country", elementType: "labels", stylers: [{visibility:"off"}]}, {featureType: "administrative.country", elementType: "geometry", stylers: [{visibility:"on"}]}]
};

// Get the HTML DOM element that will contain your map
// We are using a div with id="map" seen below in the <body>
var mapElement = document.getElementById('map');

// Create the Google Map using our element and options defined above
var map = new google.maps.Map(mapElement, mapOptions);

function gen_color(com) {
  var codes = "0123456789ABCDEF"
  var primes = [[7, 11], [11, 13], [17, 19], [23, 29], [31, 37], [41, 43]];
  var trans_code = primes.map(function(x){return codes[(com * x[0] + x[1])% 16 ]}).join("");

//  return "#"+trans_code;
//  return "#BC1421";
  return "#FF0000";
}

// ------------------------------------------------------------------------
for (var a in airports) {
  var marker = new google.maps.Marker({
    position: airports[a].center, map: map,
    icon: {path: google.maps.SymbolPath.CIRCLE,scale: 2, strokeOpacity: 1, strokeWeight: 5, fillOpacity: 0.75,
      strokeColor: gen_color(airports[a].com), fillColor: gen_color(airports[a].com)
    }
  });
}
}
