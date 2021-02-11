function category(){
	$('#pic img').on('click',function(){
		input = $('#pic input')[0];
		input.on('change',function(){
			file = this.files[0];
			reader = new FileReader();
			reader.onload = function(e){
				image = $('#pic img')[0];
				image.src = e.target.result;
			};
			reader.readAsDataURL(file);
		});
		input.click();
	});
	$('#pic .remove').on('click',function(){
		if(confirm('Точн?')){
			http.func = function(){
				if(http.json.result){
					$('#pic img')[0].src = '/media/data/no_image_new.jpg';
				}
			};
			http.get('/category/pic/'+this.get('item-id')+'/delete');
		}
	});
	$('#delete').on('click',function(){
		if(confirm('Вы уверены что хотите удалить это?')){
			url = '/'+this.get('model')+'/delete/'+this.get('item-id');
			http.func = function(){
				if(http.json.result){
					load('/category/list','categories');
				}
			};
			http.get(url);
		}
	});
	$('main form *').on('change select input',function(){
		$('#save').removeAttr('disabled');
	});
	$('#id_name').on('input',function(){
		$('h1').text(this.value);
	});
	$('#save').on('click',function(){
		if(!this.get('disabled')){
			http.func = function(){
				if(http.json.result){
					http.alert('Сохранено успешно.');
					if(http.json.href){
						location.href = http.json.href;
						categories();
					}
				}else{
					errors = '';
					for(error in http.json.errors){
						errors += error + '<br>' + http.json.errors[error] + '<br>';
					}
					errors += http.json.nonferrs + '<br>';
					http.alert(errors);
				}
			};
			url = '/' + this.get('model') + '/category/save/' + this.get('item-id');
			http.post(url,$('#item form').serialize());
		}
	});
	$('#browse').on('click',function(){
		if(!this.get('slug')){
			http.alert('Нету URL');
			return false;
		}else{
			location.href = this.get('slug');
		}
	});
	jQuery('#id_description').redactor({
			plugins: ['source'],
			imageUpload: '/redactor/upload/image/'
		});
	$('#proms .ui-icon-trash').on('click',function(){
		prom = this;
		http.func = function(){
			if(http.json.result){
				prom.parent().remove();
			}
		};
		http.get('/pc/delete/'+this.get('item-id'));
	});
	$('#prom').on('keypress input paste',function(event){
		if(this.value.length >= 3){
			input = this;
			if(window.div){
				div.remove();
			}
			http.func = function(){
				div = create('div');
				div.set('class','result');
				for(i=0;i<http.json.length;i++){
					item = create('div');
					item.html(http.json[i]['repr']);
					item.id = http.json[i]['pk'];
					item.on('click',function(){
						input.value = this.first().text();
						input.name = this.id;
						div.remove();
					});
					div.append(item);
				};
				input.parent().append(div);
			};
			http.get('/ajax_select/ajax_lookup/prom?term='+this.value);
		}
	});
	$('#promid').on('keypress',function(event){
		if(event.keyCode == 13){
			input = this;
			data = new FormData();
			data.append('prom',$('#prom').name);
			data.append('prom_category_id',input.value);
			data.append('category',$('#save').get('item-id'));
			http.func = function(){
				if(http.json.result){
					div = create('div');
					div.set('class','prom results_on_deck');
					x = create('span');
					x.set('class','ui-icon ui-icon-trash');
					x.set('item-id',http.json.id);
					x.html('X');
					x.on('click',function(){
						prom = this;
						http.func = function(){
							if(http.json.result){
								prom.parent().remove();
							}
						};
						http.get('/pc/delete/'+this.get('item-id'));
					});
					prom_id = create('span');
					prom_id.html(' '+$('#prom').value);
					prom = create('span');
					prom.html(' '+input.value);
					div.append(x);div.append(prom_id);div.append(prom);
					$('#proms').append(div);
					$('#prom').name = '';
					$('#prom').value = '';
					input.value = '';
				}
			};
			http.post('/prom/save',data);
		}
	});
}