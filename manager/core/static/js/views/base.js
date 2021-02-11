class View{
	constructor(){
		this.deleteButton = $('#delete');
		$('svg').on('mouseover',function(){
			this.set('fill','#888');
		});
		$('svg').on('mouseout',function(){
			this.set('fill','#aaa');
		});
		$('#items .load').on('click',function(event){
			router.get(this.get('href'),this.get('view'),false,this.get('item-id'));

			event.preventDefault();
			event.stopPropagation();
			return false;
		});
	}
	static variants(div,model,action){
		div.find('input').on('paste keydown click',function(event){
			if(event.keyCode == 13){
				var item = div.find('.variants .active')[0];
				if(item){
					evnt = {};
					evnt.target = item;
					action(evnt);
				}
				event.stopPropagation();
				return false;
			}
			if(event.keyCode == 38){
				if(!vactive){
					vactive = div.find('.variants')[0].last();
					vactive.addClass('active');
				}
				else{
					vactive.removeClass('active');
					if(vactive.prev()){
						vactive = vactive.prev();
					}
					else{
						vactive = div.find('.variants')[0].last();
					}
					vactive.addClass('active');
				}
				return false;
			}
			if(event.keyCode == 40){
				if(!vactive){
					vactive = div.find('.variants')[0].first();
					vactive.addClass('active');
				}
				else{
					vactive.removeClass('active');
					if(vactive.next()){
						vactive = vactive.next();
					}
					else{
						vactive = div.find('.variants')[0].first();
					}
					vactive.addClass('active');
				}
				return false;
			}
			if(timeout)
				clearTimeout(timeout);
			var input = this;
			timeout = setTimeout(function() {
				if(input.value && input.value.length >= 3){
					http.action = function(){
						var variants = div.find('.variants')[0];
						variants.html(http.text);
						variants.show();
						variants.find('div').on('click',action);
					};
					http.get(`/order_autocomplete/${input.value}`);
				}
			}, 500);
			event.stopPropagation();
			return false;
		});
	}
}