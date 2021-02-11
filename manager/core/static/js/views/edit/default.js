class Page extends Edit{
	constructor(id){
		super(id);
		this.model = 'Page';
		jQuery('.meta textarea').redactor({
				plugins: ['source'],
			});
	}
}
class City extends Edit{
	constructor(id){
		super(id);
		this.model = 'City';
		jQuery('.description textarea').redactor({
				plugins: ['source'],
			});
	}
}
class TigresCategory extends Edit{
	constructor(id){
		super(id);
		this.model = 'TigresCategory';
	}
}
class Featured extends Edit{
	constructor(id){
		super(id);
		this.model = 'Featured';
	}
}
class Tigres extends Edit{
	constructor(id){
		super(id);
		this.model = 'Tigres';
	}
}
class Site extends Edit{
	constructor(id){
		super(id);
		this.model = 'Site';
	}
}
class GoogleFeed extends Edit{
	constructor(id){
		super(id);
		this.model = 'GoogleFeed';
	}
}
class Settings extends Image{
	constructor(id){
		super(id);
		this.model = 'Settings';
	}
}
class Language extends Image{
	constructor(id){
		super(id);
		this.model = 'Language';
	}
}
class Percent extends Edit{
	constructor(id){
		super(id);
		this.model = 'Percent';
	}
}
class BelesCategory extends Edit{
	constructor(id){
		super(id);
		this.model = 'BelesCategory';
	}
}
class Review extends Edit{
	constructor(id){
		super(id);
		this.model = 'Review';
		jQuery('#id_description').redactor({
				plugins: ['source'],
			});
	}
}
class Robots extends Edit{
	constructor(id){
		super(id);
		this.model = 'Robots';
	}
}
class Sms extends Edit{
	constructor(id){
		super(id);
		this.model = 'Sms';
	}
}
class Article extends Edit{
	constructor(id){
		super(id);
		this.model = 'Article';
		jQuery('.meta textarea').redactor({
				plugins: ['source'],
			});
	}
}
class Slider extends Edit{
	constructor(id){
		super(id);
		this.model = 'Slider';
	}
}
class Offer extends Edit{
	constructor(id){
		super(id);
		this.model = 'Offer';
	}
}
class Popular extends Edit{
	constructor(id){
		super(id);
		this.model = 'Popular';
	}
}
class Special extends Edit{
	constructor(id){
		super(id);
		this.model = 'Special';
	}
}
class User extends Edit{
	constructor(id){
		super(id);
		this.model = 'User';
	}
}
class Callback extends Edit{
	constructor(id){
		super(id);
		this.model = 'Callback';
	}
}
class Attribute extends Edit{
	constructor(id){
		super(id);
		this.model = 'Attribute';
		this.fgk = new OneToOne('value');
	}
}
class Prom extends Edit{
	constructor(id){
		super(id);
		this.model = 'Prom';
	}
}
class Slug extends Edit{
	constructor(id){
		super(id);
		this.model = 'Slug';
	}
}
class Redirect extends Edit{
	constructor(id){
		super(id);
		this.model = 'Redirect';
	}
}
class Meta extends Edit{
	constructor(id){
		super(id);
		this.model = 'Meta';
	}
}
class Currency extends Edit{
	constructor(id){
		super(id);
		this.model = 'Currency';
	}
}