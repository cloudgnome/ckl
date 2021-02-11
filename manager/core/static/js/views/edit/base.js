class Edit extends View{
	constructor(id){
		super();
		this.id = id;
		this.saveButton = $('#save');
		this.saveButton.on('click',this.save);
		this.deleteButton.on('click',this.delete);
		$('main form *').on('change select input',function(){
			$('#save').removeAttr('disabled');
		});
		$('#id_name,#id_user-name').on('input',function(){
			$('h1').text(this.value)
		});

		try{
			this.active = $('label[for="'+$('.tab:checked')[0].get('id')+'"]')[0];
			this.active.addClass('active');
			$('#item-menu label').on('click',this.menu);
		}catch(e){}
		try{
			this.activeLang = $('label[for="'+$('.meta .tab:checked')[0].get('id')+'"]')[0];
			this.activeLang.addClass('active');
			$('.fieldset.meta label').on('click',this.langMenu);
		}catch(e){}
		$('.autocomplete').each(function(elem){
			var model = elem.get('model');
			window['autocomplete_' + model] = new Autocomplete(model=model);
		});
	}
	menu(){
		if(view.active)
			view.active.removeClass('active');
		view.active = this;
		this.addClass('active');
	}
	langMenu(){
		if(view.activeLang)
			view.activeLang.removeClass('active');
		view.activeLang = this;
		this.addClass('active');
	}
	delete(){
		if(confirm('Удалить?')){
			http.action = function(){
				if(http.json.result){
					router.get(`/${view.model}/list`,'List');
				}
			};
			http.get(`/delete/${view.model}/${view.id}`);
		}
	}
	save(){
		if(!view.saveButton.get('disabled')){
			http.action = function(){
				if(http.json.result){
					http.alert('Сохранено успешно.');
					if(http.json && http.json.href){
						router.get(http.json.href,http.json.view,0,http.json.id);
					}
					view.extraAction();
				}else{
					var errors = '';
					for(var error in http.json.errors){
						errors += error + '<br>' + http.json.errors[error] + '<br>';
					}
					errors += http.json.nonferrs + '<br>';
					http.alert(errors,7000);
				}
			};
			if(view.id)
				var url = `/edit/${view.model}/${view.id}`;
			else{
				var url = `/add/${view.model}`;
			}
			http.post(url,$('#item form')[0].serializeJSON());
		}
	}
	extraAction(){
		
	}
}
class Image extends Edit{
	constructor(id){
		super(id);
		$('.pic').on('click',function(){this.find('input')[0].click()});
		$('.pic .remove').on('click',this.removeImage);
		$('.pic input').on('change',this.changeImage);
	}
	changeImage(){
		var file = this.files[0];
		var reader = new FileReader();
		var that = this;
		reader.onload = function(e){
			var image = that.prev();
			image.src = e.target.result;
			that.set('value', e.target.result);
			that.parent().removeClass('active');
		};
		reader.readAsDataURL(file);
	}
	removeImage(event){
		if(confirm('Точн?')){
			this.parent().find('img')[0].src = '/media/data/no_image_new.jpg';
			this.parent().find('input')[0].set('value','remove');
			$('#save').removeAttr('disabled');
		}
		event.stopPropagation();
		return false;
	}
}