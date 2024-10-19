let dataStack = [];
let currentData = null;

// 載入 JSON 資料
fetch('products.json')
    .then(response => response.json())
    .then(data => {
        currentData = data;
        displayData(currentData);
    })
    .catch(error => console.error('Error loading data:', error));

// 顯示資料
function displayData(data) {
    const productList = document.getElementById('product-list');
    productList.innerHTML = '';

    if (Array.isArray(data)) {
        data.forEach(item => {
            const listItem = document.createElement('li');
            listItem.textContent = `${item.name} - $${item.price}`;
            productList.appendChild(listItem);
        });
    } else {
        for (const key in data) {
            const listItem = document.createElement('li');
            listItem.textContent = key;
            listItem.onclick = () => navigateTo(data[key]);
            productList.appendChild(listItem);
        }
    }

    // 更新返回按鈕狀態
    document.querySelector('.back-button').style.display = dataStack.length > 0 ? 'block' : 'none';
}

// 導航到下一層資料
function navigateTo(data) {
    dataStack.push(currentData);
    currentData = data;
    displayData(currentData);
}

// 返回上一層資料
function goBack() {
    if (dataStack.length > 0) {
        currentData = dataStack.pop();
        displayData(currentData);
    }
}
