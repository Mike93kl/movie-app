$(document).ready(function() {
    const tab = localStorage.getItem('ctab') || null;
    if(tab) {
        $(tab).click();
    }
});


$('.nav-item').on('click', function() {
    const id = $(this).attr('id') || null;
    localStorage.setItem('ctab', '#'+id)
});

$('form[name=signup_form]').submit(function(e) {
    e.preventDefault();
    const form = $(this)
    let data = form.serialize();
    const error = $('.error');

    const isAdmin = confirm('Click OK to create user as ADMIN or cancel for plain USER');
    data+='&is_admin='+isAdmin;
    console.log(data);
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


$('.nav-to-movie').on('click', function(e) {
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
                $('#new-comment').val('')
            }
        },
        error: function(e) {
            alert(e.responseJSON && e.responseJSON.message ? e.responseJSON.message: 'Oops, something went wrong');
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
            alert(e.responseJSON && e.responseJSON.message ? e.responseJSON.message:'Oops, something went wrong');
        }
        
    })
})