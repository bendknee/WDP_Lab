// FB initiation function
window.fbAsyncInit = () => {
    FB.init({
        appId      : '2004678579769743',
        cookie     : true,
        xfbml      : true,
        version    : 'v2.11'
    });

    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            // the user is logged in and has authenticated your
            // app, and response.authResponse supplies
            // the user's ID, a valid access token, a signed
            // request, and the time the access token
            // and signed request each expire
            var uid = response.authResponse.userID;
            var accessToken = response.authResponse.accessToken;
            render(true)
        } else if (response.status === 'not_authorized') {
            // the user is logged in to Facebook,
            // but has not authenticated your app
            render(false)
        } else {
            // the user isn't logged in to Facebook.
            render(false)
        }
    });

};

// Call init facebook. default dari facebook
(function(d, s, id){
    var js, fjs = d.getElementsByTagName(s)[0];
    if (d.getElementById(id)) {return;}
    js = d.createElement(s); js.id = id;
    js.src = "https://connect.facebook.net/en_US/sdk.js";
    fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

// Fungsi Render, menerima parameter loginFlag yang menentukan apakah harus
// merender atau membuat tampilan html untuk yang sudah login atau belum
// Ubah metode ini seperlunya jika kalian perlu mengganti tampilan dengan memberi
// Class-Class Bootstrap atau CSS yang anda implementasi sendiri
const render = loginFlag => {
    if (loginFlag) {
        // Jika yang akan dirender adalah tampilan sudah login

        // Memanggil method getUserData (lihat ke bawah) yang Anda implementasi dengan fungsi callback
        // yang menerima object user sebagai parameter.
        // Object user ini merupakan object hasil response dari pemanggilan API Facebook.
        getUserData(user => {
            // Render tampilan profil, form input post, tombol post status, dan tombol logout
            $('#lab8').html(
            <!-- Navbar -->
            '<div class="w3-top">' +
                '<div class="w3-bar w3-theme-d2 w3-left-align w3-large">' +
                '<a class="w3-bar-item w3-button w3-hide-medium w3-hide-large w3-right w3-padding-large w3-hover-white w3-large w3-theme-d2" href="javascript:void(0);" onclick="openNav()"><i class="fa fa-bars"></i></a>' +
            '<a href="#" class="w3-bar-item w3-button w3-padding-large w3-theme-d4"><i class="fa fa-home w3-margin-right"></i>Logo</a>' +
            '<a onclick="facebookLogout()" class="w3-bar-item w3-button w3-hide-small w3-right w3-padding-large w3-hover-white" title="Logout"><img src='+ user.picture.data.url +' class="w3-circle" style="height:25px;width:25px" alt="Avatar"></a>' +
                '</div>' +
                '</div>' +

                <!-- Navbar on small screens -->
                '<div id="navDemo" class="w3-bar-block w3-theme-d2 w3-hide w3-hide-large w3-hide-medium w3-large">'+
                '<a href="#" class="w3-bar-item w3-button w3-padding-large">My Profile </a>'+
            '</div>'+

            <!-- Page Container -->
            '<div class="w3-container w3-content" style="max-width:1400px;margin-top:80px">'+
                <!-- The Grid -->
            '<div class="w3-row">'+
                <!-- Left Column -->
            '<div class="w3-col m3">'+
                <!-- Profile -->
                '<div class="w3-card w3-round w3-white">'+
                '<div class="w3-container">'+
                '<h4 class="w3-center">'+ user.name +'</h4>'+
            '<p class="w3-center"><img src='+ user.picture.data.url +' class="w3-circle" style="height:106px;width:106px" alt="Avatar"></p>'+
                '<hr>'+
                '<p><i class="fa fa-pencil fa-fw w3-margin-right w3-text-theme"></i>' + user.about + '</p>'+
            '<p><i class="fa fa-home fa-fw w3-margin-right w3-text-theme"></i>'+ user.email +'</p>'+
            '<p><i class="fa fa-birthday-cake fa-fw w3-margin-right w3-text-theme"></i>'+ user.gender +'</p>'+
            '</div>'+
            '</div>'+
            '<br>'+

            <!-- End Left Column -->
            '</div>'+

            <!-- Middle Column -->
            '<div class="w3-col m7">'+
            '<div class="w3-row-padding">'+
            '<div class="w3-col m12">'+
            '<div class="w3-card w3-round w3-white">'+
            '<div class="w3-container w3-padding">'+
            '<h6 class="w3-opacity">Social Media template by w3.css</h6>'+
            '<p id="postInput" contenteditable="true" class="w3-border w3-padding">What is on your mind?</p>'+
            '<button type="button" class="w3-button w3-theme" onclick="postStatus()"><i class="fa fa-pencil"></i> Post</button>'+
            '</div>'+
            '</div>'+
            '</div>'+
            '</div>'+

            <!-- End Middle Column -->
            '</div>'+

            <!-- End Grid -->
            '</div>'+

            <!-- End Page Container -->
            '</div>'+
            '<br>'+

            '<script>'+


            '</script>'
        );

        // Setelah merender tampilan di atas, dapatkan data home feed dari akun yang login
        // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
        // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
        // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
        getUserFeed(feed => {
            feed.data.map(value => {
                // Render feed, kustomisasi sesuai kebutuhan.
                if (value.message && value.story) {
                    $('#list').append(
                    '<div class="w3-container w3-card w3-white w3-round w3-margin"><br>'+
                    '<img src='+ user.picture.data.url +' alt="Avatar" class="w3-left w3-circle w3-margin-right" style="width:60px">'+
                    '<h4>'+ user.name +'</h4><br>'+
                    '<hr class="w3-clear">'+
                    '<p>'+ value.message +'</p>'+
                    '</div>'
                    );
                } else if (value.message) {
                    $('#list').append(
                        '<div class="w3-container w3-card w3-white w3-round w3-margin"><br>'+
                        '<img src='+ user.picture.data.url +' alt="Avatar" class="w3-left w3-circle w3-margin-right" style="width:60px">'+
                        '<h4>'+ user.name +'</h4><br>'+
                        '<hr class="w3-clear">'+
                        '<p>'+ value.message +'</p>'+
                        '</div>'
                    );
                } else if (value.story) {
                    $('#list').append(
                        '<div class="w3-container w3-card w3-white w3-round w3-margin"><br>'+
                        '<img src='+ user.picture.data.url +' alt="Avatar" class="w3-left w3-circle w3-margin-right" style="width:60px">'+
                        '<h4>'+ user.name +'</h4><br>'+
                        '<hr class="w3-clear">'+
                        '<p>'+ value.story +'</p>'+
                        '</div>'
                    );
                }
            });
        });
    });
    } else {
        // Tampilan ketika belum login
        $('#list').html('')
        $('#lab8').html(
            '<div style="text-align: center; margin-top: 24%">' +
            '<button class="btn btn-primary btn-lg login" onclick="facebookLogin()">Login with Facebook</button>' +
            '</div>'

        );
    }
};

const facebookLogin = () => {
    FB.login(function(response){
        console.log(response);
        render(true);
    }, {scope:'public_profile,user_posts,publish_actions,user_about_me,email'})

    // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan sudah login
    // ketika login sukses, serta juga fungsi ini memiliki segala permission yang dibutuhkan
    // pada scope yang ada. Anda dapat memodifikasi fungsi facebookLogin di atas.
};

const facebookLogout = () => {
    FB.getLoginStatus(function (response) {
        if (response.status === "connected") {
            FB.logout();
            render(false);
        }
    });
    // Pastikan method memiliki callback yang akan memanggil fungsi render tampilan belum login
    // ketika logout sukses. Anda dapat memodifikasi fungsi facebookLogout di atas.
};

// Method ini memodifikasi method getUserData di atas yang menerima fungsi callback bernama fun
// lalu merequest data user dari akun yang sedang login dengan semua fields yang dibutuhkan di
// method render, dan memanggil fungsi callback tersebut setelah selesai melakukan request dan
// meneruskan response yang didapat ke fungsi callback tersebut
// Apakah yang dimaksud dengan fungsi callback?
const getUserData = (fun) => {

    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            FB.api('/me?fields=id,name,about,email,gender,cover,picture.width(168).height(168)', 'GET', function(response){
                console.log(response);
                if (response && !response.error) {
                    /* handle the result */
                    picture = response.picture.data.url;
                    name = response.name;
                    userID = response.id;
                    fun(response);
                }
                else {
                    swal({
                        text: "Something went wrong",
                        icon: "error"
                    });
                }
            });
        }
    });
};

const getUserFeed = (fun) => {
    // Pastikan method ini menerima parameter berupa fungsi callback, lalu merequest data Home Feed dari akun
    // yang sedang login dengan semua fields yang dibutuhkan di method render, dan memanggil fungsi callback
    // tersebut setelah selesai melakukan request dan meneruskan response yang didapat ke fungsi callback
    // tersebut
    FB.getLoginStatus(function(response) {
        if (response.status === 'connected') {
            FB.api('/me/posts', 'GET', function(response){
                console.log(response);
                if (response && !response.error) {
                    /* handle the result */
                    fun(response);
                }
                else {
                    swal({
                        text: "Something went wrong",
                        icon: "error"
                    });
                }
            });
        }
    });
};

const postFeed = (message) => {
    // Pastikan method ini menerima parameter berupa string message dan melakukan Request POST ke Feed
    // Melalui API Facebook dengan message yang diterima dari parameter.
    FB.api('/me/feed', 'POST', {message:message});
    swal("Your post has been posted", {
        icon: "success",
    }).then(() => {
        window.location.reload();
    });

};

const postStatus = () => {
    const message = $('#postInput').val();
    $('#postInput').val("");
    postFeed(message);
};
