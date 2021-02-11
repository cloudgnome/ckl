class Autocomplete{
	constructor(model){
		this.model = model;
		$(`.autocomplete.${model} input[type="text"]`).on('paste keypress',this.autocomplete.bind(this));
		$(`.autocomplete.${model} .remove`).on('click',this.remove.bind(this));
	}
	autocomplete(event){
		if(this.timeout)
			clearTimeout(this.timeout);
		var that = this;
		that.timeout = setTimeout(function(){
			http.action = function(){
				$(`.autocomplete.${that.model} .variants`).html(templates.autocomplete(http.json.items));
				$(`.autocomplete.${that.model} .variant`).on('click',that.add.bind(that));
				$(`.autocomplete.${that.model} .variants`).show();
			};
			http.get(`/autocomplete/${that.model}/${event.target.value}`);
		},500);
		event.stopPropagation();
		return false;
	}
	add(event){
		var id = event.target.get('value');
		var name = event.target.text();
		log(name);
		var input = $(`.autocomplete.${this.model} input[type="hidden"]`)[0];
		if(!input){
			$(`.autocomplete.${this.model} input[type="text"]`)[0].value = name;
			$(`.autocomplete.${this.model} .variants`).hide();
			return;
		}
		var value = input.value;
		if(value){
			value = eval(value);
		}
		if(Array.isArray(value)){
			value.push(parseInt(id));
			value = JSON.stringify(value);
		}
		else{
			value = id.toString();
		}
		input.value = value;
		$(`.autocomplete.${this.model} .values`).html($(`.autocomplete.${this.model} .values`).html() + templates.autocomplete_value(id,name));
		$(`.autocomplete.${this.model} .remove[value="${id}"]`).on('click',this.remove.bind(this));
		$(`.autocomplete.${this.model} .variants`).hide();
		$(`.autocomplete.${this.model} input[type="text"]`)[0].value = '';
	}
	remove(event){
		var id = parseInt(event.target.get('value'));
		var input = $(`.autocomplete.${this.model} input[type="hidden"]`)[0];
		var value = input.value;
		if(value){
			value = eval(value);
			if(Array.isArray(value)){
				value.remove(id);
				value = JSON.stringify(value);
			}
			else{
				value = '';
			}
			log(value);
			input.value = value;
			event.target.parent().parent().remove();
		}
		$('#save').removeAttr('disabled');
	}
}