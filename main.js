
// Facebook share button

(function(d, s, id) {
  
  var js, fjs = d.getElementsByTagName(s)[0];

    if (d.getElementById(id)) return;
        js = d.createElement(s); js.id = id;
        js.src = "https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v3.0";
        fjs.parentNode.insertBefore(js, fjs);

    }(document, 'script', 'facebook-jssdk'));

// Twitter share script

window.twttr = (function(d, s, id) {
      var js, fjs = d.getElementsByTagName(s)[0],
        t = window.twttr || {};

      if (d.getElementById(id)) return t;
      js = d.createElement(s);
      js.id = id;
      js.src = "https://platform.twitter.com/widgets.js";
      fjs.parentNode.insertBefore(js, fjs);

      t._e = [];
      t.ready = function(f) {
        t._e.push(f);
      };

      return t;
    }(document, "script", "twitter-wjs"));

// Whatsapp share script
      function openWhatsApp() {  
      window.open('whatsapp://send?text=Check out this website to learn more about the Twitter activity of world leaders! https://whotweetswhat.works/index.html');  
      } 


