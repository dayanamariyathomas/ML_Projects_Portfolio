function validateForm() {
    // Retrieve the form fields
    var crimInput = document.getElementById("CRIM");
    var znInput = document.getElementById("ZN");
    var indusInput = document.getElementById("INDUS");
    var rmInput = document.getElementById("RM");
    var ptratioInput = document.getElementById("PTRATIO");
    var lstatInput = document.getElementById("LSTAT");
  
    // Perform validation checks
    if (crimInput.value === "") {
      alert("Please enter a value for CRIM");
      return false;
    }
  
    if (znInput.value === "") {
      alert("Please enter a value for ZN");
      return false;
    }
  
    if (indusInput.value === "") {
      alert("Please enter a value for INDUS");
      return false;
    }
  
    if (rmInput.value === "") {
      alert("Please enter a value for RM");
      return false;
    }
  
    if (ptratioInput.value === "") {
      alert("Please enter a value for PTRATIO");
      return false;
    }
  
    if (lstatInput.value === "") {
      alert("Please enter a value for LSTAT");
      return false;
    }
  
    // If all validations pass, return true to submit the form
    return true;
  }
  