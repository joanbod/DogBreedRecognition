//SHOW UPLOADED IMAGE
function readURL(input) {
    if (input.files && input.files[0]) {
        var reader = new FileReader();
 
        reader.onload = function (e) {
            $('#imageResult')
                .attr('src', e.target.result);
        };
        reader.readAsDataURL(input.files[0]);
    }
}
 
$(function () {
    $('#upload-image').on('change', function () {
        readURL(this);
    });
});
 
//SHOW UPLOADED FILE NAME
var input = document.getElementById( 'upload-image' );
var infoArea = document.getElementById( 'upload-image-name' );
 
input.addEventListener( 'change', showFileName );
function showFileName( event ) {
  var input = event.srcElement;
  var fileName = input.files[0].name;
  infoArea.textContent = 'File name: ' + fileName;
}

