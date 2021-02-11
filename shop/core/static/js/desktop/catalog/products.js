class Category extends Buy{
	constructor(){
		super();
		this.filter = new Filter(window.parameters);
		this.list();
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