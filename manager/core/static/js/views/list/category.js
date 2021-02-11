class CategoryList{
	constructor(){
		$('.parent-arrow').on('click',function(){
			this.active();
		});
		jQuery('#categories .category').sortable({
			placeholder: "state",
			items: "div:not(.not)",
			update: function(event){
				var items = jQuery('#categories .category').sortable('toArray');
				log(items);
			},
		}).disableSelection();
		$('#add').on('click',function(event){
			router.get(this.get('href'),this.get('view'));
		});
	}
}