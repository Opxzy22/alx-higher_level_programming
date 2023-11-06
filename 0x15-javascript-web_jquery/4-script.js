function toggleCls () {
    $("header").toggleClass("red green");
}
$("div#toggle_header").on("click", toggleCls)