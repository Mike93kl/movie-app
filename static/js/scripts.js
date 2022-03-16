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


$('.nav-to-movie').on('click', function() {
    let mid = $(this).data('mid');
    if(mid) {
        window.location.href = '/movies/' + mid
    }
})

$('#add-cs').on('click', function() {
    let mid = $(this).data('mid');
    let comment = $('#new-comment').val();
    $.ajax({
        url: '/movies/add-comment',
        method: 'post',
        headers: {
            'Content-Type': 'application/json;utf-8'
        },
        data: JSON.stringify({movie_id: mid, comment}),
        success: function(response) {
            if(response.user_id) {
                let user = $('#username').val()
                
                let div = `
                 <div class="comment">
                        <p class="user ${user == response.username ? 'is' : ''}">${response.username}</p>
                        <p class="user-cs">${response.comment}</p>
                </div>`
                $('.comment-list').first().append(div)
            }
        },
        error: function(e) {
            alert(e.message ? e.message : 'Oops, something went wrong');
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