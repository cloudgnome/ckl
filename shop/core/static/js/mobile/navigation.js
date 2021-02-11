class Navigation{
    constructor(){
        this.touchStartPositionX;
        this.touchStartPositionY;
        this.verbose = false;
        this.touchEndPositionX = 0;
        this.touchEndPositionY = 0;
        this.active = false;

        $('#navigation_toggle').on('click',function(){
            $('#navigation').active();
        });

        $('#navigation #navCategories > div,#navigation .children > div,#navigation .sub > .parent,#navigation .image').on('click',this.sub.bind(this));

        $('#navigation').on('touchstart',this.touchStart.bind(this));
        $('#navigation').on('touchend',this.touchEnd.bind(this));
    }
    static scroll(){
        window.scrollTo({top:$('#navigation .head')[0].offsetTop - 58,behavior: 'smooth'});
    }
    static toggle(){
        if($('#categories-container').children.length){
            if(window.scrollY > $('#navigation').height() || $('#categories-container').style.display == 'none'){
                Navigation.scroll();
                $('#categories-container').show();
            }else{
                $('#categories-container').hide();
            }
        }else{
            var that = this;
            http.action = function(){
                $('#categories-container').html(http.response);
                $('#categories-container').show();
                $('main .container > .loading').active();
                that.active = true;
                Navigation.scroll();
                pageObject.navigation = new Navigation();
            };
            $('main > .container > .loading').active();
            http.get('/categories');
        }
    }
    touchStart(e){
        if(e.changedTouches){
            this.touchStartPositionX = e.changedTouches[0].clientX;
            this.touchStartPositionY = e.changedTouches[0].clientY;
        }
        else{
            this.touchStartPositionX = e.clientX;
            this.touchStartPositionY = e.clientY;
        }

        if(this.verbose){
            log('touchStartPositionX is: ' + this.touchStartPositionX);
            log('touchStartPositionY is: ' + this.touchStartPositionY);
        }
    }
    touchEnd(e){
        this.touchEndPositionX = e.changedTouches[0].clientX;
        this.touchEndPositionY = e.changedTouches[0].clientY;

        if(this.verbose){
            log('touchEndPositionX is: ' + this.touchEndPositionX);
            log('touchEndPositionY is: ' + this.touchEndPositionY);
        }

        var diffX = this.touchEndPositionX - this.touchStartPositionX;
        var diffY = this.touchEndPositionY - this.touchStartPositionY;

        if(this.touchEndPositionX != this.touchStartPositionX && diffX > 100 && diffY < 50){
            this.back();
        }
    }
    back(){
        var last = $('#navigation .sub.active').last();
        last.removeClass('active');
        last.prev().removeClass('active');

        this.changeHeight();
    }
    changeHeight(){
        var last = $('#navigation .sub.active').last();
        if(!last)
            return;
        var h = last.height();
        $('#navigation #navCategories')[0].css('height',h + 'px');
    }
    sub(event){
        if(event.target.hasClass('image')){
            event.target.parent().click();
            event.stopPropagation();
            event.preventDefault();
            return false;
        }

        if(event.target.find('.sub').length && event.target.find('.sub')[0].hasClass('active'))
            return false;

        var sub = event.target.find('.sub');

        if(sub.length){
            $('.nav-bg.active').removeClass('active');
            setTimeout(function(){
                event.target.find('.nav-bg')[0].active();
            },300);
        }

        if(sub.length)
            sub[0].active();
        else{
            var a = event.target.find('a');
            if(a.length)
                a[0].click();
        }
        if(sub.length){
            this.changeHeight();
        }
    }
}