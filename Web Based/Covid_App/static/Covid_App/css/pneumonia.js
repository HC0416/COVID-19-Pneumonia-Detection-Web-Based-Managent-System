if(!localStorage.getItem('#insertName')){
    localStorage.setItem('#insertName', "");
}

if(!localStorage.getItem('#insertAge')){
    localStorage.setItem('#insertAge', null);
}

if(!localStorage.getItem('#insertGender')){
    localStorage.setItem('#insertGender', "");
}

if(!localStorage.getItem('#insertphone')){
    localStorage.setItem('#insertphone', "");
}

var button1 = false;
var button2 = false;
var formSubmit = true;

document.addEventListener('DOMContentLoaded', function(){
    
    document.querySelector('#insertName').value = localStorage.getItem('#insertName');
    document.querySelector('#insertAge').value = localStorage.getItem('#insertAge');
    document.querySelector('#insertGender').value = localStorage.getItem('#insertGender');
    document.querySelector('#insertPhone').value = localStorage.getItem('#insertPhone');

    document.querySelector('#formsubmit1').onclick = () =>{

        button1 = true;
        const name = document.querySelector('#insertName').value;
        const age = document.querySelector('#insertAge').value;
        const gender = document.querySelector('#insertGender').value;
        const phone = document.querySelector('#insertPhone').value;

        console.log(name);
        localStorage.setItem('#insertName', name);
        localStorage.setItem('#insertAge', age);
        localStorage.setItem('#insertGender', gender);
        localStorage.setItem('#insertPhone', phone);

        document.getElementById("remark").focus();
    }

    document.querySelector('#formsubmit2').onclick = () =>{

        button2 = true;
        console.log("Success!")
        localStorage.setItem('#insertName', '');
        localStorage.setItem('#insertAge', '');
        localStorage.setItem('#insertGender', '');
        localStorage.setItem('#insertPhone', '');
    }

    
})

var formValidation = function(){
    var name = document.forms["xray-scan"]["insertName"].value;
    var age = document.forms["xray-scan"]["insertAge"].value;
    var gender = document.forms["xray-scan"]["insertGender"].value;
    var remark = document.forms["xray-scan"]["remark"].value;
    var phone = document.forms["xray-scan"]["insertPhone"].value;

    var filePath = document.forms["xray-scan"]["filePath"].value;
    var XrayImage = document.forms["xray-scan"]["XrayImage"].value;

    if(button2 == true){
        if (name == "" || age== null || phone == "" || gender =="" || remark=="" || XrayImage == "") {
            // nameValid.innerText = "Name is required!"
            alert("Please Fill Up All The Required Field");
            return false;
        }
    }

    if(button1 == true){
        if (filePath == ""){
            alert("Please Upload an X-ray");
            return false;
        }
    }
}

var appointmentValidation = function(){
    var name = document.forms["apppointment-form"]["name"].value;
    var number = document.forms["apppointment-form"]["Pnumber"].value;
    var email = document.forms["apppointment-form"]["email"].value;


    if(name == "" || number== "" || email == ""){
        alert("Please Full Up All The Required Field");
        return false;
    }

    formSubmit = true;

    // else{
    //     alert("Your Booking Appointment Had Been Successfully Sent!");
    // }
}
