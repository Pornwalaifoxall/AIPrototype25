document.getElementById('predictForm').addEventListener('submit', function(e) {
    e.preventDefault();

    const btnText = document.getElementById('btn-text');
    const loader = document.getElementById('loader');
    const resultBox = document.getElementById('result-box');
    const resultText = document.getElementById('result-text');
    const flowerImg = document.getElementById('flower-img'); // อ้างอิงรูปภาพ

    // Reset State
    btnText.style.display = 'none';
    loader.style.display = 'block';
    
    // ซ่อนกล่องผลลัพธ์และรูปภาพก่อน
    resultBox.style.opacity = '0';
    resultBox.style.display = 'none';
    flowerImg.style.display = 'none'; 

    const formData = new FormData();
    formData.append('sepal_length', document.getElementById('sl').value);
    formData.append('sepal_width', document.getElementById('sw').value);
    formData.append('petal_length', document.getElementById('pl').value);
    formData.append('petal_width', document.getElementById('pw').value);

    fetch('/predict', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        btnText.style.display = 'block';
        loader.style.display = 'none';

        resultBox.style.display = 'block';
        void resultBox.offsetWidth; 
        resultBox.style.opacity = '1';

        if(data.success) {
            resultBox.className = 'success';
            resultText.innerHTML = 'Predicted Species: <strong>' + data.prediction + '</strong>';
            
            // ตั้งค่ารูปภาพและแสดงผล
            flowerImg.src = data.image_url;
            flowerImg.style.display = 'block';
        } else {
            resultBox.className = 'error';
            resultText.innerHTML = 'Error: ' + data.error;
        }
    })
    .catch(error => {
        console.error('Error:', error);
        btnText.style.display = 'block';
        loader.style.display = 'none';
        resultBox.className = 'error';
        resultText.innerHTML = 'An unexpected error occurred.';
    });
});