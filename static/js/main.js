/*
This is to add functionality to the buttons on the reservation page
*/

// This will load after the page is loaded
document.addEventListener("DOMContentLoaded", function() {

  // Selects all the reservations, as they are in a card class
  document.querySelectorAll(".card").forEach(function(card) {

    // Store the buttons in const
    const editBtn = card.querySelector(".edit-btn");
    const saveBtn = card.querySelector(".save-btn");
    const cancelBtn = card.querySelector(".cancel-btn");
    const deleteBtn = card.querySelector(".delete-btn");
    const inputs = card.querySelectorAll("input");

    // To skip cards with no button
    if (!editBtn) return;

    // To remove the readonly in the inputs
    editBtn.addEventListener("click", function() {
      inputs.forEach(i => i.readOnly = false);
      editBtn.classList.add("d-none");
      saveBtn.classList.remove("d-none");
      cancelBtn.classList.remove("d-none");
    });

    // Revert readonly to true
    cancelBtn.addEventListener("click", function() {
      inputs.forEach(i => i.readOnly = true);
      // To show the edit button again
      editBtn.classList.remove("d-none");
      // hide the save and cancel buttons
      saveBtn.classList.add("d-none");
      cancelBtn.classList.add("d-none");
    });

    // If a delete button exists, it will add the eventlistener
    if (deleteBtn) {
      deleteBtn.addEventListener("click", function() {
        // Get the URL to delete the post
        const deleteUrl = card.querySelector("form").getAttribute("data-delete-url");
        if (deleteUrl) {
          // Redirect to the delete URL
          window.location.href = deleteUrl;
        } else {
          alert("Delete URL not configured.");
        }
      });
    }
  });
});