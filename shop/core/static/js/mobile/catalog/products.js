class Category extends Buy{
	constructor(){
		super();
		this.filter = new Filter(window.parameters);
		this.list();
		$('#filters label.dropdownButton').on('click',this.showFilter.bind(this));
		$('#filters .close').on('click',this.closeFilter.bind(this));
	}
	showFilter(e){
		var target = e.target;
		target.next().next().toggle();
		target.next().show();
		$('#bg').toggle();
		var closeButton = target.next();
		setTimeout(function(){
			closeButton.toggleClass('show');
		},100);
	}
	closeFilter(e){
		var closeButton = e.target;
		setTimeout(function(){
			closeButton.toggleClass('show');
			closeButton.hide();
		},100);
		closeButton.next().hide();
		$('#bg').hide();
	}
	list(){
		if(!storage.list)
			storage.list = 'grid';

		$(`#elementStyle i[type="${storage.list}"]`).addClass('active');
		$('main .items').toggleClass(storage.list);

		$('#elementStyle i').on('click',function(){
			var type = this.attr('type');
			$('main .items').toggleClass(storage.list);
			$('main .items').toggleClass(type);
			$('#elementStyle i.active').toggleClass('active');
			$(`#elementStyle i[type="${type}"]`).toggleClass('active');
			storage.list = type;
		});
	}
}

class Brand extends Category{
	constructor(){
		super();
	}
}

class Tag extends Category{
	constructor(){
		super();
	}
}
class Sale extends Category{
	constructor(){
		super();
	}
}
class Bestsellers extends Category{
	constructor(){
		super();
	}
}
class New extends Category{
	constructor(){
		super();
	}
}