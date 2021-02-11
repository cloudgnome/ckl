class OneToOne{
	constructor(model,field){
		this.model = model;
		$('#fgk .remove').on('click',this.remove);
		$('#fgk input').on('keypress input',this.add);
	}
	add(event){
		if(event.keyCode == 13){
			var value = this.value;
			if(value){
				var template = `<span class="ui-icon ui-icon-trash remove">X</span> 
								<span class="tag">${value}</span>
								<input type="hidden" name="${view.fgk.model}[]" value="${value}">`;
				var div = create('div');
				div.html(template);
				div.find('.remove')[0].on('click',view.fgk.remove);
				$('#id_fgk_on_deck').append(div);
				this.value = '';
			}
		}
		event.stopPropagation();
		return false;
	}
	remove(){
		this.parent().remove();
		$('#save').removeAttr('disabled');
	}
}