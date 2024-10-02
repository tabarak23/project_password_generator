document.getElementById('generate').addEventListener('click', async () => {
    const length = document.getElementById('length').value;
    const response = await fetch('/generate', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ length: parseInt(length) })
    });

    const data = await response.json();
    const resultDiv = document.getElementById('result');

    if (response.ok) {
        resultDiv.textContent = `Generated Password: ${data.password}`;
        resultDiv.classList.add('success'); // Add the success class
    } else {
        resultDiv.textContent = `Error: ${data.error}`;
        resultDiv.classList.add('error'); // Add the error class
    }
});