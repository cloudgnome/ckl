class Product extends Edit{
	constructor(id){
		super(id);
		this.model = 'Product';
		jQuery('.fieldset.meta textarea').redactor({
				plugins: ['source'],
				imageUpload: '/redactor/upload/image/'
			});
		jQuery('#id_description').redactor({
				plugins: ['source'],
				imageUpload: '/redactor/upload/image/'
			});
		this.images = new Gallery(this);
		this.fgk = new OneToOne('add_model');
	}
	extraAction(){
		if($('input[type="file"]').length){
			$('input[type="file"]').each(function(elem){
				elem.remove();
			});
		}
	}
}

class Storage extends Product{
	constructor(id){
		super(id);
		this.model = 'storage';
	}
	save(){
		super.save();
	}
	extraAction(){
		super.extraAction();
		var active = $('.load[model="product"]')[0];
		active.active();

		if(current)
			current.active();

		current = active;
	}
}

class Beles extends Product{
	constructor(id){
		super(id);
		this.model = 'beles';
	}
}