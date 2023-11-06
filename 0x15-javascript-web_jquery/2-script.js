function changeColor() {
    $("header").css("color", "red")
}
$("div#red_header").on("click", changeColor)