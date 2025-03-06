const ctx = document.getElementById('myChart').getContext('2d');
const chart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [],
        datasets: [{
            label: 'Real-Time Data',
            data: [],
            borderColor: 'blue',
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            x: { display: true },
            y: { display: true }
        }
    }
});

const ws = new WebSocket('ws://localhost:8000/ws/data');
ws.onmessage = function(event) {
    const jsonData = JSON.parse(event.data);
    if (chart.data.labels.length > 20) {
        chart.data.labels.shift();
        chart.data.datasets[0].data.shift();
    }
    chart.data.labels.push(jsonData.time);
    chart.data.datasets[0].data.push(jsonData.value);
    chart.update();
};