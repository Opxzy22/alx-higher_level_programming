window.onload = function () {
    function addItem() {
        $('ul.my_list').append('<li>item</li>');
    }
    function removeItem() {
        var list = $('ul.my_list'); // Use the same selector as addItem
        var item = list.find('li'); // Use jQuery's find() method
        item.last().remove(); // Use jQuery's remove() method
    }
    function clearItem() {
        var list = $('ul.my_list'); // Use the same selector as addItem
        var item = list.find('li'); // Use jQuery's find() method
        item.remove(); // Use jQuery's remove() method
    }
    $('div#add_item').on('click', addItem);
    $('div#remove_item').on('click', removeItem);
    $('div#clear_list').on('click', clearItem);
};
