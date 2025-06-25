$(document).ready(function() {
    
    $(document).on('click', '.like-btn', function(e) {
        e.preventDefault();
        const button = $(this);
        const postId = button.data('post-id');

        $.ajax({
            type: 'POST',
            url: '/like-post/',
            data: {
                'post_id': postId,
                'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()
            },
            success: function(response) {
                console.log("Response:", response);

              
                button.toggleClass('btn-primary btn-outline-primary');
                button.find('i')
                    .toggleClass('far fas')


              
                button.find('.like-count').text(response.like_count);
            },
            error: function(xhr) {
                console.log("Error:", xhr.responseText);
            }
        });
    });
});
