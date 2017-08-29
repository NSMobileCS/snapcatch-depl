
function initMap() {
    
  
    var uluru = {lat: 37.0902, lng: -95.7129};
    var map = new google.maps.Map(document.getElementById('map'), {
      zoom: 4,
      center: uluru
      
    });
    var lat = uluru.lat; //position.coords.latitude;
    var long = uluru.long; //position.coords.longitude;
  
    GeoMarker = new GeolocationMarker();
        GeoMarker.setCircleOptions({fillColor: '#808080'});
  
        google.maps.event.addListenerOnce(GeoMarker, 'position_changed', function() {
          map.setCenter(this.getPosition());
          map.fitBounds(this.getBounds());
        });
  
        google.maps.event.addListener(GeoMarker, 'geolocation_error', function(e) {
          alert('There was an error obtaining your position. Message: ' + e.message);
        });
  
        GeoMarker.setMap(map);
        
      }
      google.maps.event.addDomListener(window, 'load', initMap);
  
        if(!navigator.geolocation) {
            alert('Your browser does not support geolocation');
        }
    
      $(document).ready(function(){
                //add event listener to find out which tab we are on and pass that to the "iconic_taxa" parameter of the api call
  
                //save species name
  
                //query eol.org for the species
                //return the results

                var animal_list = [];
                $.get("http://api.inaturalist.org/v1/observations?photos=true&verifiable=true&year=2012%2C2013%2C2014%2C2015%2C2016&iconic_taxa=Mammalia&lat="+lat+"&lng="+long+"&radius=100&order=desc&order_by=created_at", function(res) {
                var animal_dict = {};
                for(var i=0;i<30;i++){
                    this.setattribute('id', res.results[i].id)
                    this.setattribute('name', res.results[i].species_guess)
                  $("#mammal-pics").append("<img src= " + '' + res.results[i].photos[0].url +''+">")
                    }
                },"json");
  
  
                $('#pics').click(function(){
                $.ajax({
                  url: '//en.wikipedia.org/w/api.php',
                  data: { action: 'query', list: 'search', srsearch: this.name, format: 'json' },
                  dataType: 'jsonp',
                  success: function (x) {
                  console.log('title', x.query.search[0].title);
                }
  
              });
              });
  
                //add event listener and function for animal click
                //show cards on map
         });
