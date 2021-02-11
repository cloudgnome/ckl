http = new XMLHttpRequest();
body = $('body');
loading = create('div');
loading.hide();
loading.set('id','loading');
form = create('div');
form.hide();
form.set('id','form');
bg = create('div');
bg.hide();
bg.set('id','bg');
bg.on('click',function(){
	form.hide();
	this.hide();
});
body.append(bg);
body.append(form);
body.append(loading);
http.get = function(url){
	this.method = 'GET';
	this.url = url;
	this.request();
};
http.post = function(url,data){
	this.method = 'POST';
	this.url = url;
	this.data = data;
	this.request();
};
http.response = http.responseText;
http.request = function(){
	loading.show();
	this.open(this.method,this.url);
	if(this.method == 'POST'){
		if(this.data instanceof FormData){
			this.setRequestHeader("X-CSRFToken", cookie.get('csrftoken'));
		}
		else if(typeof this.data == 'object'){
			this.data = JSON.stringify(this.data);
			this.setRequestHeader("X-CSRFToken", cookie.get('csrftoken'));
			this.setRequestHeader("Content-Type", "application/json");
		}
		else{
			this.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
		}
	}
	this.setRequestHeader('X-Requested-With','XMLHttpRequest');
	this.onreadystatechange = function(){
		switch(this.readyState){
			case 4: 
				loading.hide();
				if(this.status == 200){
					if(this.getResponseHeader('Content-Type') == 'application/json'){
						try{
							this.json = JSON.parse(this.responseText);
						}catch(e){
							console.log(e);
						}
					}
					this.text = this.responseText;
					try{
						this.action();
					}catch(e){
						log(e);
						/*this.render();*/
					}
				}
				else{
					this.alert(this.status);
				}
				break;
		}
	};
	this.send(this.data);
};
http.render = function(json){
	if(this.json){
		form.html(JSON.stringify(this.json));
	}else{
		form.html(this.text);
	}
	form.show();
	form.top(form.offsetTop + 18 + 'px');
	bg.show();
	form.css('margin-left', window.width/2 - form.width()/2 + 'px');
};

httpAlert = create('div');
httpAlert.set('id','http-alert');
httpAlert.hide();
message = create('div');
message.set('id','message');
close = create('div');
close.set('class','close');
httpAlert.append(close);
httpAlert.append(message);
body.append(httpAlert);
timeout = false;
http.alert = function(text,scnds){
	if(!scnds)
		scnds = 3000;
	message.html(text);
	httpAlert.show();
	timeout = setTimeout(function(){httpAlert.hide()},scnds);
};
httpAlert.on('mouseover',function(){
	if(timeout)
		clearTimeout(timeout);
});
httpAlert.on('mouseout',function(){
	timeout = setTimeout(function(){httpAlert.hide()},3000);
});
close.on('click',function(){
	httpAlert.hide();
});
http.renderErrors = function(){
	text = '';
	errors = this.json.errors;
	for(error of errors){
		text += `${error}: ${JSON.stringify(errors[error])}` + '<br> <br>';
	}
	this.alert(text,10000)
};