let postings = [];
const $postings_ul = document.querySelector('.postings_ul');
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
    console.log('쿠키가만들어지는중입니다.');
  }
  return cookieValue;
}
const csrftoken = getCookie('csrftoken');
const getPostings = () => {
  fetch('http://localhost:8000/', {
    method: 'GET',
    credentials: 'include',
    headers: {
      Accept: 'application/json',
      'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
    },
  })
    .then(response => {
      return response.json(); //Convert response to JSON
    })
    .then(data => {
      console.log(data);
      $postings_ul.innerHTML = `<li>${data.msg}</li>`;
    });
  fetch('http://localhost:8000/', {
    method: 'POST',
    credentials: 'include',
    headers: {
      Accept: 'application/json',
      'Content-Type': 'application/json',
      'X-CSRFToken': csrftoken,
    },
    Accept: 'application/json',
    'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
    body: JSON.stringify({
      msg: "Here's my posted data!",
    }),
  })
    .then(res => {
      return res.json();
    })
    .then(data => {
      console.log(data);
      $postings_ul.innerHTML += `<li>${data.msg}</li>`;
    })
    .catch(() => {
      console.error('Errororroroor', error);
    });
};
// postings = [
//   {
//     profile_img_src: 'https://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/avatar.jpg',
//     user_pk: 5,
//     posting_img_src:
//       'http://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/2021070512algorithm.jpg',
//     posting_pk: 19,
//     likes: 2,
//   },
//   {
//     profile_img_src: 'https://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/avatar.jpg',
//     user_pk: 5,
//     posting_img_src:
//       'http://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/2021070512algorithm.jpg',
//     posting_pk: 19,
//     likes: 2,
//   },
//   {
//     profile_img_src: 'https://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/avatar.jpg',
//     user_pk: 5,
//     posting_img_src:
//       'http://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/2021070512algorithm.jpg',
//     posting_pk: 19,
//     likes: 2,
//   },
//   {
//     profile_img_src: 'https://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/avatar.jpg',
//     user_pk: 5,
//     posting_img_src:
//       'http://django-s3-practice-1.s3.ap-northeast-2.amazonaws.com/2021070512algorithm.jpg',
//     posting_pk: 19,
//     likes: 2,
//   },
// ];
// render();
console.log('lalalal');
// };
// const render = () => {
// $postings_ul.innerHTML = postings
//   .map(posting => {
//     return `<li class="posting">
//     <div class="author-profile">
//     <img class="profile-img"
//       src="${posting.profile_img_src}"
//       alt="프로필사진" />
//     <a href="/profile/${posting.user_pk}/"><span>${posting.user_pk}</span></a>
//     </div>
//     <div class="posting-detail">
//     <a class="posting-img" href="/posting/${posting.posting_pk}" title="게시물로 이동">
//     </a><img src="${posting.posting_img_src}" alt="업로드된 사진" /></a>
//     </li>`;
//   })
//   .join('');
// };

//   <form class="like-form" method="POST" action="/posting/like/19">
//     <p>
//       좋아요 <span class="like-count">0</span>

//       <button type="submit">좋아요</button>
//     </p>
//   </form>
//   <script type="text/javascript">
//     const $like_form = document.querySelector('.like-form');

//     const toggleLike = eventtarget => {
//       console.log('toggleLike호출도 잘된다');
//       const csrftoken = getCookie('csrftoken');
//       function getCookie(name) {
//         let cookieValue = null;
//         if (document.cookie && document.cookie !== '') {
//           const cookies = document.cookie.split(';');
//           for (let i = 0; i < cookies.length; i++) {
//             const cookie = cookies[i].trim();
//             // Does this cookie string begin with the name we want?
//             if (cookie.substring(0, name.length + 1) === name + '=') {
//               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//               break;
//             }
//           }
//         }
//         return cookieValue;
//       }
//       fetch('/posting/like/19', {
//         method: 'POST',
//         headers: {
//           'X-CSRFToken': csrftoken,
//         },
//         body: JSON.stringify({
//           msg: "Here's my posted data!",
//         }),
//       })
//         .then(res => {
//           return res.json();
//         })
//         .then(data => {
//           console.log(data);
//           eventtarget.querySelector('button').textContent = data['button_msg'];
//           eventtarget.querySelector('.like-count').textContent = data['count'];
//         })
//         .catch(() => {
//           console.error('Errororroroor', error);
//         });
//     };

//     $like_form.onsubmit = e => {
//       e.preventDefault();
//       console.log('onsubmit까진 잘된다');
//       toggleLike(e.target);
//     };
//   </script>
//   <a class="author-username" href="/profile/5/">test04</a> 제발
//   <div class="comments">
//     <ul class="comments-list reset-list"></ul>
//   </div>
// </div>
// </article>
// `;

document.addEventListener('DOMContentLoaded', getPostings);
