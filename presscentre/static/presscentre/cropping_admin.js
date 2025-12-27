$(document).ready(function() {
    // Функция для обновления cropping виджета при изменении изображения
    function updateCroppingWidget() {
        // Находим cropping контейнер
        var croppingContainer = $('.image-ratio[data-field-name="cropping"]');

        if (croppingContainer.length > 0) {
            // Получаем URL нового изображения
            var imageInput = $('#id_image');
            var imageUrl = '';

            if (imageInput.length > 0 && imageInput[0].files && imageInput[0].files[0]) {
                // Новое изображение выбрано
                imageUrl = URL.createObjectURL(imageInput[0].files[0]);
            } else if (imageInput.next('.clearable-file-input').find('a').length > 0) {
                // Существующее изображение
                imageUrl = imageInput.next('.clearable-file-input').find('a').attr('href');
            }

            if (imageUrl) {
                // Обновляем изображение в cropping виджете
                var img = croppingContainer.find('img');
                if (img.length > 0) {
                    img.attr('src', imageUrl);
                }

                // Переинициализируем cropping
                setTimeout(function() {
                    if (window.ImageCropping && window.ImageCropping.init) {
                        window.ImageCropping.init();
                    }
                }, 100);
            }
        }
    }

    // Обработчик изменения изображения
    $('#id_image').change(function() {
        setTimeout(updateCroppingWidget, 200);
    });

    // Также проверяем существующее изображение
    if ($('#id_image').next('.clearable-file-input').find('a').length > 0) {
        setTimeout(updateCroppingWidget, 500);
    }
});