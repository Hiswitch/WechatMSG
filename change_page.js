const container = document.querySelector('.container');
let currentPage = 0;

function goToPage(pageIndex) {
  if (pageIndex < 0 || pageIndex >= pages.length) {
    return;
  }

  const currentPosition = -100 * currentPage;
  const newPosition = -100 * pageIndex;

  container.style.transform = `translateY(${newPosition}vh)`;

  currentPage = pageIndex;
}

// 根据鼠标滚动切换页面
window.addEventListener('keydown', (event) => {
    if (event.key === 'ArrowLeft' && currentPage > 0) {
      goToPage(currentPage - 1);
    } else if (event.key === 'ArrowRight' && currentPage < container.children.length - 1) {
      goToPage(currentPage + 1);
    }
  });

window.addEventListener('wheel', (event) => {
    if (event.deltaY > 50 && currentPage < container.children.length - 1) {
        goToPage(currentPage + 1);
    } else if (event.deltaY < -50 && currentPage > 0) {
        goToPage(currentPage - 1);
    }
});

