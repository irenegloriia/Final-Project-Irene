/*!
* Start Bootstrap - Stylish Portfolio v6.0.2 (https://startbootstrap.com/theme/stylish-portfolio)
* Copyright 2013-2021 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-stylish-portfolio/blob/master/LICENSE)
*/


window.addEventListener('DOMContentLoaded', event => {

    const sidebarWrapper = document.getElementById('sidebar-wrapper');
    let scrollToTopVisible = false;
    // Closes the sidebar menu
    const menuToggle = document.body.querySelector('.menu-toggle');
    menuToggle.addEventListener('click', event => {
        event.preventDefault();
        sidebarWrapper.classList.toggle('active');
        _toggleMenuIcon();
        menuToggle.classList.toggle('active');
    })

    // Closes responsive menu when a scroll trigger link is clicked
    var scrollTriggerList = [].slice.call(document.querySelectorAll('#sidebar-wrapper .js-scroll-trigger'));
    scrollTriggerList.map(scrollTrigger => {
        scrollTrigger.addEventListener('click', () => {
            sidebarWrapper.classList.remove('active');
            menuToggle.classList.remove('active');
            _toggleMenuIcon();
        })
    });

    function _toggleMenuIcon() {
        const menuToggleBars = document.body.querySelector('.menu-toggle > .fa-bars');
        const menuToggleTimes = document.body.querySelector('.menu-toggle > .fa-times');
        if (menuToggleBars) {
            menuToggleBars.classList.remove('fa-bars');
            menuToggleBars.classList.add('fa-times');
        }
        if (menuToggleTimes) {
            menuToggleTimes.classList.remove('fa-times');
            menuToggleTimes.classList.add('fa-bars');
        }
    }

    // Scroll to top button appear
    document.addEventListener('scroll', () => {
        const scrollToTop = document.body.querySelector('.scroll-to-top');
        if (document.documentElement.scrollTop > 100) {
            if (!scrollToTopVisible) {
                fadeIn(scrollToTop);
                scrollToTopVisible = true;
            }
        } else {
            if (scrollToTopVisible) {
                fadeOut(scrollToTop);
                scrollToTopVisible = false;
            }
        }
    })
})

function fadeOut(el) {
    el.style.opacity = 1;
    (function fade() {
        if ((el.style.opacity -= .1) < 0) {
            el.style.display = "none";
        } else {
            requestAnimationFrame(fade);
        }
    })();
};

function fadeIn(el, display) {
    el.style.opacity = 0;
    el.style.display = display || "block";
    (function fade() {
        var val = parseFloat(el.style.opacity);
        if (!((val += .1) > 1)) {
            el.style.opacity = val;
            requestAnimationFrame(fade);
        }
    })();
};

function validatelink(){
    a = document.getElementById("username").value; 
    if (a != "") {
        document.getElementById("username").style.color = "Green";
        document.getElementById("username").innerHTML = "<strong>V</strong>"
        return true;
    } else {
        document.getElementById("username").style.color = "Red";
        document.getElementById("username").innerHTML = "<strong>X</strong>"
        return false;
    }
}


// var firebaseConfig = {
//         apiKey: "AIzaSyAeLzgjzy_LV_bpDck064AEUZ2vRf91ka4",
//         authDomain: "final-project-9e2cc.firebaseapp.com",
//         databaseURL: "https://final-project-9e2cc-default-rtdb.asia-southeast1.firebasedatabase.app",
//         projectId: "final-project-9e2cc",
//         storageBucket: "final-project-9e2cc.appspot.com",
//         messagingSenderId: "816416542969",
//         appId: "1:816416542969:web:6275bacdd4d2aa5e54d228",
//         measurementId: "G-EC494EPBMD"
//       };
//       // Initialize Firebase
//       firebase.initializeApp(firebaseConfig);
//       firebase.analytics();
//   var berita = firebase.database().ref("berita/")
//   var link = firebase.database().ref("link/")

//     berita.on('child_added',(data) => {
//       $( 'h1' ).remove()
//     // label = str.substring(msg.length - n)
//     // pesan = str.substring(0,msg.length - n)
//     // console.log("label = "+msg+typeof msg)
//     // console.log("label = "+label+typeof label)
//     // console.log("label = "+pesan+typeof pesan)
//         $( 'div.message_holder2' ).prepend( '<div class="msg_bbl"><b style="color: #000">'+data.val()['hasil']+'</b>'+'<br>'
//         +data.val()['judul']+'<br>'+data.val()['link']+'</div>')
//         $( 'div.msg_bbl2' ).remove()
//         $( 'div.message_holder' ).append( '<div class="msg_bbl2"><b style="color: #000">'+data.val()['hasil']+'</b>'+'<br>'
//         +data.val()['judul']+'<br>'+data.val()['berita']+'</div>')

//     })
//   function myFunction() {
//     a = document.getElementById("username").value;
//     console.log(a)

//     // berita.push({
//     //   link : a,
//     //   title : msg.judul,
//     //   label : msg.hasil,
//     //   news : msg.berita
//     // })
//     link.set({
//       berita : a
//     })
//     // berita.on('child_added',(data) => {
//     //   $( 'h1' ).remove()
//     // // label = str.substring(msg.length - n)
//     // // pesan = str.substring(0,msg.length - n)
//     // // console.log("label = "+msg+typeof msg)
//     // // console.log("label = "+label+typeof label)
//     // // console.log("label = "+pesan+typeof pesan)
//     //     $( 'div.message_holder' ).append( '<div class="msg_bbl"><b style="color: #000">'+data.val()['hasil']+'</b>'+'<br>'
//     //     +data.val()['judul']+'<br>'+data.val()['berita']+'</div>')

//     // })
   
//   }

