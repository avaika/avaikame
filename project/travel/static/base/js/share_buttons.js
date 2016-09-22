$(document).ready(function(){
    $('.avaika-share-item').click(bindFunction);
    var Share = {
        vkontakte: function(params) {
            url  = 'http://vkontakte.ru/share.php?';
            url += 'url='          + encodeURIComponent(params.url);
            url += '&title='       + encodeURIComponent(params.name);
            url += '&description=' + encodeURIComponent(params.description);
            url += '&imageurl='       + encodeURIComponent(params.image);
            url += '&noparse=true';
            Share.popup(url);
        },
        odnoklassniki: function(params) {
            url  = 'http://www.odnoklassniki.ru/dk?st.cmd=addShare&st.s=1';
            url += '&st.comments=' + encodeURIComponent(params.description);
            url += '&st._surl='    + encodeURIComponent(params.url);
            Share.popup(url);
        },
        facebook: function(params) {
            url  = 'http://www.facebook.com/sharer.php?s=100';
            url += '&p[title]='     + encodeURIComponent(params.name);
            url += '&p[summary]='   + encodeURIComponent(params.description);
            url += '&p[url]='       + encodeURIComponent(params.url);
            url += '&p[images][0]=' + encodeURIComponent(params.image);
            Share.popup(url);
        },
        twitter: function(params) {
            url  = 'http://twitter.com/share?';
            url += 'text='      + encodeURIComponent(params.name);
            url += '&url='      + encodeURIComponent(params.url);
            Share.popup(url);
        },
        google: function(params) {
            url  = 'https://plus.google.com/share?';
            url += 'url='          + encodeURIComponent(params.url);
            Share.popup(url)
        },

        me : function(el){
            console.log(el.href);
            Share.popup(el.href);
            return false;
        },
        popup: function(url) {
            window.open(url,'','toolbar=0,status=0,width=626,height=436');
        }
    };
    function bindFunction(e){
        var site = $('.avaika-share').data('site');
        var params = [];
        var e = e.target;
        var title = $(e).attr('title');
        params.name = $(e).data('article');
        params.url = $(e).data('link');
        params.image = site + '/' + $(e).data('image');
        params.description = "share" + params.url;
        Share[title](params)
    }
})
