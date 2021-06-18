// console.log("this is my custom");
/*
$(function () {
  $("#videoModal2")
    .modal({
      show: false,
    })
    .on("hidden.bs.modal", function () {
      $(this).find("video")[0].pause();
      // console.log("paused video");
    });
});

//  console.log('script');
var modal = $("#modalVideo").hasClass("show");
if (modal) {
  // console.log('modal is now open');
} else {
  //  console.log('modal is now closed');
}

$("#videoModal").on("hidden.bs.modal", function (e) {
  // do something...
  console.log("modal is now closed fsdf fdsf dfsd");
});
*/
$("#videoModal").on("show.bs.modal", function (e) {
  console.log("finally opened modal");
});

$("#videoModal").on("shown.bs.modal", function () {
  alert("Hello World!");
});

$(document).ready(function () {
  $("#modalClick2").bind("click", function () {
    // your statements;
    alert("button");
  });

  $(".modalClick2").click(function () {
    alert("button");
  });

  // alert("Image loaded.");
});




    