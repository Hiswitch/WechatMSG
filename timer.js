// 设置目标日期，可以是一个将来的日期
const targetDate = new Date('2022-10-31T22:00:00');

function updateTimer() {
    // 获取当前时间
    const now = new Date();
    
    // 计算剩余时间
    const timeDiff = now - targetDate;
    
    // 将剩余时间转换成天、小时、分钟和秒
    const days = Math.floor(timeDiff / (1000 * 60 * 60 * 24));
    const hours = Math.floor((timeDiff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    const minutes = Math.floor((timeDiff % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeDiff % (1000 * 60)) / 1000);
    
    // 将时间显示在页面上
    document.getElementById('timer').innerHTML = `
        <p>我们已经在一起</p>
        <p>${days} 天 ${hours} 小时 ${minutes} 分钟 ${seconds} 秒</p>
    `;
}

// 每秒更新一次计时器
setInterval(updateTimer, 1000);