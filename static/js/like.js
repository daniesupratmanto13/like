$(document).ready(function(){

    $('.like-post').submit(function(e){
        e.preventDefault()
        const post_id = $(this).attr('id')
        const like_text = $.trim($(`.like-btn${post_id}`).text())
        const url = $(this).attr('action')
        
        const likes = parseInt($.trim($(`.like-value${post_id}`).text()))
        let result
        
        $.ajax({
            type: 'POST',
            url: url,
            data: {
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken').val(),
                'post-id': post_id,
            },
            success: function(response) {
                if (like_text === 'Unlike'){
                    $.trim($(`.like-btn${post_id}`).text('Like'))
                    result = likes - 1
                } else {
                    $.trim($(`.like-btn${post_id}`).text('Unlike'))
                    result = likes + 1
                }
                $.trim($(`.like-value${post_id}`).text(result))
            },
            error: function(response) {
                console.log('errorrrrr', response)
            }
        })
    })

})
