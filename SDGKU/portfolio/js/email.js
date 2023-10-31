// THIS IS EXCUUTED WHEN THE USER PRESSES "SEND EMAIL"
document.getElementById("emailForm").addEventListener("submit", function(event){

    event.preventDefault();//

    const form = event.target; //THIS IS THE ELEMENT THAT IS GETTING THE SUBMIT ACTION (THIS FORM)

    // GET VALUES
    const name = form.elements.name.value;
    const email = form.elements.email.value;
    const subject = form.elements.subject.value;
    const message = form.elements.message.value;

    // NOW! LETS'S GO AND CREATE YOUR EMAIL JS ACCOUNTS :emailjs.com
    emailjs.init("6Cn1J20DJW_x_dmAr");

    // THIS IS THE OBJECT INSTURCTION TO SEND EMAILS
    const params = {
        from_email: email,
        from_name: name,
        subject: subject,
        message: message
    };

    // VERIFY IF THE SUBJSCT IS EMPTY
    if (!subject) {
        const result = confirm("Subject is empty. Are you sure you want to send the email");
        // RETURNS OK = TRUE

        if(result === true) {
            sendEmail();
        }else {
            // DONT NEED ELSE
        }
    } else {
        sendEmail();
    }

    function sendEmail() {

        emailjs.send("service_isoz6qb", "template_xj27sa6", params).send(function(response){
            alert("Email was sucessfully sent");
            form.reset(); //Clear the form
        }, function (error) {
            alert("Error sending email");
        });
    }

    

});