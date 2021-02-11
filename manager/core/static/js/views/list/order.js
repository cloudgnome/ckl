class ListOrder extends List{
	constructor(){
		super();
		$('#tracking button').on('click',this.tracking);
		$('#sms').on('click',this.sms);
	}
	sms(){
		if(confirm('Are you sure?')){
			http.action = function(){
				if(http.json.result)
					http.alert('SMS разошлись успешно.');
			};
			http.get('/order/mass_sms');
		}
	}
	tracking(){
		http.action = function(){
			if(http.json.items){
				var items = http.json.items;
				for(var i in items){
					var item = items[i];
					var ul = create('ul');
					ul.html(`${i}:`);
					for(var value in item){
						var li = create('li');
						li.html(`${value}: ${item[value]}`);
						ul.append(li);
					}
					$('#tracking #result')[0].append(ul);
				}
				$('#tracking #result')[0].show();
			}else{
				http.alert('Нет таких заказов.');
			}
		};
		http.get('/order/tracking');
	}
}