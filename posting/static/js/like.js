const $test = document.querySelector('.like-form')

  const toggleLike = () => {
    console.log('toggleLike호출도 잘되는데')
    const csrftoken = getCookie('csrftoken');
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    fetch("{% url 'posting:like' posting.pk %}", {
      method: "POST",
      headers: {
          "X-CSRFToken": csrftoken,
      },
      body: JSON.stringify({
          myData: "Here's my posted data!"
      })
    }).then(res=>{
      return res.json();
    }).then(data => {
      console.log(data);
    }).catch(() => {
      console.error("Errororroroor", error);
    })
  }

  $test.onsubmit = e => {
    e.preventDefault()
    console.log('onsubmit까진 잘됐는데')
    
    toggleLike()
  }