function addElement() {
    $("ul.my_list").append("<li>Item</li>");
}
$("div#add_item").on("click", addElement)