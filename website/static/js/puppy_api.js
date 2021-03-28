$.get( "https://dog.ceo/api/breeds/image/random", function( data ) {
  $( "#puppy_image" ).attr("src", data.message );
});

const settings = {
	"async": true,
	"crossDomain": true,
	"url": "https://quotes15.p.rapidapi.com/quotes/random/",
	"method": "GET",
	"headers": {
		"x-rapidapi-key": "d7cb94f27dmsh96d3dabd8b73ea8p1e8114jsn6514282cc8de",
		"x-rapidapi-host": "quotes15.p.rapidapi.com"
	}
};

$.ajax(settings).done(function (response) {
  $( "#quote" ).html( `${response.content} - ${response.originator.name}`);
});

function refresh(){
  location.reload();
}