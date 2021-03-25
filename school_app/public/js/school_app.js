/**
 * Created by vanessa on 3/25/21.
 */

console.log("=========")

$(document).ready(function() {
    $('.layout-side-section').hide();
});

$(document).keydown(function(response) {
  if(response.key === "m" && response.ctrlKey === true && $('div.layout-side-section').is(':hidden')){
       $('.layout-side-section').show();
       $('.col-md-10').css("width", "80.33333%");
  }
  else if(response.key === "m" && response.ctrlKey === true && $('div.layout-side-section').is(':visible')){
       $('.layout-side-section').hide();
       $('.col-md-10').css("width", "100%");
  }
});