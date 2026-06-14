let uniqueIdCounter = Math.floor(Math.random() * 1000);

function generate12DigitId() {
    // 1. Get the current Unix timestamp in seconds (10 digits)
    let timestampStr = Math.floor(Date.now() / 1000).toString(); 
    
    // 2. Increment the counter and wrap it securely around 1000 (0 to 999)
    uniqueIdCounter = (uniqueIdCounter + 1) % 1000;
    
    // Pad to exactly 5 digits to match the % 1000 wrap-around
    let counterStr = uniqueIdCounter.toString().padStart(5, '0');
    
    // 3. To get a strict 10-digit ID, take the LAST 7 digits of the timestamp 
    // and append the 3-digit counter. (7 digits + 3 digits = 10 digits)
    let uniqueId = timestampStr.substring(timestampStr.length - 7) + counterStr;
    
    return parseInt(uniqueId, 10);
}
$(document).ready(function(e){
    window.console && console.log("patients script loaded");
    $("#btn-add-patient").click(function(){
        window.console && console.log("add patient clicked");
        const patinetID=generate12DigitId();
        const firstname=$("#firstname").val();
        const lastname=$("#lastname").val();
        const date_of_birth=$("#date_of_birth").val();
        const gender=$("#gender").val();
        const hometown=$("#hometwon").val();
        const phone_number=$("#phone_number").val();
        window.console && console.log("patientID: "+patinetID)
        window.console && console.log(firstname)
        /*
        if(firstname.length<1){
            alert("Firstname must be filled");
        }
        if(last.length<1){
            alert("Lastame must be filled");
        }
        if(date_of_birth.length<1){
            alert("Date of birthe must be filled");
        }
        if(gender==0){
            alert("Gender must be selected");
        } 
        if(hometown.length<1){
            alert("Hometwon must be field");
        }      
        if(phoneNumber.length<1){
            alert("Phone Number must be field");
        }
        $.ajax({
            url:"/add-new-patient",
            type:"POST",
            data:{
                patientID:  patinetID,
                firstname:  firstname,
                lastname: lastname,
                date_of_birth:  date_of_birth,
                gender:gender,
                hometown:  hometown,
                phone_number:phone_number
            },
            success: function(response){
                console.log(response);
            },
            error: function(e){
                console.log("error");
            }
               
        });
         */
    });
});