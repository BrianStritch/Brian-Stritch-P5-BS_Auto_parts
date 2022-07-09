
/* *************** Function to toggle toasts display property *************/
$('#close_btn').click(closeMessageBox);
function closeMessageBox() {
    document.getElementById('msg-box').classList.remove('d-block');
    document.getElementById('msg-box').classList.add('d-none');
}

