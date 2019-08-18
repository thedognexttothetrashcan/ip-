$(function () {

    $.get("/api/movies/", function (data) {
        console.log(data);

        var $movie_container = $("#movie_container");

        if(data["status"] === 200){
            var movie_data = data["data"];

            for( var i=0; i < movie_data.length; i++){
                var $li = $("<li></li>");

                var $a = $("<a></a>");
                $a.attr("href", "/static/html/movie.html?m_id=" + movie_data[i]["m_id"]);

                $a.appendTo($li);

                $a.html(movie_data[i]["m_name"]);

                $li.appendTo($movie_container);

            }
        }

    }, "json")

})