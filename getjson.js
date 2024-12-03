// 获取所有 .operator 下的 img 元素
const images = document.querySelectorAll('.operator img');
const imageUrls = {};

// 遍历所有图片
images.forEach(img => {
    const src = img.src;
    const filename = src.split('/').pop();  // 获取图片的文件名
    const parts = filename.split('_');     // 半身像_乌尔比安_1.png
    const newFilename = decodeURIComponent(parts[1]);  // 使用 decodeURIComponent 解码中文字符

    imageUrls[newFilename] = src;
});

console.log(JSON.stringify(imageUrls, null, 2));  // 格式化 JSON，缩进为 2 个空格
