//
//window.onload = function () {
//    $('.basket_list').on('click', 'input[type="number"]', function () {
//        var t_href = event.target;
//
//        $.ajax({
//            url:"basket/edit/" + t_href + "/" + t_href.value + "/",
//
//            success: function (data) {
//                $('.basket_list').html(data.result);
//            },
//        });
//        event.preventDefault();
//    });
//}

console.log('hello');
window.onload = function () {
    console.log('hello');
    $('.basket_list').on('click', 'input[type="number"]', function () {
        var t_href = event.target;
//        console.log(t_href)
//        console.log('hello')
        $.ajax({
            url: "/basket/edit/" + t_href.name + "/" + t_href.value + "/",

            success: function (data) {
                $('.basket_list').html(data.result);
            },
        });
        event.preventDefault();
    });
}