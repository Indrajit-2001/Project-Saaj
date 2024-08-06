let modalBtns = [...document.querySelectorAll(".button")];
    modalBtns.forEach(function (btn) {
      btn.onclick = function () {
        let modal = btn.getAttribute("data-modal");
        document.getElementById(modal).style.display = "block";
      };
    });
    let closeBtns = [...document.querySelectorAll(".close")];
    closeBtns.forEach(function (btn) {
      btn.onclick = function () {
        let modal = btn.closest(".modal");
        modal.style.display = "none";
      };
    });
    window.onclick = function (event) {
      if (event.target.className === "modal") {
        event.target.style.display = "none";
      }
    };

    const validateEmail = (email) => {
      return email.match(
        /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      );
    };
    const validateNumber = (number) => {
      return number.match(
        /^[6-9]\d{9}$/
      );
    };
    submit=document.getElementById('submit')
    submit.addEventListener('click',check)
    function check(event){
      if (document.forms["booking"]["name"].value=="")
      {  
          alert("Please enter your name");  
          console.log('Empty name')
          // event.preventDefault()
      } 
      else if (document.forms["booking"]["email"].value=="")
      {  
          alert("Please enter the Name");  
          console.log('Empty name')
          // event.preventDefault()
      }  
      else if(!validateEmail(document.forms["booking"]["email"].value)){
        alert("Please enter a valid email id"); 
        // event.preventDefault()
      }
      else if (document.forms["booking"]["phone"].value=="")
      {  
          alert("Please enter the Phone number"); 
          // event.preventDefault()
          console.log()
      }  
      else if(!validateNumber(document.forms["booking"]["phone"].value)){
        alert("Please enter the valid Phone number");  
        // event.preventDefault()
      }
      else if (document.forms["booking"]["date"].value=="")
      {  
          alert("Please enter the your suitable Date");  
          console.log('Empty name')
          // event.preventDefault()
      }      
      else if (new Date() > new Date(document.forms["booking"]["date"].value))
      {  
          alert("Please enter the valid Date");
          // event.preventDefault()
      } 
    }