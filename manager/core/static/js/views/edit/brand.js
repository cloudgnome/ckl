class Brand extends Image{
	constructor(id){
		super(id);
		this.model = 'brand';
		jQuery('.meta textarea').redactor({
				plugins: ['source'],
			});
	}
}