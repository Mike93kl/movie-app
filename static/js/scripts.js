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


$('.movie-card').on('click', function() {
    let datamid = $(this).data('mid');
    console.log(datamid)
    $.ajax({
        url: '/movies/add-fav',
        method: 'post',
        headers: {
            'Content-Type': 'application/json;utf-8'
        },
        data: JSON.stringify({movie_id: datamid}),
        success: function(response) {
            $(`#fav-${datamid}`).text('FAVORITE')
            alert('Added to favorites')
        },
        error: function(e) {
            console.log(e)
        }
        
    })
})