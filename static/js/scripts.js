$('form[name=signup_form]').submit(function(e) {
    e.preventDefault();
    const form = $(this)
    const data = form.serialize();
    const error = $('.error');
    $.ajax({
        url: '/auth/signup',
        type: 'POST',
        data: data,
        dataType: "json",
        success: function(response) {
            alert('You may now login!')
            window.location.href = '/auth/login'
        },
        error: function(response) {
            const message = response.responseJSON.message;
            error.text(message);
            error.removeClass('error--hidden');
            setTimeout(() => {
                error.addClass('error--hidden')
            }, 4000)
        }
    })
})


$('.fav-button').on('click', function() {
    let elem = $(this)
    let datamid = elem.data('mid');
    let remove = elem.data('remove')
    $.ajax({
        url: '/movies/add-fav?remove='+remove,
        method: 'post',
        headers: {
            'Content-Type': 'application/json;utf-8'
        },
        data: JSON.stringify({movie_id: datamid}),
        success: function(response) {
            let msg = ''
            if(remove == 1) {
                elem.text('ADD FAVORITE')
                elem.removeClass('fav')
                msg = 'Removed from favorites';
            } else {
                elem.text('FAVORITE')
                elem.addClass('fav')
                msg = 'Added to favorites';
            }
            
            alert(msg)
        },
        error: function(e) {
            alert('Oops, something went wrong');
        }
        
    })
})