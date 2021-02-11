function login(){
	$('body').on('keypress',function(event){
		if(event.keyCode == 13){
			login(event);
		}
	});
	$('#login').on('click',function(){
		login();
	});
	function login(){
		http.action = function(){
			if(http.json && http.json.next)
				location.href = http.json.next;
			else if(http.errors){
				http.alert(http.errors);
			}
		};
		data = $('#login-form').serialize();
		data.append('next',location.pathname);
		http.post('/user/signin/',data);
	}
}