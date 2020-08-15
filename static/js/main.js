function GetHotelReviewsTones() {
    var selectedHotel = document.getElementById("hotels").value ;
    var updateSuccess = function( result ) {console.log("sucess");}
    var printError = function( result ) {console.log("failed");}
    $.ajax({
        type: 'POST',
        url: "/GetReviewsTones",
        data: {'name': selectedHotel},
        success: function(response) {
            $("div.HotelReviews").html(response);
          },
        error: function(jqxhr, status, exception) {
            console.log(exception);
        }
        });
    }

function IndexHotel() {
    var selectedHotel = document.getElementById("hotels").value ;
    var updateSuccess = function( result ) {console.log("sucess");}
    var printError = function( result ) {console.log("failed");}
    $.ajax({
        type: 'POST',
        url: "/IndexData",
        data: {'name': selectedHotel},
        success: function(jqxhr, status, exception) {
            alert("Indexing hotel finished")},
        error: function(jqxhr, status, exception) {
            alert("Indexing failed")
        }
        });
    }

function IndexAll() {
    var updateSuccess = function( result ) {console.log("sucess");}
    var printError = function( result ) {console.log("failed");}
    $.ajax({
        type: 'POST',
        url: "/IndexData",
        data: {},
        success: function(jqxhr, status, exception) {
            alert("Indexing finished")},
        error: function(jqxhr, status, exception) {
            alert("Indexing failed")
        }
        });
    }