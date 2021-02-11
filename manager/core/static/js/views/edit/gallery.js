class Gallery{
	constructor(item){
		this.item = item;
		this.previewImage = $('#bigPhoto img')[0];
		this.fullSize = $('#bigPhoto');
		this.fullSize.on('click',function(){
			view.images.fullSize.hide();
			$('#bg').hide();
		});
		this.stop = false;
		this.images = $('#images');
		$('#plus').on('click',this.add);
		$('#images .remove').on('click',this.remove);
		$('#images img').on('click',this.preview);
		var that = this;
		jQuery('#images').sortable({
			placeholder: "state",
			items: "div:not(.not)",
			update: function(event){
				var ordering = {};
				var position = 1;
				$('#images .remove').each(function(elem){
					if(elem.get('item-id')){
						ordering[elem.get('item-id')] = position;
						position++;
					}
				});
				http.action = function(){};
				http.post(`/gallery/${that.item.model}/${view.id}/ordering`,ordering);
			},
			stop: function(){
				view.stop = true;
			}
		}).disableSelection();
	}
	preview(event){
		if(view.stop){
			view.stop = false;
			return;
		}
		var image = event.target;
		view.images.previewImage.set('src',image.get('original'));
		view.images.fullSize.css('display','flex');
		$('#bg').show();
	}
	remove(event){
		var parent = event.target.parent().parent();
		var agree = confirm('Удалить картину?');
		if(this.get('item-id') && agree){
			http.action = function(){
				parent.remove();
			};
			http.get(`/delete/gallery/${this.get('item-id')}`);
		}else if(agree)
			parent.remove();
		event.stopPropagation();
		return false
	}
	add(){
		var input = create('input');
		input.set('type','file');
		input.hide();
		view.images.input = input;
		view.images.images.before(input,2);
		input.on('change',view.images.render);
		input.click();
	}
	render(){
		var file = this.files[0];
		var reader = new FileReader();
		reader.onload = function(e){
			var div = create('div');
			div.set('class','image ui-sortable-handle');
			div.html('<div class="remove"><i class="fas fa-times"></i></div>');
			div.find('.remove')[0].on('click',view.images.remove);
			var image = create('img');
			image.src = e.target.result;
			image.set('original',e.target.result);
			image.on('click',view.images.preview);
			div.append(image);
			view.images.input.set('name','images');
			view.images.input.set('value',e.target.result);
			view.images.images.before(div,2);
		};
		reader.readAsDataURL(file);
	}
}