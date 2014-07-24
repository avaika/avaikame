var placeSearch, autocomplete;

function initialize() {
  // initialize the autocomplete
  for (var i = 0; i < 10; i++) {
    autocomplete = new google.maps.places.Autocomplete( (document.getElementById('id_postmap_set-' + i + '-place')), { types: ['geocode'] });
    google.maps.event.addListener(autocomplete, 'place_changed', function() { fillInAddress(); });
  }
}

function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocomplete.getPlace();

  // Get each component of the address from the place details
  // and fill the corresponding field on the form.
  for (var i = 0; i < place.address_components.length; i++) {
    var addressType = place.address_components[i].types[0];
    if (componentForm[addressType]) {
      var val = place.address_components[i][componentForm[addressType]];
      document.getElementById(addressType).value = val;
      }
    }
  }

google.maps.event.addDomListener(window, 'load', initialize);
