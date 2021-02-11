var timeout;
class Order extends Edit{
	constructor(id){
		super(id);
		this.model = 'order';
		this.panel = $('#sms-panel');
		this.panelButtons = $('#sms-panel .buttons');
		this.cart = new Cart();
		this.address = $('#id_address').value;
		this.seats = $('#seats');
		this.product_names = this.collectNames();
		this.index = 0;

		this.OptionsSeat = [];

		$('#add-seat').on('click',this.addSeat.bind(this));
		$('#order-ttn .close').on('click',this.showFilters);

		$('#save').on('click',this.save);
		$('#make-ttn').on('click',this.ttn.bind(this));
		$('#sms').on('click',this.smsPanel);
		$('#sms-panel .buttons button').on('click',this.sms);
		$('#track').on('click',this.track);
		$('#id_delivery_type').on('change',this.delivery);
		$('#edit-filter svg').on('click',this.showFilters);
		$('#edit-filters *').on('click',function(event){
			event.stopPropagation();
			return false;
		});

		$('#edit-filters').on('click',function(event){
			event.stopPropagation();
			return false;
		});

		$('#id_city').on('input keyup paste',this.city);

		$('#id_departament').on('input keyup paste',function(){
			this.departament($('#id_delivery_type').value,$('input[name="city"]')[0].value);
		}.bind(this));

		var type = $('#id_delivery_type').value;
		if(type == 1 || type == 2){
			$('#city').show();
			$('#departament').show();
		}

		$('body').on('click',this.hide_variants);

		$('#id_city').on('click',function(event){
			var variants = $('#city .variants')[0];
			if(this.value && variants.children.length)
				variants.show();
			else{
				view.city(true);
			}
			event.stopPropagation();
			return false;
		});

		$('#id_departament').on('click',function(event){
			var variants = $('#departament .variants')[0];
			if(this.value && variants.children.length)
				variants.show();
			else{
				view.departament($('#id_delivery_type').value,$('input[name="city"]')[0].value);
			}
			event.stopPropagation();
			return false;
		});

		$('#copyFIO').on('click',this.copyFIO);
	}
	collectNames(){
		var result = [];
		for(var i of $('#order-items .item .name')){
			result.push(i.text());
		}
		return result
	}
	calculateSeatCost(){
		var cost = this.cart.totalSum / $('#seats .seat').length;
		$('#seats input[name="cost"]').each(function(elem){
			elem.value = cost;
		});
	}
	addSeat(){
		var seat = getTemplate($('#seat'));
		this.seats.append(seat);
		this.calculateSeatCost();
		this.seats.find('.remove').on('click',this.removeSeat.bind(this));
		if(this.product_names[this.index])
			var name = this.product_names[this.index];
		else{
			var name = this.product_names[0];
		}
		$('#seats .seat input[name="description"]').last().value = name;
		$('#seats .seat input[name="weight"]').on('change',function(e){
			e.stopPropagation();
			e.preventDefault();
			return false;
		});
		$('#seats .seat input.calculate').on('change',this.calculateVolumeGeneral);
		this.index++;
	}
	calculateVolumeGeneral(){
		var res = 0;
		$('#seats .seat').each(function(seat){
			var h = seat.find('input[name="volumetricHeight"]')[0].value;
			var w = seat.find('input[name="volumetricWidth"]')[0].value;
			var l = seat.find('input[name="volumetricLength"]')[0].value;
			if(h && w && l){
				var volumeGenaral = (h * w * l) / 4000;
				res += volumeGenaral;
				seat.find('input[name="weight"]')[0].value = volumeGenaral;
			}
		});

		$('#order-ttn input[name="volume"]')[0].value = res;
	}
	removeSeat(e){
		if(e.target.parent().hasClass('remove')){
			e.target.parent().click();
			return false;
		}
		e.target.parent().remove();
		this.calculateSeatCost();
	}
	collectSeats(){
		var result = [];
		$('#seats .seat').each(function(seat){
			result.push(seat.serializeJSON());
		});
		return result;
	}
	copyFIO(){
		var fio = `${$('#id_lname').value} ${$('#id_name').value} ${$('#id_sname').value}`;
		navigator.clipboard.writeText(fio).then(function() {
			/* clipboard successfully set */
		}, function() {
			/* clipboard write failed */
		});
	}
	hide_variants(){
		if($('#id_city').value && $('#city .variants')[0].style.display == 'block')
			$('#city .variants')[0].hide();
		if($('#id_departament').value && $('#departament .variants')[0].style.display == 'block')
			$('#departament .variants')[0].hide();
	}
	showFilters(event){
		$('#order-ttn').active();
		$('#bg').active();
		event.stopPropagation();
		return false;
	}
	delivery(){
		var type = $('#id_delivery_type').value;

		$('#city').hide();
		$('#departament').hide();
		$('input[name="city"]')[0].value = '';
		$('#id_city').value = '';
		$('input[name="departament"]')[0].value = '';
		$('#id_departament').value = '';

		if(type != 3 && $('#address') && !Array.isArray($('#address')))
			$('#address').remove();

		if(type == 1 || type == 2){
			$('#city').show();
			$('#departament').show();
		}
		if(type == 3){
			var div = create('div');
			var address = templates.address();
			div.html(address);
			div.set('id','address');
			$('#order-info').afterOf(div,$('#id_payment_type').parent());
		}
	}
	city(click){
		if(timeout)
			clearTimeout(timeout);

		var type = $('#id_delivery_type').value;
		var city = $('#id_city').value;

		timeout = setTimeout(function(){
			if(city && city.length > 1){
				http.action = function(){
					$('#city').show();
					$('#city .variants')[0].clear();
					$('#city .variants')[0].html(templates.variants(http.json));
					$('#city .variant').on('click',function(){
						$('#id_city').value = this.text();
						$('input[name="city"]')[0].value = this.get('value');
						view.departament(type, this.get('value'));
					});
					for(var item of http.json){
						if(item.address == $('#id_city').value && !click){
							$('input[name="city"]')[0].value = item.id;
							view.departament(type, item.id);
							return;
						}
					}
					$('#city .variants')[0].show();
				};
				http.get(`/delivery/city/${type}/${city}`);
			}
		},500);
	}
	departament(type, city_id, value){
		if(!value)
			var value = $('#id_departament').value;
		http.action = function(){
			$('#departament').show();
			$('#departament .variants')[0].clear();
			$('#departament .variants')[0].show();
			$('#departament .variants')[0].html(templates.variants(http.json));
			$('#departament .variant').on('click',function(){
				$('#id_departament').value = this.text();
				$('input[name="departament"]')[0].value = this.get('value');
			});
		};
		http.get(`/delivery/departament/${type}/${city_id}/${value}`);
	}
	save(e){
		http.action = function(){
			if(http.json.result){
				view.cart.removeList = [];
				if(http.json.href){
					router.get(http.json.href,'order','',http.json.id);
				}else{
					http.alert('Сохранен успешно.',3000);
				}
			}else if(http.json.errors){
				var errors = '';
				for(var error in http.json.errors){
					errors += error + '<br>' + http.json.errors[error] + '<br>';
				}
				errors += http.json.nonferrs + '<br>';
				http.alert(errors,7000);
			}
		};

		if(!view.id){
			var url = '/add/order';
		}else{
			var url = '/edit/order/' + view.id;
		}

		var items = [];
		$('#order-items .item').each(function(item){
			var qty = parseInt(item.find('input[name="qty"]')[0].value);
			var price = parseInt(item.find('input[name="price"]')[0].value);
			items.push({id:item.get('product-id'),qty:qty,price:price});
		});

		var data = $('form').serializeJSON();
		data['items'] = items;
		data['remove'] = view.cart.removeList;

		http.post(url,data);

		e.stopPropagation();
		e.preventDefault();
		return false;
	}
	ttn(e){
		http.action = function(){
			if(http.json.ref){
				/*win = window.open("https://my.novaposhta.ua/orders/printDocument/orders[]/"+http.json.ref+"/type/html/apiKey/a5d31efa7bc0f7b138a06a130d8e5327",'_blank');
				win.focus();
				win.print();*/
				$('#id_status').value = 8;
				http.alert('TTH создана');
			}else if(http.json && http.json.errors){
				http.renderErrors();
			}
		};

		var data = {};
		data['order'] = $('#order').serializeJSON();
		data['ttn'] = $('#order-ttn').serializeJSON();
		data['seats'] = this.collectSeats();
		data['total'] = $('#total .sum').text();

		http.post('/order/ttn',data);
	}
	smsPanel(event){
		view.panel.active();
		view.panelButtons.active();
		event.stopPropagation();
	}
	sms(){
		var summ = null;
		var delivery_type = $('#id_delivery_type');
		if(delivery_type.value == 3)
			summ = prompt('Введи сумму');
		if(delivery_type.value == 3 && !summ)
			return false;
		var type = this.get('id');
		if(type == 'ttn' && !$('#id_ttn').value.length){
			http.alert('Создайте ТТН');
			return;
		}
		http.action = function(){
			if(http.json.result){
				http.alert('Отправлена.');
			}
		};
		if(summ)
			http.get(`/order/sms/${view.id}/${type}/${summ}`);
		else{
			http.get(`/order/sms/${view.id}/${type}`);
		}
	}
	track(){
		http.action = function(){
			http.render(http.json);
		};
		http.get(`/order/track/${view.id}`);
	}
}