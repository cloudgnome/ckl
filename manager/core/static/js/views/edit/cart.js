var vactive;
class Cart{
	constructor(){
		$('.remove').on('click',this.remove);
		$('#add-product').on('click',this.add);
		$('input[name="qty"], input[name="price"]').on('change',this.calculate_item);
		this.total = $('#total .sum')[0];
		this.totalSum = parseInt(this.total.text());
		this.discount = $('#discount .sum')[0];
		this.removeList = [];
		$('body').on('click',this.hide_variants);
	}
	hide_variants(){
		if($('#order-items .variants').length)
			$('#order-items .variants')[0].parent().parent().remove();
	}
	calculate(){
		var total = 0;
		var discount = 0;
		var items = $('#order-items .item');
		items.each(function(item){
			var qty = parseInt(item.find('input[name="qty"]')[0].value);
			var price = parseInt(item.find('input[name="price"]')[0].value);
			total += price * qty;
			discount += price * qty;
		});
		if(total > 5000){
			total = 0;
			discount = 0;
			items.each(function(item){
				var qty = parseInt(item.find('input[name="qty"]')[0].value);
				var price = parseInt(item.find('input[name="price"]')[0].value);
				var opt = parseInt(item.find('input[name="price"]')[0].get('opt'));
				total += opt * qty;
				discount += price * qty;
			});
		}

		if(discount > total){
			discount = discount - total;
		}else{
			discount = '0';
		}

		this.discount.text(discount);
		this.totalSum = total;
		this.total.text(total);
	}
	calculate_item(){
		var item = this.parent().parent();
		var qty = parseInt(item.find('input[name="qty"]')[0].value);
		var price = parseInt(item.find('input[name="price"]')[0].value);
		item.find('.total').text(qty * price + ' грн.');
		view.cart.calculate();
	}
	remove(){
		view.cart.removeList.push(this.get('item-id'));
		this.parent().parent().remove();
		view.cart.calculate();
		$('#save').removeAttr('disabled');
	}
	add(event){
		var div = create('div');
		div.set('class','item visible');
		div.html(templates.cart_new_item());
		div.find('.remove').on('click',function(event){
			this.parent().parent().remove();
			event.stopPropagation();
			return false;
		});
		View.variants(div,'product',view.cart.save);
		$('#order-items').append(div);
		event.stopPropagation();
		return false;
	}
	save(event){
		var item = $('#order-items .variants')[0].parent().parent();
		var id = event.target.get('item-id');
		if($(`.item[product-id="${id}"]`).length){
			var qty = $(`.item[product-id="${id}"] input[name="qty"]`)[0];
			qty.value++;
			item.remove();
		}else{
			item.html(templates.add(event.target));
			item.find('.image')[0].html(event.target.get('image'));
			item.find('input[name="qty"], input[name="price"]').on('change',view.cart.calculate_item);
			item.set('product-id',event.target.get('item-id'));
			item.find('.remove').on('click',view.cart.remove);
		}
		item.removeClass('visible');
		view.cart.calculate();
		return false;
	}
}