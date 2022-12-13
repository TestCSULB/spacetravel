function getToken(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    const cookies = document.cookie.split(";");
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrftoken = getToken("csrftoken");

function onLoaderFunc() {
  $(".seatStructure *").prop("disabled", true);
  $(".displayerBoxes *").prop("disabled", true);
}
function takeData() {
  if ($("#Numseats").val().length == 0) {
    alert("Please enter Number of Seats");
  } else {
    $("#Numseats").prop("disabled", true);
    $("#h1").removeClass("hide");
  }
}

function updateTextArea() {
  if ($("input:checked").length == $("#Numseats").val()) {
    $(".seatStructure *").prop("disabled", true);

    var allNumberVals = [];
    var allSeatsVals = [];
    var ReservePrice = $("#Numseats").val() * 50000.0;

    allNumberVals.push($("#Numseats").val());
    $("input:checked").each(function () {
      allSeatsVals.push($(this).val());
    });

    $("#NumberDisplay").val(allNumberVals);
    $("#seatsDisplay").val(allSeatsVals);
    $("#Price").val(ReservePrice);

    $("#i1").val(allNumberVals);
    $("#i2").val(allSeatsVals);
    $("#i3").val(ReservePrice);

    localStorage.setItem("NumSeats", allNumberVals);
    localStorage.setItem("TotalPrice", ReservePrice);
    $("#h2").removeClass("hide");
  } else {
    alert("Please select " + $("#Numseats").val() + " seats");
  }
}

$(".seats").click(function () {
  if ($("input:checked").length == $("#Numseats").val()) {
    $("input[type=checkbox]").prop("disabled", true);
    $("input:checked").prop("disabled", false);
  } else if ($("input:checked").length < $("#Numseats").val()) {
    $("input[type=checkbox]").prop("disabled", false);
  }
});

$("#confirm").click(function () {
    var allSeatsVals = [];
    $("input:checked").each(function () {
        allSeatsVals.push($(this).val());
      });
  
  var totalseats = $("#NumberDisplay").val();
  var price = $("#Price").val();

  const data = { noOfSeat: totalseats, seatNo: allSeatsVals, price: price };

  fetch("/book-flight", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": csrftoken,
    },
    body: JSON.stringify(data),
  }).then(
    (response) =>
    window.location.reload()
  );

});


$("#registerFlightbtn").click(function () {
    $("#viewFlight").removeClass('hide')
    $("#registerFlight").addClass('hide')
});


$("#viewFlightbtn").click(function () {
    $("#viewFlight").addClass('hide')
    $("#registerFlight").removeClass('hide')
});