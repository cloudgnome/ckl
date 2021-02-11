class Home{
	constructor(){
		if(storage.limit)
			$('#settings #limit')[0].value = storage.limit;
		$('#settings #limit').on('keypress paste',this.limit);

		if(storage.merchant_min_price)
			$('#merchant_min_price').value = storage.merchant_min_price;
		$('#merchant_min_price').on('keypress paste',this.merchant_min_price);

		$('#merchant button').on('click',this.create_merchant_file);

		if(storage.facebook_merchant_min_price)
			$('#facebook_merchant_min_price').value = storage.facebook_merchant_min_price;
		$('#facebook_merchant_min_price').on('keypress paste',this.facebook_merchant_min_price);

		$('#merchant button').on('click',this.create_merchant_file);

		$('#facebook_merchant button').on('click',this.create_facebook_merchant_file);

		$('#prices button').on('click',this.start_prices_sync);
		$('#cache .click').on('click',this.drop_cache);
		$('#stock button').on('click',this.stock);
		$('#rozetka button').on('click',this.export);
		$('#hotline button').on('click',this.export1);
		$('#sync_prices button').on('click',this.prices);
		$('#stock input').on('keypress paste',this.stock_brand);
	}
	drop_cache(){
		if(!confirm('Впевнені?'))
			return;
		http.action = function(){
			if(http.json && http.json.result)
				http.alert('Кэш очищен.');
		};
		http.get('/drop_cache');
	}
	create_merchant_file(){
		http.action = function(){
			if(http.json && http.json.result)
				http.alert('Задача поставлена в очередь');
		};
		http.get('/merchant/create?min_price=' + storage.merchant_min_price);
	}
	create_facebook_merchant_file(){
		http.action = function(){
			if(http.json && http.json.result)
				http.alert('Задача поставлена в очередь');
		};
		http.get('/merchant/create/facebook?min_price=' + storage.facebook_merchant_min_price);
	}
	start_prices_sync(){
		http.action = function(){
			if(http.json && http.json.result)
				http.alert('Задача поставлена в очередь');
		};
		http.get('/prices/sync');
	}
	merchant_min_price(){
		if(timeout)
			clearTimeout(timeout);
		var that = this;
		timeout = setTimeout(function(){
			storage.merchant_min_price = that.value;
		},500);
	}
	facebook_merchant_min_price(){
		if(timeout)
			clearTimeout(timeout);
		var that = this;
		timeout = setTimeout(function(){
			storage.facebook_merchant_min_price = that.value;
		},500);
	}
	stock(){
		http.action = function(){
			if(http.json && http.json.result)
				http.alert('Задача поставлена в очередь');
		};
		http.get('/sync/stock');
	}
	export(){
		http.action = function(){
			if(http.json && http.json.result)
				http.alert('Задача поставлена в очередь');
		};
		http.get('/sync/rozetka');
	}
	export1(){
		http.action = function(){
			if(http.json && http.json.result)
				http.alert('Задача поставлена в очередь');
		};
		http.get('/sync/hotline');
	}
	prices(){
		http.action = function(){
			if(http.json && http.json.result)
				http.alert('Задача поставлена в очередь');
		};
		http.get('/sync/prices');
	}
	stock_brand(){
		if(timeout)
			clearTimeout(timeout);
		var that = this;
		timeout = setTimeout(function(){
			storage.stock_brand = that.value;
		},500);
	}
	limit(){
		if(timeout)
			clearTimeout(timeout);
		var that = this;
		timeout = setTimeout(function(){
			storage.limit = that.value;
		},500);
	}
}