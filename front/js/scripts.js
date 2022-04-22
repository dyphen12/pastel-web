// --------- STOCKDOTSHOP ----------

// These are the functions of the main Stockdotshop app
// Status: Under Development
// Note: Fixes for organization a better standard resourcing of functions


// ########## INDEX MAIN PROCESSES ########

function getUsername(ssid) {

    var std = "http://127.0.0.1:5000/user/%";


    var url = std.replace('%', ssid);

    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')


      } else {
        console.log('Sy')

        document.getElementById("user-welcome").innerHTML = 'Saludos, ' + res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}

function loadHome() {

  // RYZEN: First (R1)
  console.log('R1 Started')

  // This deletes some item that bothers.


  // Loads Sneaker Live Table Routine


  // Start SSID
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {

  // R1 Fail end
    //document.getElementById("mySidebar").innerHTML = '';
    //document.getElementById("pageC").innerHTML = 'Please Login';
    console.log('Please Login')
    HomeData();

  }
  else {

    makelogin();

    // RYZEN: Second (R2)
    console.log('R2 Started')

    // First Message to Console

    console.log(ssid);
    console.log('Somos los que somos');

    // User's name routines

    // Get user name from index.html (this is a faulty one) needs to be in a future onload for index only.
    getUsername(ssid);

  }

}

function HomeData() {



    apiVersion();

    return true;

}

// -------- LOGIN ----------

// Registration Process

function SignUpNow() {

    document.getElementById("signup-status").innerHTML = 'Signing up...';

    var std = "http://127.0.0.1:5000/signup/%";

    var query = '{"results": {"name": "%","lastname": "#","email": "&","password": "$"}}'

    var signname = document.getElementById("name").value;
    var signlastname = document.getElementById("lastname").value;
    var signemail = document.getElementById("email").value;
    var signpassword = document.getElementById("signpassword").value;

    console.log(query);

    var query1 = query.replace('%', signname);
    var query2 = query1.replace('#', signlastname);
    var query3 = query2.replace('&', signemail);
    var query4 = query3.replace('$', signpassword);

    if (signname == '' || signlastname == '' || signemail == '' || signpassword == '' ) {

        document.getElementById("signup-status").innerHTML = 'Fill the entire form';
        return true



    }

    var url = std.replace('%',query4)

       var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);



      if (res == 'User Already Registered'){
        console.log(res)




      } else {

      document.getElementById("signup-status").innerHTML = 'Eureka!';

        var cookiephrase = 'ssid=';

        var ssidcookie = cookiephrase + res;

        sessionStorage.setItem('ssid',res);

        location.href='user.html';

        console.log(res)



        // document.getElementById("img-status").innerHTML = 'Images inserted successfully, sync and check your drive!';
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();

    return true;
}

// Front: Called on Index
function login() {

    document.getElementById("login-message").innerHTML = 'Iniciando Sesión...';

    var x , y;

    // Get the value of the input field with id="numb"
    x = document.getElementById("login-mail").value;
    y = document.getElementById("loginpass").value;

    var token = "user=%&pass=$"
    var credentialx = token.replace('%',x);
    var credential = credentialx.replace('$',y);


    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);

      //signup-message




      if (res == 'fail'){
        // document.getElementById("demo").innerHTML = 'Wrong password or username';

        document.getElementById("signup-message").innerHTML = 'Usuario u contraseña incorrectos';

      } else {
        // document.getElementById("demo").innerHTML = 'Succesfully Logged in';
        var cookiephrase = 'ssid=';
        var ssidcookie = cookiephrase + res;
        sessionStorage.setItem('ssid',res);
        var andnavcontainer = document.getElementById('nav-cont');

        andnavcontainer.innerHTML = '';

        makelogin();
        location.reload();
      }

      }
    };
    xhttp.open("POST", "http://127.0.0.1:5000/auth", true);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send(credential);

}

// Back Processes
function setCookie(key, value) {
            var expires = new Date();
            expires.setTime(expires.getTime() + (1 * 24 * 60 * 60 * 1000));
            document.cookie = key + '=' + value + ';expires=' + expires.toUTCString();
        }

// Called on: login()>makelogin() / R2 /
// Just changes the Header to an Logged Header
function makeloginProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

    var drawSignin = document.getElementById('draw-signin').innerHTML = 'Bienvenido';
    var drawLogin = document.getElementById('draw-login').style.display = 'none';
    document.getElementById('more-button').style.display = 'inline';

    document.getElementById('draw-signin').onclick = dummy;


    //Nav Container
          var navcontainer = document.createElement("nav");

          navcontainer.className = "android-navigation mdl-navigation";

          // Four childs

          // Child 1 - a

          var aname = document.createElement("a");

          aname.className = "mdl-navigation__link mdl-typography--text-uppercase";

          aname.innerHTML = 'Bienvenido, ';

          aname.id = 'user-welcome';

          navcontainer.appendChild(aname);

       // document.getElementById('loginbots').style.display = "inline";


       var andnavcontainer = document.getElementById('nav-cont');

          andnavcontainer.appendChild(navcontainer)

      resolve('makeloginProcess() ended');
    }, 0);
  });
}

// Called on: Login
async function makelogin() {

  console.log('calling');
  const result = await makeloginProcess();
  console.log(result);
  document.getElementById('loginbots').style.display = 'none';
  loaduser();


  // expected output: "resolved"
}

// Front Ad hoc

function toggleloginProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

        document.getElementById('loginbots').style.display = "inline";

      resolve('resolved');
    }, 2);
  });
}

async function togglelogin() {
  console.log('calling');
  const result = await toggleloginProcess();
  console.log(result);
  // expected output: "resolved"
}

function togglesignupProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

        document.getElementById('saininbots').style.display = "inline";

      resolve('resolved');
    }, 2);
  });
}

async function togglesignup() {
  console.log('calling');
  const result = await togglesignupProcess();
  console.log(result);
  // expected output: "resolved"
}

function gosignupProcess() {
  return new Promise(resolve => {
    setTimeout(() => {

        document.getElementById('formasignup').innerHTML = 'Loading...';



      resolve('resolved');
    }, 2);
  });
}

async function gosignup() {
  console.log('calling');
  const result = await gosignupProcess();
  console.log(result);
  // expected output: "resolved"
}

// ########## USER APP MAIN PROCESSES ########


function logout() {
  sessionStorage.removeItem('ssid');
  window.location.href = "index.html";

}

// COOKIES

function getCookie(cname) {
  var name = cname + "=";
  var decodedCookie = decodeURIComponent(document.cookie);
  var ca = decodedCookie.split(';');
    for(var i = 0; i <ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') {
          c = c.substring(1);
                    }
          if (c.indexOf(name) == 0) {
            return c.substring(name.length, c.length);
                    }
                  }
                  return "";
}

function getUsernameprofile(ssid) {

    var std = "http://127.0.0.1:5000/user/%";


    var url = std.replace('%', ssid);

    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')


      } else {
        console.log('Sy')

        document.getElementById("hello-user").innerHTML = 'Hola, ' + res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}


// --------- USER DATA ----------

function loaduser() {


  // RYZEN: First (R1)
  console.log('R1 Started')

  apiVersion();

  // This deletes some item that bothers.
  document.getElementById('more-button').style.display = 'none';
  var andnavcontainer = document.getElementById('nav-cont');
  andnavcontainer.innerHTML = '';


  // Start SSID
  let ssid = sessionStorage.getItem('ssid');
  if (ssid == null) {

  // R1 Fail end
    document.getElementById("hello-user").innerHTML = 'Please Login';
    document.getElementById("stockdotshop-content").innerHTML = '';
    document.getElementById("sneaker-user").innerHTML = '';
    document.getElementById("sneaker-live").innerHTML = '';
    console.log('Please Login')

  }
  else {


    // RYZEN: Second (R2)
    console.log('R2 Started')


    // First Message to Console

    console.log(ssid);
    console.log('Somos los que somos');


    // User's name routines


    // Get user name from index.html (this is a faulty one) needs to be in a future onload for index only.
    getUsername(ssid);

    // Get user name for user.html (this is the main one for the profile so thats why)
    // So it only changes the "Hello, user"
    getUsernameprofile(ssid);

    // Does the header changing for user.html
    makeloginProcess();
    document.getElementById('more-button').style.display = 'inline';

  }

}

function dummy() {

  console.log('I love you!');

}

// Api Version

function apiVersion() {

    var std = "http://127.0.0.1:5000/";


    document.getElementById("version").innerHTML = 'Loading...';

    var url = std

    //document.getElementById("demo").innerHTML = credential;

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {

      var res = JSON.parse(this.responseText);
      console.log(res);


      if (res == 'fail'){
        console.log('Fail')

      } else {
        console.log('Sy')
        document.getElementById("version").innerHTML = res;
      }

      }
    };
    xhttp.open("GET", url);
    xhttp.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhttp.send();


    return true;
}
