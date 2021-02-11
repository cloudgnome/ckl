var timeout = false;

class List extends View{
	constructor(){
		super();
		this.url = new URL(location.href);

		$('#list-all').on('click',this.showAll);
		$('#pagination .step-links a').on('click',this.pagination);
		$('#check-all').on('click',this.checkAll);
		$('#head a').on('click',this.ordering);
		$('#items-search input').on('input paste keypress',this.search);
		$('.delete-list').on('click',this.delete);
		$('#add').on('click',function(event){
			router.get(this.get('href'),this.get('view'));
		});
		$('#filters *,#filters').on('click',function(event){
			event.stopPropagation();
		});
		$('#filter svg').on('click',this.showFilters);
		$('#filter form *').on('change',this.filter);
		$('#items-search .clear-search').on('click',this.clearSearch);
	}
	showAll(event){
		view.url.searchParams.set('all',true);
		var href = view.url.pathname + view.url.search;

		router.get(href,'reload','#items');

		event.stopPropagation();
		event.preventDefault();
		return false;
	}
	clearSearch(){
		var input = this.prev();
		if(input.value){
			input.value = '';
			view.url.searchParams.delete(input.get('name'));
			var href = view.url.pathname + view.url.search;

			router.get(href,'reload','#items');
		}
		this.hide();
	}
	filter(){
		var filters = $('#filters').serializeJSON();
		for(key of view.url.searchParams.keys()){
			view.url.searchParams.delete(key);
		}
		for(var key of Object.keys(filters)){
			view.url.searchParams.set(key,filters[key]);
		}
		router.get(view.url.pathname + view.url.search,'reload','#items');
	}
	showFilters(event){
		var form = $('#filters');
		if(form.style.display == 'grid'){
			form.hide();
		}else{
			form.grid();
		}
		event.stopPropagation();
	}
	delete(){
		var checkboxes = $('input[type=checkbox]');
		if(checkboxes.length){
			var data = [];
			for(var i=0;i<checkboxes.length;i++){
				if(checkboxes[i].checked && checkboxes[i].value*1){
					data.push(checkboxes[i].value);
				}
			}
			if(!data.length)
				return;
			else if(confirm('Are U sure?')){
				http.action = function(){
					if(http.json.result){
						for(i=0;i<checkboxes.length;i++){
							checkboxes[i].checked = false;
						}
						location.reload();
					}
				};
				http.post('/delete/'+this.get('model'),data);
			}
		}
	}
	ordering(){
		var ordering = this.get('ordering');
		if(!view.url.search.includes('o=-'))
			ordering = '-' + ordering;

		view.url.searchParams.set('o',ordering);
		var href = view.url.pathname + view.url.search;

		router.get(href,'reload','#items');
	}
	search(){
		if(this.value){
			var input = this;
			if(timeout)
				clearTimeout(timeout);
			timeout = setTimeout(function(){
				input.next().show();
				if(input.value)
					view.url.searchParams.set(input.name,input.value);
				else{
					view.url.searchParams.delete(input.name);
				}
				var href = view.url.pathname + view.url.search;

				router.get(href,'reload','#items');
			},500);
		}
	}
	checkAll(){
		var checkboxes = $('input[type=checkbox]');
		for(var i=0, n=checkboxes.length;i<n;i++) {
			checkboxes[i].checked = this.checked;
		}
	}
	pagination(event){
		view.url.searchParams.set('page',this.get('page'));
		var href = view.url.pathname + view.url.search;

		router.get(href,'reload','#items');
		event.stopPropagation();
	}
}
class Reload{
	constructor(){
		this.url = new URL(location.href);
		$('#list-all').on('click',this.showAll);
		$('#pagination .step-links a').on('click',this.pagination);
	}
	pagination(event){
		view.url.searchParams.set('page',this.get('page'));
		var href = view.url.pathname + view.url.search;

		router.get(href,'reload','#items');
		event.stopPropagation();
	}
	showAll(event){
		view.url.searchParams.set('all',true);
		var href = view.url.pathname + view.url.search;

		router.get(href,'reload','#items');

		event.stopPropagation();
		event.preventDefault();
		return false;
	}
	categoryAutocomplete(target){
		var category = $('#category');
		category.find('.variants')[0].hide();
		category.find('input')[0].value = target.text();
	}
	brandAutocomplete(target){
		var brand = $('#brand');
		brand.find('.variants')[0].hide();
		brand.find('input')[0].value = target.text();
	}
}