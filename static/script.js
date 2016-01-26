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
		var maxRank = 3
		if(perkToRank[perkname] < maxRank) {
			perkToRank[perkname]++
		}
		console.log("Increase " + perkname + " - Rank: " + perkToRank[perkname])
	});

	var perkToRank = {}

	$(".perk").each(function(){
		perkToRank[$(this).find(".perk-name").text()] = 0
	});
});

