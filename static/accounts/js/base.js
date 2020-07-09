(function($) {
    $(function() {
        var selectField = $('#id_number_of_images'),
            oneimage = $('.oneimage');
            twoimages = $('.twoimages');
            threeimages = $('.threeimages');
            fourimages = $('.fourimages');
            fiveimages = $('.fiveimages');

        function toggleImages(value) {
            if (value === '1') {
                oneimage.show();
                twoimages.hide();
                threeimages.hide();
                fourimages.hide();
                fiveimages.hide();
            }

            else if (value === '2') {
                oneimage.show();
                twoimages.show();
                threeimages.hide();
                fourimages.hide();
                fiveimages.hide();
            }

            else if (value === '3') {
                oneimage.show();
                twoimages.show();
                threeimages.show();
                fourimages.hide();
                fiveimages.hide();
            }

            else if (value === '4') {
                oneimage.show();
                twoimages.show();
                threeimages.show();
                fourimages.show();
                fiveimages.hide();

            }

            else if (value === '5') {
                oneimage.show();
                twoimages.show();
                threeimages.show();
                fourimages.show();
                fiveimages.show();
            }


            else {
                oneimage.hide();
                twoimages.hide();
                threeimages.hide();
                fourimages.hide();
                fiveimages.hide();
            }
        }

        // show/hide on load based on pervious value of selectField
        toggleImages(selectField.val());

        // show/hide on change
        selectField.change(function() {
            toggleImages($(this).val());
        });
    });
})(django.jQuery);
