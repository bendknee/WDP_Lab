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
            '<div class="profile">' +
            '<img class="cover" src="' + user.cover.source + '" alt="cover" />' +
            '<img class="picture" src="' + user.picture.data.url + '" alt="profpic" />' +
            '<div class="data">' +
            '<h1>' + user.name + '</h1>' +
            '<h2>' + user.about + '</h2>' +
            '<h3>' + user.email + ' - ' + user.gender + '</h3>' +
            '</div>' +
            '</div>' +
            '<input id="postInput" type="text" class="post" placeholder="Ketik Status Anda" />' +
            '<button class="postStatus" onclick="postStatus()">Post ke Facebook</button>' +
            '<button class="logout" onclick="facebookLogout()">Logout</button>'
        );

        // Setelah merender tampilan di atas, dapatkan data home feed dari akun yang login
        // dengan memanggil method getUserFeed yang kalian implementasi sendiri.
        // Method itu harus menerima parameter berupa fungsi callback, dimana fungsi callback
        // ini akan menerima parameter object feed yang merupakan response dari pemanggilan API Facebook
        getUserFeed(feed => {
            feed.data.map(value => {
            // Render feed, kustomisasi sesuai kebutuhan.
            if (value.message && value.story) {
            $('#lab8').append(
                '<div class="feed">' +
                '<h1>' + value.message + '</h1>' +
                '<h2>' + value.story + '</h2>' +
                '</div>'
            );
        } else if (value.message) {
            $('#lab8').append(
                '<div class="feed">' +
                '<h1>' + value.message + '</h1>' +
                '</div>'
            );
        } else if (value.story) {
            $('#lab8').append(
                '<div class="feed">' +
                '<h2>' + value.story + '</h2>' +
                '</div>'
            );
        }
    });
    });
    });
    } else {
        // Tampilan ketika belum login
        $('#lab8').html(
            '<div id="fb-root"></div>\n' +
            '<script>(function(d, s, id) {\n' +
            '  var js, fjs = d.getElementsByTagName(s)[0];\n' +
            '  if (d.getElementById(id)) return;\n' +
            '  js = d.createElement(s); js.id = id;\n' +
            '  js.src = \"https://connect.facebook.net/en_GB/sdk.js#xfbml=1&version=v2.11&appId=2004678579769743\";\n' +
            '  fjs.parentNode.insertBefore(js, fjs);\n' +
            '}(document, \'script\', \'facebook-jssdk\'));</script>'+
            '<div class="fb-login-button" data-max-rows="1" data-size="large" data-button-type="login_with" ' +
            'data-show-faces="false" data-auto-logout-link="true" data-use-continue-as="false"></div>'
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

// TODO: Lengkapi Method Ini
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
    // TODO: Implement Method Ini
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
    // Todo: Implement method ini,
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
