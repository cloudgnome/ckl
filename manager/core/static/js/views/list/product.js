var timeout;
class ListProduct extends List{
	constructor(){
		super();
		$('.autocomplete').each(function(elem){
			var model = elem.get('model');
			window['autocomplete_' + model] = new Autocomplete(model=model);
		});
	}
}