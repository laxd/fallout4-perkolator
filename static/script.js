$(document).ready(function(){

	$(".perk").bind("contextmenu", function() {
		var perkname = $(this).find(".perk-name").text()
		if(perkToRank[perkname] > 0) {
			perkToRank[perkname]--
		}
		console.log("Decrease " + perkname + " - Rank: " + perkToRank[perkname])
		return false;
	});

	$(".perk").on("click", function(){
		var perkname = $(this).find(".perk-name").text()
		var ranks = $(this).find(".perk-ranks > div");
		var maxRank = ranks.size()
		if(perkToRank[perkname] < maxRank) {
			perkToRank[perkname]++
		}
		console.log("Increase " + perkname + " - Rank: " + perkToRank[perkname])
	});

	$("#get-suggestion").on("click", function() {
		console.log("Getting suggestion...")
		$.ajax({
			url: "/get-suggestion",
			method: "POST",
			data: perkToRank,
			success: function(data) {
				for(key in data) {
					$("#suggestions").append(key + " -> " + data[key])
				}
			}
		})
	});

	var perkToRank = {}

	$(".perk").each(function(){
		perkToRank[$(this).find(".perk-name").text()] = 0
	});
});

