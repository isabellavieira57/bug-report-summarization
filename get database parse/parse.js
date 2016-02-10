var http = require('https');
var Parse = require('parse/node').Parse;
var async = require("async");

Parse.initialize("5eVzRldiF9L7nuB4V39VKffzGsSjYd55obLfCCyi", "0XfKd0esbjLX0syKdqs4yGPos77AvuBoP7llWUvn");

retornados = 0;
nexts = 0;

//Chamada funcao
getNext(nexts, function(returnValue) {
			retornados = returnValue;
});


function getNext(skip){
	console.log("Proximos 1000: " + nexts + "\n");
	
	var numeroResultados = 0;
	var Comments = Parse.Object.extend("Comments");
	var query = new Parse.Query(Comments);
	query.limit(1000);							//Limite max do parse
	query.skip(1000); 							// skip the first 10 results
	
	//Obter numero de resultados
	query.find({
		success: function(results) {
			
			//For para obter autores
			for (var i = 0; i < results.length; i++) {
				var object = results[i];
				console.log(object.id + ' - ' + object.get('author'));
			}
			
			//For para obter body
			for (var i = 0; i < results.length; i++) {
				var object = results[i];
				//console.log(object.id + ' - ' + object.get('body'));
			}			
			
			console.log("\nResultados: " + results.length);
			numeroResultados = results.length;
		},
	  error: function(objects,error) {
		console.log("erro");
		numeroResultados = 0;
	  }
	});	
	return numeroResultados;
}
