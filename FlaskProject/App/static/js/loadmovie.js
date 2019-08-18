$(function () {

    console.log(window.location.href);

    var url = window.location.href;

    var params = url.split("?")[1];

    var m_id = params.split("=")[1];

    console.log(m_id);

    $.getJSON("/api/movies/" + m_id + "/", function (data) {
        console.log(data);

        if(data["status"] === 200){
            var movie_data = data["data"];

            var $container = $("#container");

            var $h1 = $("<h1></h1>");

            $h1.html(movie_data["m_name"]);

            $h1.appendTo($container);

            var $p = $("<p></p>");
            $p.html(movie_data["m_duration"]);

            $container.append($p);

            var $button = $("<button>删除</button>");

            $button.click(function () {

                $.ajax("/api/movies/" + m_id + "/", {
                    type: "delete",
                    dataType: "json",
                    success: function (data) {
                        console.log(data);
                        if(data["status"] === 204){
                            console.log("跳转回电影列表");
                            window.open("/static/html/movies.html", target="_self");
                        }
                    }
                })

            })

            $button.appendTo($container);
        }

    })

})