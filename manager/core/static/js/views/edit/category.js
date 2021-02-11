class Category extends Image{
	constructor(id){
		super(id);
		this.model = 'category';
		jQuery('.meta textarea').redactor({
				plugins: ['source'],
			});
		$('#promList .ui-icon-trash').on('click',this.deleteProm);
		$('#prom').on('keypress input paste',this.addProm);
		$('#promid').on('keypress',this.renderProm);
	}
	renderProm(event){
		if(event.keyCode == 13){
			var div = create('div');
			var PromID = $('#prom').value;
			var template = `<span class="ui-icon ui-icon-trash">X</span>
							<span>&nbsp;${PromID}</span>
							<span>&nbsp;${this.value}</span>
							<input type="hidden" name="proms[]" value="${PromID}|${this.value}">`;
			div.html(template);
			div.find('.ui-icon-trash')[0].on('click',view.deleteProm);
			$('#promList').append(div);
			$('#prom').value = '';
			this.value = '';
		}
	}
	addProm(event){
		if(this.value.length >= 3){
			var input = this;
			if(window.div){
				div.remove();
			}
			http.action = function(){
				var div = create('div');
				div.set('class','variants');
				for(var i=0;i<http.json.length;i++){
					var item = create('div');
					item.html(http.json[i]['repr']);
					item.id = http.json[i]['pk'];
					item.on('click',function(){
						input.value = this.first().text();
						input.name = this.id;
						$('.variants')[0].remove();
					});
					div.append(item);
				};
				input.parent().append(div);
				$('.variants').on('click',function(){this.remove()});
			};
			http.get('/ajax_select/ajax_lookup/prom?term='+this.value);
		}
	}
	deleteProm(){
		this.parent().remove();
		$('#save').removeAttr('disabled');
	}
}