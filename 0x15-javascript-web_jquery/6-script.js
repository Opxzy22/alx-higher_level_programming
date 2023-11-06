function updateText() {
    $("header").text("New Header!!!");
}
$("div#update_header").on("click", updateText)