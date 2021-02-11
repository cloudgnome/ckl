class Tag extends Image{
	constructor(id){
		super(id);
		this.model = 'tag';
		jQuery('.meta textarea').redactor({
				plugins: ['source'],
			});
	}
}