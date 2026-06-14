$(document).ready(function () {
    // 1. Listen for the click event to slide the sheet up
    $(document).on('click', '#prescriptions-btn', function (e) {
        e.preventDefault();
        $('#prescriptionPopupModal').addClass('show-sheet');
    });

    // 2. Listen for the close actions (X button or Close button) to slide it down
    $(document).on('click', '#prescriptionPopupModal [data-dismiss="modal"]', function (e) {
        e.preventDefault();
        $('#prescriptionPopupModal').removeClass('show-sheet');
    });
});