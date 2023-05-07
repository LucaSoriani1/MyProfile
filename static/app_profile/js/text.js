$(document).ready(function () {
  var $randomnbr1 = $(".random1 .nbr");
  var $randomnbr2 = $(".random2 .nbr");
  var $timer = 10;
  var $it;
  var $data = 0;
  var index;
  var change;
  var name = document.getElementById("fullName").value.replace(/\s/g, "");
  var letters1 = Array.from(name);
  const phrase = document.getElementById("title").value.replace(/\s/g, "");
 
  var letters2 = Array.from(phrase);

  $randomnbr1.each(function () {
    change = Math.round(Math.random() * 100);
    $(this).attr("data-change", change);
  });

  $randomnbr2.each(function () {
    change = Math.round(Math.random() * 100);
    $(this).attr("data-change", change);
  });

  function random() {
    return Math.round(Math.random() * 9);
  }

  function select1() {
    return Math.round(Math.random() * $randomnbr1.length + 1);
  }

  function select2() {
    return Math.round(Math.random() * $randomnbr2.length + 1);
  }

  function value() {
    $(".random1 .nbr:nth-child(" + select1() + ")").html("" + random() + "");
    $(".random1 .nbr:nth-child(" + select1() + ")").attr("data-number", $data);
    $(".random2 .nbr:nth-child(" + select2() + ")").html("" + random() + "");
    $(".random2 .nbr:nth-child(" + select2() + ")").attr("data-number", $data);
    $data++;

    var $nbrs = $randomnbr1.add($randomnbr2);
    var $remainingNbrs = $nbrs.filter(".nbr");

    $remainingNbrs.each(function () {
      if (
        parseInt($(this).attr("data-number")) >
        parseInt($(this).attr("data-change"))
      ) {
        index = $(".ltr").index(this);
        $(this).html(index < letters1.length ? letters1[index] : letters2[index - letters1.length]);
        $(this).removeClass("nbr");
      }
    });

    if ($remainingNbrs.length == 0) {
      clearInterval($it);
    }
  }

  $it = setInterval(value, $timer);
});
